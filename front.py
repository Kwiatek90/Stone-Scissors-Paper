import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.rowconfigure([0,1], minsize=50, weight=0)
window.columnconfigure([0], minsize=100, weight=1)
window.rowconfigure(2, minsize=100, weight=1)

#text who plays
frm_up = tk.Frame(master=window)
frm_up.grid(row=0, column=0)

lbl_player = tk.Label(master=frm_up, text="Play the game!")
lbl_player.grid(row=0, column=0)

btn_reset = tk.Button(master=window, text="Reset")
btn_reset.grid(row=1, column=0)

#frame board
frm_board = tk.Frame(master=window)
frm_board.grid(row=2, column=0, padx=10, pady=10)

frm_board.rowconfigure([0,1,2], minsize=100, weight=0)
frm_board.columnconfigure([0,1,2], minsize=100, weight=0)
#pola

#row 1
btn_00 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_00.grid(row=0 , column=0, sticky="nsew")
btn_01 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_01.grid(row=0 , column=1, sticky="nsew")
btn_02 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_02.grid(row=0 , column=2, sticky="nsew")

#row2
btn_10 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_10.grid(row=1 , column=0, sticky="nsew")
btn_11 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_11.grid(row=1 , column=1, sticky="nsew")
btn_12 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_12.grid(row=1 , column=2, sticky="nsew")

#row3
btn_20 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_20.grid(row=2 , column=0, sticky="nsew")
btn_21 = tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_21.grid(row=2 , column=1, sticky="nsew")
btn_22= tk.Button(master=frm_board, text="X", relief=tk.GROOVE, border=2)
btn_22.grid(row=2 , column=2, sticky="nsew")


window.mainloop()



