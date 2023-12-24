'''
gui.py
===============================================
gui.py contains the  graphical user interface
uses tkinter as the engine
connects the game data to the interface on the screen
'''
import tkinter
from tkinter import *
from functools import partial
import tkinter.font as font

from pygame import mixer
import os

import game
import alphaBetaPruning

#rules screen
def rules(root):
    root.destroy()
    root=Tk()
    root.geometry("1920x1080")
    root.config(bg='black')
    root.title("Maxit")
    #background
    C = Canvas(root, bg="blue", height=1080, width=1920)
    path=getBgPath()
    filename = PhotoImage(file=path)
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create text widget and specify size.
    T = Text(root, height=10, width=72, bg='black',fg='lime')
    T.config(font=("Terminal",29))
    T.tag_config("tag_name", justify='center')
    Fact = "Each cell in a game board of 8*8 cells contains a number.\nThe players take turns selecting numbers from the game board.\nThese numbers are added to the players cumulative score.\nThe player selects any number along a horizontal row that is on.\nThe number at that location gets added to your score,\n and removed from the board.\nThe computer then selects a number from the game board.\nThe computer can only select numbers along the vertical columns.\nPlay continues in this fashion until there is no move available.\nThe object of the game is to have the highest score when the game ends."

    # Create label
    l = Label(root, text="Rules Of Maxit", bg='black',fg='lime')
    l.config(font=("Terminal", 50))
    headlinefont = font.Font(family='Terminal', size=40)
    myfont = font.Font(family='Terminal', size=30)

    #buttons
    fun = partial(out, root)
    B1 = Button(root, text="Return To Main Menu", command=fun,
                activeforeground='black',
                activebackground="lime", bg="black",
                fg="lime", width=20, font=myfont, bd=15)
    head = Button(root, text="The MAXIT Game!",
                  activeforeground='black',
                  activebackground="lime", bg="black",
                  fg="lime", width=90, font=headlinefont, bd=20, state=DISABLED)

    head.pack()
    l.pack()
    T.pack()
    B1.pack(side='top')
    C.pack()

    # Insert The Fact.
    T.insert(tkinter.END, Fact)
    T.tag_add("tag_name", "1.0", "end")
    root.mainloop()

#when return back to menu is clicked
def out(root):
    root.destroy()
    play()

#finds filepath of file in the same directory
def findPath(str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, str)
    return file_path

#start music and game
def start():
    mixer.init()
    file_path =findPath("music.mp3")
    mixer.music.load(file_path)
    mixer.music.play(loops=-1)
    play()

def getBgPath():
    path = findPath('bg.png')
    return path
