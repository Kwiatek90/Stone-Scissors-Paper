#Stone_scissor_paper
#W oby przypadkach musi być również możliwość gry z komputerem.

#W przypadku 1️⃣, jest to trywialne, bo to tylko loswanie jednego z 3 elementów
#W przypadku 2️⃣, zrób to najprościej jak się da i po prostu losuj co się pojawi na 
#dowolnym polu, nie staraj się teraz tworzyć, algorytmu "myślenia" analizującego planszę.

#   [00] , [01], [02]
#   [10], [11], [12]
#   [20], [21], [22]


#tworzyc wygrane
#dodac komputer



def show_board(board):
        for i in range(3):
                print("\t")
                for j in range(3):
                        print(board[i][j], end="\t")
                print("\t")
        
                


def result_option(board, player):
        if player == 0:
                player = "X"
        elif player == 1:
                player = "O"
        
        
        if (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") : 
                print(f"Win player {player}") 
                exit()   
        elif (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") : 
                print(f"Win player {player}") 
                exit()
        elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") : 
                print(f"Win player {player}") 
                exit()
                

def enter_XO(board,player):
        while True:
                print(f"Now playing player {player}")
                column = input("Enter column(1-3): ")
                line = input("Enter line(1-3): ")
                if line == "Exit" or column == "Exit":
                        break
                line = int(line) - 1
                column = int(column) - 1
                if board[line][column] == "O":
                        print("Pole jest zajęte")
                        continue
                elif board[line][column] == "X":
                        print("Pole jest zajęte")
                        continue
                return line, column
        

def play(board):
        player = 0
        proba = 0
        while True:
                if proba < 10:
                        if player == 0:
                                line, column = enter_XO(board, player)
                                board[line][column] = "X"
                                show_board(board)
                                result_option(board, player)
                                player = 1
                                proba += 1
                        elif player == 1:
                                line, column = enter_XO(board, player)
                                board[line][column] = "O"
                                show_board(board)
                                result_option(board, player)
                                player = 0
                                proba += 1
                else:
                        print("REMIS")

        
        



board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

play(board)


