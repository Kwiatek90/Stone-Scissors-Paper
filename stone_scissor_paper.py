#Stone_scissor_paper
#W oby przypadkach musi być również możliwość gry z komputerem.

#W przypadku 1️⃣, jest to trywialne, bo to tylko loswanie jednego z 3 elementów
#W przypadku 2️⃣, zrób to najprościej jak się da i po prostu losuj co się pojawi na 
#dowolnym polu, nie staraj się teraz tworzyć, algorytmu "myślenia" analizującego planszę.

#   [11] , [12], [13]
#   [21], [22], [23]
#   [31], [32], [33]

#wyswietlic tablice
#dodawac wartosc
#tworzyc wygrane
#dodac komputer


def show_board(board):
        for i in range(3):
                print("\t")
                for j in range(3):
                        print(board[i][j], end="\t")
                
        
        



board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]


while True:
        column = input("Enter column(1-3): ")
        line = input("Enter line(1-3): ")
        if line == "Exit" or column == "Exit":
                break
        line = int(line) - 1
        column = int(column) - 1
        board[line][column] = "X"
        show_board(board)