#main meu
def play():
    menu = Tk()
    menu.geometry("1920x1080")
    menu.title("Maxit")
    menu.config(bg='black')
    C = Canvas(menu, bg="blue", height=1080, width=1920)
    path=getBgPath()
    filename = PhotoImage(file=path)
    background_label = Label(menu, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    wpc = partial(withpc, menu)
    wrl = partial(rules, menu)
    myfont= font.Font(family='Terminal', size=40)
    headlinefont=font.Font(family='Terminal', size=60)

    head = Button(menu, text="The MAXIT Game!",
                  activeforeground='black',
                  activebackground="lime", bg="black",
                  fg="lime", width=40, font=headlinefont, bd = 40)

    B1 = Button(menu, text="Start", command=wpc,
                activeforeground='black',
                activebackground="lime", bg="black",
                fg="lime", width=10, font=myfont, bd=10)

    B3 = Button(menu, text="Rules", command=wrl, activeforeground='black',
                activebackground="lime", bg="black", fg="lime",
                width=10, font=myfont, bd=10)

    B4 = Button(menu, text="Exit", command=exitprogram, activeforeground='black',
                activebackground="lime", bg="black", fg="lime",
                width=10, font=myfont, bd=10)

    head.pack(side='top')
    B1.pack(side='top')
    B3.pack(side='top')
    B4.pack(side='top')
    C.pack()
    menu.mainloop()

def exitprogram():
    exit()

#when start game is clicked
def withpc(root):
    root.destroy()
    select_diff(root)

# Initialize the game window
def defwindow(root):
    root.destroy()
    game_board = Tk()
    game_board.title("Maxit Game")
    game_board.geometry("1920x1080")
    game_board.config(bg='black')
    gameboard_pc(game_board)

#select difficulty screen
def select_diff(menu):
    menu = Tk()
    menu.geometry("1920x1080")
    menu.title("Maxit")
    menu.config(bg='black')

    C = Canvas(menu, bg="blue", height=1080, width=1920)
    path=getBgPath()
    filename = PhotoImage(file=path)
    background_label = Label(menu, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    wpc = partial(withpc, menu)
    wrl = partial(rules, menu)
    myfont = font.Font(family='Terminal', size=40)

    head = Button(menu, text="The MAXIT Game!",
                  activeforeground='black',
                  activebackground="lime", bg="black",
                  fg="lime", width=90, font=myfont, bd=20, state=DISABLED)

    l = Label(menu, text="Select Difficulty", bg='black', fg='lime')
    l.config(font=("Terminal", 50))

    set1=partial(seteasy, menu)
    set2 = partial(setmedium, menu)
    set3 = partial(sethard, menu)
    B1 = Button(menu, text="Easy", command=set1,
                activeforeground='black',
                activebackground="lime", bg="black",
                fg="lime", width=10, font=myfont, bd=10)

    B2 = Button(menu, text="Medium", command=set2, activeforeground='black',
                activebackground="lime", bg="black", fg="lime",
                width=10, font=myfont, bd=10)

    B3 = Button(menu, text="Hard", command=set3, activeforeground='black',
                activebackground="lime", bg="black", fg="lime",
                width=10, font=myfont, bd=10)

    fun = partial(out, menu)
    B4 = Button(menu, text="Return To Main Menu", command=fun,
                activeforeground='black',
                activebackground="lime", bg="black",
                fg="lime", width=20, font=myfont, bd=15)
    B4.config(font=("Terminal", 25))
    head.pack(side='top')
    l.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    B4.pack(side='top')
    C.pack()
    menu.mainloop()

#set depth of AI
def seteasy(root):
    alphaBetaPruning.DEPTH=1
    defwindow(root)
def setmedium(root):
    alphaBetaPruning.DEPTH=2
    defwindow(root)
def sethard(root):
    alphaBetaPruning.DEPTH=8
    defwindow(root)

def gameboard_pc(game_board):
    C = Canvas(game_board, bg="blue", height=1080, width=1920)
    path=getBgPath()
    filename = PhotoImage(file=path)
    background_label = Label(game_board, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    global board
    board = game.create()
    button = []
    myfont = font.Font(family='Terminal',size=34) #22
    smallfont = font.Font(family='Terminal',size=34)
    bigfont= font.Font(family='Terminal',size=34)
    hugefont = font.Font(family='Terminal', size=130)
    retfun=partial(out, game_board)

    l1 = Label(game_board, text="Your Score:", bg='black', fg='cyan', font=bigfont)
    l2 = Label(game_board, text="AI Score:", bg='black', fg='red', font=bigfont)
    l3 = Label(game_board, text="0", bg='black', fg='cyan', font=hugefont)
    l4 = Label(game_board, text="0", bg='black', fg='red', font=hugefont)
    rtm = Button(game_board, bd=10, height=1, width=26, state=NORMAL, font=smallfont, bg='black', fg='lime',
                     text="Return To Menu",command=retfun)

    rtm.grid(row=8, column=8, rowspan=1)
    l1.grid(row=9, column=8, rowspan=1)
    l2.grid(row=13, column=8, rowspan=1)
    l3.grid(row=9, column=8, rowspan=3)
    l4.grid(row=13, column=8, rowspan=3)
    scores = [l3, l4]

    for a in range(8):
        m = 8 + a
        button.append(a)
        button[a] = []
        for b in range(8):
            get_t = partial(clicked, a, b, game_board, button, scores)
            n = b
            button[a].append(b)
            button[a][b] = Button(game_board,text=board[a][b], bd=5, height=2, width=4, state=DISABLED,command=get_t,font=myfont, bg='black', fg='lime')
            button[a][b].grid(row=m, column=n)
    open_row(button)
    game_board.mainloop()

#Activates buttons
def open_row(button):
    row_number = game.lastTurn(board)
    for i in range(8):
        if board[row_number][i] != 99:
            button[row_number][i].config(state=NORMAL)

#Screen of the results of the game
def resultScreen(root):
        root.destroy()
        # specify size of window.
        root = Tk()
        root.geometry("1920x1080")
        root.config(bg='black')
        root.title("Maxit")
        C = Canvas(root, bg="blue", height=1080, width=1920)
        path=getBgPath()
        filename = PhotoImage(file=path)
        background_label = Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        fun = partial(out, root)
        # Create label
        l = Label(root, bg='black', fg='lime')
        l.config(font=("Terminal", 35))
        l2 = Label(root, bg='black', fg='lime')
        l2.config(font=("Terminal", 35))
        lbig=Label(root, bg='black')

        if game.CompScore(board) > game.HumScore(board):
            msg = "Your score was " + str(game.HumScore(board)) + "!"
            msg2 = "The AI algorithm won the match with a score of " + str(game.CompScore(board)) + "!"

            lbig.config(font=("Terminal", 140), fg='red')
            lbig.config(text="You Lost!")
            l.config(text=msg)
            l2.config(text=msg2)
        elif game.CompScore(board) == game.HumScore(board):
            lbig.config(font=("Terminal", 140), fg='white')
            msg = "You made a draw with a score of " + str(game.CompScore(board)) + "!"
            lbig.config(text="A Tie!")
            l.config(text=msg)
        else:
            lbig.config(font=("Terminal", 140), fg='cyan')
            msg = "Your score was " + str(game.HumScore(board)) + "!"
            msg2 = "The AI algorithm lost with a score of " + str(game.CompScore(board)) + "!"
            lbig.config(text="You Won!")
            l.config(text=msg)
            l2.config(text=msg2)
        B1 = Button(root, text="Return To Main Menu", command=fun,
                    activeforeground='black',
                    activebackground="lime", bg="black",
                    fg="lime", width=20, bd=15)
        B1.config(font=("Terminal", 50))

        head = Button(root, text="The MAXIT Game!",
                      activeforeground='black',
                      activebackground="lime", bg="black",
                      fg="lime", width=90, bd=20, state=DISABLED)
        head.config(font=("Terminal", 50))
        head.pack()
        lbig.pack()
        l.pack()
        l2.pack()
        B1.pack()
        C.pack()
        root.mainloop()

#when a button is clicked:
def clicked(row, col, game_board, button, scores):
    global board
    number = col  # col number
    if (game.inputMove(board, number) ==1): #input check
        if not game.isFinished(board):
            for i in range(8):
                    button[row][i].config(state=DISABLED) #close row
            board = alphaBetaPruning.go(board) #AI turn
            if not game.isFinished(board):
                open_row(button)
                print_new_grid(game_board, button, scores)
            else:
                resultScreen(game_board)
    else:
        print("Ilegal move")

#update the board on the screen
def print_new_grid(game_board, button, scores):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 99:
                button[i][j].config(text='',bg='gray5')
            else:
                button[i][j].config(text=board[i][j])
    str1=str(game.HumScore(board))
    str2=str(game.CompScore(board))
    scores[0].config(text=str1)
    scores[1].config(text=str2)
    game_board.update()
    game_board.update_idletasks()

#start
def main():
    start()
if __name__ == '__main__':
    main()
