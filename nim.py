def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")#quebrar uma linha
    if n % (m + 1) == 0:
        #usuário começa
        print("Você começa!")
        print("")
        while(n > 0):
            qtd = usuario_escolhe_jogada(n, m)
            n = n - qtd #n = número de peças restantes
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "user"
                
            else:
                qtd = computador_escolhe_jogada(n, m)
                n = n - qtd
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                    return "pc"

    else: 
        #computador começa
        print("Computador começa!")
        print("")
        while(n > 0):
            qtd = computador_escolhe_jogada(n, m)
            n = n - qtd
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "pc"
                
            else:
                qtd = usuario_escolhe_jogada(n, m)
                n = n - qtd
                if(n == 0):
                    print("Fim do jogo! Você ganhou!")
                    return "user"

def campeonato():
    pc = 0
    user = 0
    rodada = 1
    while rodada <= 3:
        print("")
        print("**** Rodada", rodada, "****")
        print("")
        rodada = rodada + 1
        winner = partida()
        if winner == "user":
            user = user + 1
        else:
            pc = pc + 1

    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", user, "X", pc, "Computador")

def computador_escolhe_jogada(n, m):
    if(m > n):
        m = n

    qtd = m
    while (n - qtd) % (m + 1) != 0 and qtd > 0:
        qtd = qtd - 1

    if qtd == 0:
        qtd = m

    if qtd == 1:
        print("O computador tirou uma peça")

    else:
        print("O computador tirou", qtd, "peças")

    if (n - qtd) == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
        print("")
    else:
        if (n - qtd) != 0:
            print("Agora restam", n - qtd, "peças no tabuleiro.")
            print("")

    return qtd           

def usuario_escolhe_jogada(n, m): 
    qtd = int(input("Quantas peças você vai tirar? "))
    while qtd > n or qtd > m or qtd <= 0:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        qtd = int(input("Quantas peças você vai tirar? "))

    print("")
    if(qtd > 1):
        print("Você tirou", qtd, "peças")
    else:
        print("Você tirou uma peça.")

    if (n - qtd) == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
        print("")
    else:
        if (n - qtd) != 0:
            print("Agora restam", n - qtd, "peças no tabuleiro.")
            print("") 

    return qtd #qtd = número de peças retiradas do tabuleiro

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar um campeonato")
    print("2 - para jogar uma partida isolada")
    opc = int(input("Opção: "))
    
    while opc != 1 and opc != 2:
        print("Por favor, digite uma opção válida!")
        opc = int(input("Opção: "))

    if opc == 1:
        print("Voce escolheu um campeonato!")
        campeonato() #chama a função campeonato
    else:
        print("Voce escolheu uma partida isolada!")
        partida()
main()