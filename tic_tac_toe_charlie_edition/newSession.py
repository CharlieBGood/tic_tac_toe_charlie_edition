from tkinter import *
from tkinter import ttk
from classes import *

#Create the window element
window = Tk()
window.title('Players info')
window.geometry('250x100')
window.configure(background = 'white')
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)

#Create input labels
playerOne = Label(window, text='Player 1: ').grid(row=0, column=0)
playerTwo = Label(window, text='Player 2: ').grid(row=1, column=0)

playerOneVar = StringVar()
playerTwoVar = StringVar()

#Create input fields
playerOneInput = Entry(window, justify=CENTER, width = 18, textvariable=playerOneVar).grid(row = 0,column = 1)
playerTwoInput = Entry(window, justify=CENTER, width = 18, textvariable=playerTwoVar).grid(row = 1,column = 1)

pOne = Player()
pTwo = Player()
session = Session(pOne, pTwo)

def getPlayersNames():
    playerOneName = playerOneVar.get()
    playerTwoName = playerTwoVar.get()
    pOne.setName(playerOneName)
    pTwo.setName(playerTwoName)
    window.destroy()


#Create button
btn = ttk.Button(window ,text="Start Game", command=getPlayersNames).place(x=85, y = 65)

def newSession():
    window.mainloop()
    return session
    