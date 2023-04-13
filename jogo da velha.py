
def menu():
    continuar = 1
    while continuar:
        continuar = int(input("0. Exit \n" 
                              "1. Begin game\n"))
        if continuar:
            jogo()
        else:
            break


def jogo():
    jogada = 0

    while pontuacao() == 0:
        print("\nJogador ", jogada % 2 + 1) #determinar o ordem dos usuários, ela começa do 0 por isso acrescenta o +1
        tabela()
        linha = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if board[linha - 1][coluna - 1] == 0: #verifica a posição escolhida pelo usuário
            if (jogada % 2 + 1) == 1:
                board[linha - 1][coluna - 1] = 1
            else:
                board[linha - 1][coluna - 1] = -1
        else:
            print("Esta posição já foi escolhida, por favor escolha novamente")
            jogada -= 1

        if pontuacao():
            print("Parabéns Jogador ", jogada % 2 + 1, " ganhou !!!!!")

        jogada += 1



def pontuacao():
    # checando as linhas
    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]
        if soma == 3 or soma == -3:
            return 1

    # checando as colunas
    for i in range(3):
        soma = board[0][i] + board[1][i] + board[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checando as diagonais
    diagonal_1 = board[0][0] + board[1][1] + board[2][2]
    diagonal_2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal_1 == 3 or diagonal_1 == -3 or diagonal_2 == 3 or diagonal_2 == -3:
        return 1

    return 0


def tabela():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

menu()

