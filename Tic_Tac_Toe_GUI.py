import tkinter as tk
import tkinter.font as font
import random

trials = 0
player = 0
win = 0

def enter_XO_computer():
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
                enter_XO_computer()
        else:
            def put_x_check_win():
                global player
                field[ran_num]["text"] = "X"
                check_win()
                player = 0
            lbl_info.after(500, put_x_check_win)
            
            
        
def play_computer_vs_player():
    global player
    global trials
    global win
    if win == 0:
        lbl_info["text"] = "Now is playing computer!"
        enter_XO_computer()
        trials += 1
        def txt_playing_you():
            if win == 0:
                lbl_info["text"] = "Now you are playing!" 
        lbl_info.after(1000, txt_playing_you )
    

def btn_0_click():
    global trials
    global player
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_0['text'] == "O" or btn_0['text'] == "X" :
        lbl_info["text"] = "This field is occupied!" 
    else:
        btn_0['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
            
def btn_1_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_1['text'] == "O" or btn_1['text'] == "X" :
        lbl_info["text"] = "This field is occupied!" 
    else:
        btn_1['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
            
def btn_2_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_2['text'] == "O" or btn_2['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    else:
        btn_2['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
        
def btn_3_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_3['text'] == "O" or btn_3['text'] == "X" :
        lbl_info["text"] = "This field is occupied!" 
    else:
        btn_3['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
        
def btn_4_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_4['text'] == "O" or btn_4['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    else:
        btn_4['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
        
def btn_5_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_5['text'] == "O" or btn_5['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    else:
        btn_5['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 
        
def btn_6_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_6['text'] == "O" or btn_6['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    else:
        btn_6['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 

def btn_7_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_7['text'] == "O" or btn_7['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"  
    else:
        btn_7['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 

def btn_8_click():
    global player
    global trials
    if win == 1:
        lbl_info["text"] = "Click the reset button!"
    elif btn_8['text'] == "O" or btn_8['text'] == "X" :
        lbl_info["text"] = "This field is occupied!"
    else:
        btn_8['text'] = "O"
        check_win()
        trials += 1
        player = 1
        play_computer_vs_player() 

def win_function(player_sign):
    global win
    lbl_info["text"] = "The " + player_sign + " wins!" 
    win += 1         
        
def check_win():
    global win
    global trials
    if player == 0:
            player_sign = "player"
    elif player == 1:
            player_sign = "computer"
    if (btn_0["text"] == "O" and btn_1["text"] == "O" and btn_2["text"] == "O") or (btn_0["text"] == "X" and btn_1["text"] == "X" and btn_2["text"] == "X") : 
            win_function(player_sign)
    elif (btn_3["text"] == "O" and btn_4["text"] == "O" and btn_5["text"] == "O") or (btn_3["text"] == "X" and btn_4["text"] == "X" and btn_5["text"] == "X") : 
            win_function(player_sign)
    elif (btn_6["text"] == "O" and btn_7["text"] == "O" and btn_8["text"] == "O") or (btn_6["text"] == "X" and btn_7["text"] == "X" and btn_8["text"] == "X") : 
            win_function(player_sign)
    elif (btn_0["text"] == "O" and btn_3["text"] == "O" and btn_6["text"] == "O") or (btn_0["text"] == "X" and btn_3["text"] == "X" and btn_6["text"] == "X") : 
            win_function(player_sign)
    elif (btn_1["text"] == "O" and btn_4["text"] == "O" and btn_7["text"] == "O") or (btn_1["text"] == "X" and btn_4["text"] == "X" and btn_7["text"] == "X") : 
            win_function(player_sign)
    elif (btn_2["text"] == "O" and btn_5["text"] == "O" and btn_8["text"] == "O") or (btn_2["text"] == "X" and btn_5["text"] == "X" and btn_8["text"] == "X") : 
            win_function(player_sign)
    elif (btn_0["text"] == "O" and btn_4["text"] == "O" and btn_8["text"] == "O") or (btn_0["text"] == "X" and btn_4["text"] == "X" and btn_8["text"] == "X") : 
            win_function(player_sign)
    elif (btn_2["text"] == "O" and btn_4["text"] == "O" and btn_6["text"] == "O") or (btn_2["text"] == "X" and btn_4["text"] == "X" and btn_6["text"] == "X") : 
            win_function(player_sign)
    elif trials == 9:
        lbl_info["DRAW!"]
        win += 1
def reset_game():
    global trials
    global player
    global win
    btn_0["text"] = ""
    btn_1["text"] = ""
    btn_2["text"] = ""
    btn_3["text"] = ""
    btn_4["text"] = ""
    btn_5["text"] = ""
    btn_6["text"] = ""
    btn_7["text"] = ""
    btn_8["text"] = ""
    lbl_info["text"] = "Welcome in The Tic Tac Toe!\nYou are O, computer is X\nChoose field!"
    trials = 0
    player = 0
    win = 0

#windows
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
window.rowconfigure([0,1], minsize=50, weight=0)
window.columnconfigure([0], minsize=100, weight=1)
window.rowconfigure(2, minsize=100, weight=1)

#text who plays
frm_up = tk.Frame(master=window)
frm_up.grid(row=0, column=0)

lbl_info = tk.Label(master=frm_up, text="Welcome in The Tic Tac Toe!\nYou are O, computer is X\nChoose field!")
lbl_info.grid(row=0, column=0)


#reset button
btn_reset = tk.Button(master=window, text="Reset", command=reset_game)
btn_reset.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#frame board
frm_board = tk.Frame(master=window)
frm_board.grid(row=2, column=0, padx=10, pady=10)

frm_board.rowconfigure([0,1,2], minsize=100, weight=0)
frm_board.columnconfigure([0,1,2], minsize=100, weight=0)

myFont = font.Font(size=40)

btn_0 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_0_click)
btn_0.grid(row=0 , column=0, sticky="nsew")
btn_1 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_1_click)
btn_1.grid(row=0 , column=1, sticky="nsew")
btn_2 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_2_click)
btn_2.grid(row=0 , column=2, sticky="nsew")

#row2
btn_3 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_3_click)
btn_3.grid(row=1 , column=0, sticky="nsew")
btn_4 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_4_click)
btn_4.grid(row=1 , column=1, sticky="nsew")
btn_5 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_5_click)
btn_5.grid(row=1 , column=2, sticky="nsew")

#row3
btn_6 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_6_click)
btn_6.grid(row=2 , column=0, sticky="nsew")
btn_7 = tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_7_click)
btn_7.grid(row=2 , column=1, sticky="nsew")
btn_8= tk.Button(master=frm_board, text="", relief=tk.GROOVE, border=2, font=myFont, command=btn_8_click)
btn_8.grid(row=2 , column=2, sticky="nsew")

window.mainloop()



