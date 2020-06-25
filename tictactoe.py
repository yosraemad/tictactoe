### AI functions ###
def testForkMove(button, s):
    winningMoves = 0
    button['text'] = s
    for j in range(0, 9):
        if l[j]['text'] == '' and testWinMove(l[j], s):
            winningMoves += 1
    button['text'] = ''
    return winningMoves >= 2

def testWinMove(button, s):
    button['text'] = s
    win = checkWinning(s)
    button['text'] = ''
    return win

def getComputerMove():
    global l
    for i in range(0, 9):
        if l[i]['text'] == '' and testWinMove(l[i],'X'):
            return i
    for i in range(0, 9):
        if l[i]['text'] == '' and testWinMove(l[i], 'O'):
            return i
    for i in range(0, 9):
        if l[i]['text'] == '' and testForkMove(l[i], 'X'):
            return i
    playerForks = 0
    for i in range(0, 9):
        if l[i]['text'] == '' and testForkMove(l[i], 'O'):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if l[j]['text'] == '':
                return j
    for i in [0, 2, 6, 8]:
        if l[i]['text'] == '':
            return i
    if l[4]['text'] == '':
        return 4
    for i in [1, 3, 5, 7]:
        if l[i]['text'] == '':
            return i

def playComputer():
    x = getComputerMove()
    changeTextOfTheButton(l[x])
### end AI functions ###

### GUI functions ###
from tkinter import messagebox as mb
click = 0
def changeTextOfTheButton(button):
    global click
    button['text'] = stringValue()
    changePlayer()
    button['state'] = 'disabled'
    button['disabledforeground'] = 'black'
    click += 1
    if checkWinning(button['text']):
        changePlayer()
        mb.showinfo('Congrats', 'Player {} won!'.format(player))
        m.destroy()
    if (click == 9):
        mb.showinfo('Congrats', 'It\'s a draw!')
        m.destroy()
    if (player == 2 and click != 9):
        playComputer()
    

player = 1

def stringValue():
    if player == 1:
        return 'X'
    else:
        return 'O'
def changePlayer():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def checkWinning(str):
    return ((button1['text'] == str and button2['text'] == str and button3['text'] == str) or
            (button4['text'] == str and button5['text'] == str and button6['text'] == str) or
            (button7['text'] == str and button8['text'] == str and button9['text'] == str) or
            (button1['text'] == str and button4['text'] == str and button7['text'] == str) or
            (button2['text'] == str and button5['text'] == str and button8['text'] == str) or
            (button3['text'] == str and button6['text'] == str and button9['text'] == str) or
            (button1['text'] == str and button5['text'] == str and button9['text'] == str) or
            (button3['text'] == str and button5['text'] == str and button7['text'] == str))

### end GUI functions ###

### GUI ###

import tkinter
m = tkinter.Tk()

m.title('tic tac toe')

l = []

button1 = tkinter.Button(m, text='', width=10, height = 5)
button1['command'] = lambda: changeTextOfTheButton(button1)
button1.grid(row=0, column=0)
l.append(button1)

button2 = tkinter.Button(m, text='', width=10, height = 5)
button2['command'] = lambda: changeTextOfTheButton(button2)
button2.grid(row=0, column=1)
l.append(button2)

button3 = tkinter.Button(m, text='', width=10, height = 5)
button3['command'] = lambda: changeTextOfTheButton(button3)
button3.grid(row=0, column=2)
l.append(button3)

button4 = tkinter.Button(m, text='', width=10, height = 5)
button4['command'] = lambda: changeTextOfTheButton(button4)
button4.grid(row=1, column=0)
l.append(button4)

button5 = tkinter.Button(m, text='', width=10, height = 5)
button5['command'] = lambda: changeTextOfTheButton(button5)
button5.grid(row=1, column=1)
l.append(button5)

button6 = tkinter.Button(m, text='', width=10, height = 5)
button6['command'] = lambda: changeTextOfTheButton(button6)
button6.grid(row=1, column=2)
l.append(button6)

button7 = tkinter.Button(m, text='', width=10, height = 5)
button7['command'] = lambda: changeTextOfTheButton(button7)
button7.grid(row=2, column=0)
l.append(button7)

button8 = tkinter.Button(m, text='', width=10, height = 5)
button8['command'] = lambda: changeTextOfTheButton(button8)
button8.grid(row=2, column=1)
l.append(button8)

button9 = tkinter.Button(m, text='', width=10, height = 5)
button9['command'] = lambda: changeTextOfTheButton(button9)
button9.grid(row=2, column=2)
l.append(button9)


m.mainloop()

### end GUI ###
