from tkinter import *
import random

win = Tk()
win.title('Tic-Tac-Toe Game')
win.geometry("320x460") 



def winner(b,letter):
    return  ((b[1]==letter and b[2]==letter and b[3]==letter) or
            (b[4]==letter and b[5]==letter and b[6]==letter) or
            (b[7]==letter and b[8]==letter and b[9]==letter) or 
            (b[1]==letter and b[4]==letter and b[7]==letter) or
            (b[2]==letter and b[5]==letter and b[8]==letter) or
            (b[3]==letter and b[6]==letter and b[9]==letter) or
            (b[1]==letter and b[5]==letter and b[9]==letter) or
            (b[3]==letter and b[5]==letter and b[7]==letter))



rval = StringVar(value='0')

theLabel = Label(win, text="Select Game Level: ", font=('Helvetica', '20', 'bold'))
theLabel.grid(row=0,column=0,columnspan=9, sticky=N+E+W+S)

o1=Radiobutton(win,text="Easy",value='easy',variable=rval,command=lambda: display(easy), font=('Helvetica', '15', 'bold'))
o1.grid(row=1,column=0,columnspan=3, sticky=N+E+W+S)
o2=Radiobutton(win,text="Medium",value='medium',variable=rval, command=lambda: display(medium), font=('Helvetica', '15', 'bold'))
o2.grid(row=1,column=3,columnspan=3,sticky=N+E+W+S)
o3=Radiobutton(win,text="Hard",value='hard',variable=rval, command=lambda: display(hard), font=('Helvetica', '15', 'bold'))
o3.grid(row=1,column=6,columnspan=3,sticky=N+E+W+S)

resultLabel = Label(win,text='', font=('Helvetica', '20', 'bold'))
resultLabel.grid(row=9,column=1,columnspan=9, sticky=N+E+W+S)

def display(level):

    resultLabel.config(text='')

    global board, btns, available
    board = [' ' for x in range(10)]
    btns = ['']

    available = [1,2,3,4,5,6,7,8,9]

    c = 1
    for i in range(3,6):
        for j in range(0,7,3):

            label = LabelFrame(win, width=100, height=100)
            label.grid(row=i, column=j, columnspan=3)
            label.grid_propagate(False)
            label.grid_rowconfigure(0, weight=1)
            label.grid_columnconfigure(0, weight=1)


            btn = Button(label, 
                        text=' ',
                        activebackground='light blue',
                        command=lambda i=c: level(i)) 

            btn.grid(row=0, column=0, sticky='nesw') 
            btns.append(btn)
            c += 1

    restartbtn = Button(win,text='Restart',activebackground='light blue',command=lambda: display(level),font=('Helvetica', '10', 'bold'))
    restartbtn.grid(row=10,column=1,columnspan=9, sticky=N+E+W+S)


def hard(i):
    global board, btns, available
    if board[i] == ' ' and not winner(board,'X' or 'O'):
        
        # player move
        board[i] = 'X'
        btns[i].config(text=board[i],font=('Helvetica', '20', 'bold'))
        available.remove(i)
        # if no available space then match draw
        if len(available)==0:
            return resultLabel.config(text = 'Match Draw!!!')

        # computer smart move to win the game or stop player to win
        # This will put 'O' at those places where computer or player is going to win
        for let in ['O','X']:
            for n in available:
                boardcopy = board[:]
                boardcopy[n] = let
                if winner(boardcopy,let):
                    move = n
                    available.remove(move)
                    return printboard(move)

        # computer center move
        if 5 in available:
            move = 5
            available.remove(move)
            return printboard(move)

        # computer available corners
        corners = []
        for n in available:
            if n in [1,3,7,9]:
                corners.append(n)

        # computer corner move
        # This condition will stop the player to win the game by opposite corners technique
        # If player try to win the game by opposite corners technique this will pass the computer move to edges move
        if (len(corners)!=2 and board[5] == 'O') or board[5] == 'X':      
            if len(corners)>0:
                move = random.choice(corners)
                available.remove(move)
                return printboard(move)

        # computer available edges
        edges = []
        for n in available:
            if n in [2,4,6,8]:
                edges.append(n)

        # computer edges move
        if len(edges)>0:
            move = random.choice(edges)
            available.remove(move)
            return printboard(move)


def easy(i):
    global board, btns, available
    if board[i] == ' ' and not (winner(board,'O') or winner(board, 'X')):

        # player move
        board[i] = 'X'
        btns[i].config(text=board[i],font=('Helvetica', '20', 'bold'))
        available.remove(i)
        # if no available space then match draw
        if len(available)==0:
            resultLabel.config(text = 'Match Draw!!!')

        # computer random move at available spaces
        move = random.choice(available)
        available.remove(move)
        return printboard(move)


def medium(i):
    global board, btns, available
    if board[i] == ' ' and not (winner(board,'O') or winner(board, 'X')):

        # player move
        board[i] = 'X'
        btns[i].config(text=board[i],font=('Helvetica', '20', 'bold'))
        available.remove(i)
        # if no available space then match draw
        if len(available)==0:
            resultLabel.config(text = 'Match Draw!!!')

        # computer smart move to win the game or stop player to win
        # This will put 'O' at those places where computer or player is going to win
        for let in ['O','X']:
            for n in available:
                boardcopy = board[:]
                boardcopy[n] = let
                if winner(boardcopy,let):
                    move = n
                    available.remove(move)
                    return printboard(move)

        # computer random move
        move = random.choice(available)
        available.remove(move)
        return printboard(move)


def printboard(move):
    if winner(board,'X'):
        resultLabel.config(text = 'You Won!!!')
    else:
        board[move] = 'O'
        for n in range(1,10):
            btns[n].config(text=board[n],font=('Helvetica', '20', 'bold'))
            if winner(board,'O'):
                resultLabel.config(text = 'You Lost!!!')


win.mainloop()

