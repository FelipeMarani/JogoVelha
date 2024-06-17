partida = 0
jogada = 1
VtX = 0
VtO = 0
VitoriaX = 0
VitoriaO = 0
Empate = 0
Qpe = 0
Jogar = "SIM"
while True:
    if Jogar == "SIM":
        tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        while True:
            while VtO <= 0 and VtX <= 0 and Empate <= 0:
                if jogada % 2 == 1:
                    while jogada % 2 == 1 :
                        print("O Jogador X ira começar:")
                        Linha = int(input("Escolha a Linha(0, 1, 2) ao qual ira jogar: "))
                        Coluna = int(input("Agora escolha a Coluna(0, 1, 2) que deseja marcar: "))
                        if tabuleiro[Linha][Coluna] == " ":
                            tabuleiro[Linha][Coluna] = "X"
                            jogada += 1
                            # Verificação de Valores
                            if tabuleiro[0][0]=="X" and tabuleiro[0][1]=="X" and tabuleiro[0][2] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[1][0]=="X" and tabuleiro[1][1]=="X" and tabuleiro[1][2] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break    
                            elif tabuleiro[2][0]=="X" and tabuleiro[2][1]=="X" and tabuleiro[2][2] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[0][0]=="X" and tabuleiro[1][1]=="X" and tabuleiro[2][2] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[0][2]=="X" and tabuleiro[1][1]=="X" and tabuleiro[2][0]== "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[0][0]=="X"and tabuleiro[1][0]=="X" and tabuleiro[2][0] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[0][1]=="X"and tabuleiro[1][1]=="X" and tabuleiro[2][1] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                            elif tabuleiro[0][2]=="X"and tabuleiro[1][2]=="X" and tabuleiro[2][2] == "X":
                                print("O jogador X Venceu")
                                VtX += 1
                                break
                        else:
                            print("Posição Inválida, já esta ocupada!!")
                            print("Tente novamente!")
                            jogada -= 1
                            continue
                        
                elif jogada % 2 == 0 :
                    while jogada % 2 == 0:
                        print("O Jogador O ira começar:")
                        Linha = int(input("Escolha a Linha(0, 1, 2) ao qual ira jogar: "))
                        Coluna = int(input("Agora escolha a Coluna(0, 1, 2) que deseja marcar: "))
                        if tabuleiro[Linha][Coluna] == " ":
                            tabuleiro[Linha][Coluna] = "O"
                            jogada += 1
                            if tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break    
                            elif tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[0][0] == "O"and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[0][1] == "O"and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                            elif tabuleiro[0][2] == "O"and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O":
                                print("O jogador O Venceu")
                                VtO += 1
                                break
                        else:
                            print("Posição Inválida, já esta ocupada!!")
                            print("Tente Novamente!")
                            continue
                        
                elif jogada == 10:
                    print("Empate entre o jogadores!")
                    Empate += 1

            VitoriaX += VtX
            VitoriaO += VtO
            Qpe += Empate

            if VtX > 0 or VtO > 0 or Empate > 0:
                partida += 1
                print("Vitórias do Jogador X: {}".format(VitoriaX))
                VtX -= 1
                print("Vitórias do Jogador O: {}".format(VitoriaO))
                VtO -= 1
                print("Número de empates: {}".format(Qpe))
                print("Partida de número {}°".format(partida))
                novamente = str(input("Deseja jogar novamente?(Sim ou Não): ")).upper()
                if novamente[0] == "S":
                    continue
                elif novamente[0] == "N":
                  Jogar = "NÃO"
                  break
    elif Jogar == "NÃO":
        print("Obrigado pela(s) partida(s), e até breve!!")
        break
                