from tkinter import *

window = Tk()
window.geometry("130x150")
window.title('Tic Tac Toe')

player = 'x'
print('x starts the game')

def click(num):
    global player, window

    if num == 1:
        print(text_1.get(), not text_1)
        if text_1.get() == ' ':
            text_1.set(player)
            print('here', text_1.get())
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 2:
        if text_2.get() == ' ':
            text_2.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'
            
    elif num == 3:
        if text_3.get() == ' ':
            text_3.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 4:
        if text_4.get() == ' ':
            text_4.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 5:
        if text_5.get() == ' ':
            text_5.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 6:
        if text_6.get() == ' ':
            text_6.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 7:
        if text_7.get() == ' ':
            text_7.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'
            
    elif num == 8:
        if text_8.get() == ' ':
            text_8.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    elif num == 9:
        if text_9.get() == ' ':
            text_9.set(player)
            if player == 'x':
                player = 'o'
            else:
                player = 'x'

    if (text_1.get() == text_2.get() and text_2.get() == text_3.get() and text_1.get() != ' '):
        print(text_1.get() + ' won the game')
        window.destroy()

    elif (text_4.get() == text_5.get() and text_5.get() == text_6.get() and text_4.get() != ' '):
        print(text_4.get() + ' won the game')
        window.destroy()

    elif (text_7.get() == text_8.get() and text_8.get() == text_9.get() and text_7.get() != ' '):
        print(text_7.get() + ' won the game')
        window.destroy()

    elif (text_1.get() == text_4.get() and text_4.get() == text_7.get() and text_1.get() != ' '):
        print(text_1.get() + ' won the game')
        window.destroy()

    elif (text_2.get() == text_5.get() and text_5.get() == text_8.get() and text_2.get() != ' '):
        print(text_2.get() + ' won the game')
        window.destroy()

    elif (text_3.get() == text_6.get() and text_6.get() == text_9.get() and text_3.get() != ' '):
        print(text_3.get() + ' won the game')
        window.destroy()

    elif (text_1.get() == text_5.get() and text_5.get() == text_9.get() and text_1.get() != ' '):
        print(text_1.get() + ' won the game')
        window.destroy()

    elif (text_3.get() == text_5.get() and text_5.get() == text_7.get() and text_3.get() != ' '):
        print(text_3.get() + ' won the game')
        window.destroy()

text_1 = StringVar()
text_2 = StringVar()
text_3 = StringVar()
text_4 = StringVar()
text_5 = StringVar()
text_6 = StringVar()
text_7 = StringVar()
text_8 = StringVar()
text_9 = StringVar()

_1 = Button(window, textvariable = text_1, height = 2, width = 2, command = lambda : click(1))
_2 = Button(window, textvariable = text_2, height = 2, width = 2, command = lambda : click(2))
_3 = Button(window, textvariable = text_3, height = 2, width = 2, command = lambda : click(3))
_4 = Button(window, textvariable = text_4, height = 2, width = 2, command = lambda : click(4))
_5 = Button(window, textvariable = text_5, height = 2, width = 2, command = lambda : click(5))
_6 = Button(window, textvariable = text_6, height = 2, width = 2, command = lambda : click(6))
_7 = Button(window, textvariable = text_7, height = 2, width = 2, command = lambda : click(7))
_8 = Button(window, textvariable = text_8, height = 2, width = 2, command = lambda : click(8))
_9 = Button(window, textvariable = text_9, height = 2, width = 2, command = lambda : click(9))

text_1.set(' ')
text_2.set(' ')
text_3.set(' ')
text_4.set(' ')
text_5.set(' ')
text_6.set(' ')
text_7.set(' ')
text_8.set(' ')
text_9.set(' ')

_1.grid(row = 1, column = 1)
_2.grid(row = 1, column = 2)
_3.grid(row = 1, column = 3)
_4.grid(row = 2, column = 1)
_5.grid(row = 2, column = 2)
_6.grid(row = 2, column = 3)
_7.grid(row = 3, column = 1)
_8.grid(row = 3, column = 2)
_9.grid(row = 3, column = 3)

window.mainloop()
