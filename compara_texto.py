from os import posix_fallocate
import re
from socket import AF_UNIX
from tarfile import LENGTH_NAME
from unittest.mock import sentinel

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print()
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#testar
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    i = 0
    while i < len(as_a):
        soma = soma + (abs(as_a[i] - as_b[i]))
        i += 1
    # tamMed = abs(as_a[0] - as_b[0])
    # typeToken = abs(as_a[1] - as_b[1])
    # legomana = abs(as_a[2] - as_b[2])
    # medSent = abs(as_a[3] - as_b[3])
    # complex = abs(as_a[4] - as_b[4])
    # medFrase = abs(as_a[5] - as_b[5])
    # soma = tamMed + typeToken + legomana + medSent + complex + medFrase
    SAB = soma / 6
    return SAB

#funciona
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []
    caracteres = 0
    tam_sentenca = 0
    tam_frase = 0

    #preparando as listas
    lista_sentencas = separa_sentencas(texto)

    for sent in lista_sentencas:
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)#cria uma lista de frases

    for frase in lista_frases:
        novas_palavras = separa_palavras(frase)
        lista_palavras.extend(novas_palavras)#cria uma  lista de palavras

    #cálculo dos parametros da assinatura
    #tamanho médio de palavra
    for palavra in lista_palavras:
        caracteres = caracteres + len(palavra)
    wal_texto = caracteres / len(lista_palavras)    

    #relação type token
    num_diferentes = n_palavras_diferentes(lista_palavras)
    ttr_texto = num_diferentes / len(lista_palavras)

    #razão hapax legomana
    num_unicas = n_palavras_unicas(lista_palavras)
    hlr = num_unicas / len(lista_palavras)

    #tamanho medio da sentença
    for sentenca in lista_sentencas:
        tam_sentenca = tam_sentenca + len(sentenca)
    sal_texto = tam_sentenca / len(lista_sentencas)

    #complexidade da sentença
    sac_texto = len(lista_frases) / len(lista_sentencas)

    #tamanho médio de frase
    for frase in lista_frases:
        tam_frase = tam_frase + len(frase)
    pal_texto = tam_frase / len(lista_frases)

    return ([wal_texto, ttr_texto, hlr, sal_texto, sac_texto, pal_texto])

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_assinaturas = []
    lista_similaridades = []
    for texto in textos:
        lista_assinaturas.append(calcula_assinatura(texto)) #recebemos uma lista com todas as assinaturas(listas)    
    for assinatura in  lista_assinaturas:
        similaridade = compara_assinatura(assinatura, ass_cp)
        lista_similaridades.append(similaridade) #comparando as assinaturas e salvando em uma lista os valores
    
    minimo = min(lista_similaridades)
    posicao = lista_similaridades.index(minimo)

    return posicao + 1

def main():
    as_b = []
    as_b =  le_assinatura()
    
    # # executa a função LE TEXTOS
    textos = []
    textos = le_textos()

    cohpiah = avalia_textos(textos, as_b)
    print("O autor do texto", cohpiah, "está infectado com COH-PIAH")
main()    