import random
import time
import os

#display the board
def show_board(board):
        for i in range(3):
                print("\t")
                for j in range(3):
                        print(board[i][j], end="\t")
                print("\t")

#check the board if there is a win
def result_option(board, player):
        if player == 0:
                player = "X"
        elif player == 1:
                player = "O"
        if (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") : 
                print(f"The player {player} wins!") 
                exit()   
        elif (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") : 
                print(f"The player {player} wins!") 
                exit()
        elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") : 
                print(f"The player {player} wins!") 
                exit()
                
#function which you can put the XO in game 1 vs 1 and check if the field is occupied
def enter_XO(board,player):
        while True:
                if player == 0:
                        player = "X"
                elif player == 1:
                        player = "O"
                print(f"Now playing player {player}")
                column = input("Enter column(1-3): ")
                if column == "1" or column == "2" or column == "3":
                        True
                else:
                        print("You entered the wrong number! Try again")
                        continue
                line = input("Enter line(1-3): ")
                if line == "1" or line == "2" or line == "3":
                        True
                else:
                        print("You entered the wrong number! Try again")
                        continue
                line = int(line) - 1
                column = int(column) - 1
                if board[line][column] == "O":
                        print("The field is occupied")
                        continue
                elif board[line][column] == "X":
                        print("The field is occupied")
                        continue
                return line, column
        
#function which you can put the XO in game vs computer and check if the field is occupied    
def enter_XO_computer(board):
        while True:
                print(f"Now the computer plays by typing the X character ...")
                time.sleep(2)
                column = random.randint(0,2)
                line = random.randint(0,2)
                if board[line][column] == "O":
                        print("The field is occupied")
                        continue
                elif board[line][column] == "X":
                        print("The field is occupied")
                        continue
                return line, column

def play_vs_game(player,board,trials):
        while True:
                        if trials < 10:
                                if player == 0:
                                        line, column = enter_XO(board, player)
                                        board[line][column] = "X"
                                        show_board(board)
                                        result_option(board, player)
                                        player = 1
                                        trials += 1
                                elif player == 1:
                                        line, column = enter_XO(board, player)
                                        board[line][column] = "O"
                                        show_board(board)
                                        result_option(board, player)
                                        player = 0
                                        trials += 1
                        else:
                                print("Draw")

def play_with_computer_game(player, board, trials):
        while True:
                        if trials < 10:
                                if player == 0:
                                        line, column = enter_XO_computer(board)
                                        board[line][column] = "X"
                                        os.system('cls')
                                        show_board(board)
                                        result_option(board, player)
                                        player = 1
                                        trials += 1
                                        
                                elif player == 1:
                                        line, column = enter_XO(board, player)
                                        board[line][column] = "O"
                                        os.system('cls')
                                        show_board(board)
                                        result_option(board, player)
                                        player = 0
                                        trials += 1
                                        
                        else:
                                print("Draw") 
#main function
def play(board):
        os.system('cls')
        while True:
                player = 0
                trials = 0
                print("Hello, you're playling the stone, scissor, paper game!")
                time.sleep(1)
                choose_game = input("Do you want to play with 'computer'( Enter 1) or 1 vs 1(Enter 2)?")
                if choose_game == "1" or choose_game == "2":
                                True
                else:
                        print("You entered the wrong number! Try again")
                        continue
                if choose_game == "1":
                        play_with_computer_game(player,board,trials)  
                elif choose_game == "2":
                        play_vs_game(player,board,trials)
        
        



board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

play(board)

