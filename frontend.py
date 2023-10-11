import tkinter as tk
import tkinter.font as font
import time
import random

trials = 0
player = 0 # 0 to O, 1 to X
computer_on = 0

def enter_XO_computer():
        while True:
            time.sleep(2)
            field = {
                0: btn_0,
                1: btn_1,
                2: btn_2,
                3: btn_3,
                4: btn_4,
                5: btn_5,
                6: btn_6, 
                7: btn_7,
                8: btn_8,
            }
            ran_num = random.randint(0,8)
            if field[ran_num]['text'] == "O" or field[ran_num]['text'] == "X" :
                    continue
            field[ran_num]["text"] = "X"
            return ran_num
def play_computer_and_player(trials, player):
    while True:
        if trials < 10:
            if player == 0:
                lbl_info["text"] = "Now is playing computer!"
                time.sleep(1)
                enter_XO_computer()
                #sprawdzic rezultat
                player = 1
                trials += 1
            elif player == 1:
                lbl_info["text"] = "Now you are playing!"
                time.sleep(1)
            

def play_with_computer_game():
    lbl_info["text"] = "The Computer places an O\nYou place an X"
    time.sleep(2)
    global trials
    global player
    global computer_on
    computer_on = 1
    play_computer_and_player(trials, player)
    
                
def play_game():
    pass  


def  play_versus_player():
    pass

def btn_1_click():
    
    if btn_1['text'] == "O" or btn_1['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    if trials < 10:
        if player == 0:
            btn_1['text'] == "O"
            trials += 1
            player = 1
        elif player == 1:
            btn_1['text'] == "X"
            trials += 1
            player = 0
    #zrób tylko z komputerem wedlug twojego wzoru 
        
            




#windows
window = tk.Tk()
window.resizable(False, False)
window.rowconfigure([0,1], minsize=50, weight=0)
window.columnconfigure([0], minsize=100, weight=1)
window.rowconfigure(3, minsize=100, weight=1)

#text who plays
frm_up = tk.Frame(master=window)
frm_up.grid(row=0, column=0)

lbl_info = tk.Label(master=frm_up, text="Welcome in The Tic Tac Toe!\nChoose with who You want to play!")
lbl_info.grid(row=0, column=0)


#buttons play vs
frm_versus = tk.Frame(master=window)
frm_versus.grid(row=1, column=0)
frm_versus.columnconfigure([0,1], minsize=160)

btn_computer = tk.Button(master=frm_versus, text="Computer", command=play_with_computer_game)
btn_computer.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

btn_versus_player = tk.Button(master=frm_versus, text="Vs Player")
btn_versus_player.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

#reset button
btn_reset = tk.Button(master=window, text="Reset")
btn_reset.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

#frame board
frm_board = tk.Frame(master=window)
frm_board.grid(row=3, column=0, padx=10, pady=10)

frm_board.rowconfigure([0,1,2], minsize=100, weight=0)
frm_board.columnconfigure([0,1,2], minsize=100, weight=0)

myFont = font.Font(size=40)

btn_0 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_0.grid(row=0 , column=0, sticky="nsew")
btn_1 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_1_click)
btn_1.grid(row=0 , column=1, sticky="nsew")
btn_2 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_2.grid(row=0 , column=2, sticky="nsew")

#row2
btn_3 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_3.grid(row=1 , column=0, sticky="nsew")
btn_4 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_4.grid(row=1 , column=1, sticky="nsew")
btn_5 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_5.grid(row=1 , column=2, sticky="nsew")

#row3
btn_6 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_6.grid(row=2 , column=0, sticky="nsew")
btn_7 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_7.grid(row=2 , column=1, sticky="nsew")
btn_8= tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont)
btn_8.grid(row=2 , column=2, sticky="nsew")

window.mainloop()



