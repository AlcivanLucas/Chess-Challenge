from funcoes import *
import random

Heuristic = bool(random.getrandbits(1))
count = 0
board = chess.Board() # cria um novo tabuleiro la no terminal
print("Bem vindo ao Xadrez!")
playerColor = bool(int(input("Escolha a cor: Branco(1) ou preto(0)? ")))
print(board)
##board 
while not gameOver(board):
    if board.turn == playerColor: #So paa determinar quem vai jogar primeiro 
        print(board.legal_moves) # mostra quais jogadas são possiveis ser realizadas
        move = input("Coloque sua jogada: ")
        verifyPlayerMove(move,board) # verifica se a jogada é valida
        print(board) # depois da jogada 
        ##board
    else: #Desativa a heurística
        if Heuristic:
            italianGame(board,count)
            count += 1
            Heuristic = False if count > 2 else True
        else:
            print("Jogada da IA:")
            move = minimaxRoot(6,board,True)
            move = chess.Move.from_uci(str(move))# Converte a jogada resultante do minimax para o formato adequado e a aplica ao tabuleiro
            board.push(move)
        clearConsole()
        print(board)
        ##board
        #fim do loop
print("Xeque mate")