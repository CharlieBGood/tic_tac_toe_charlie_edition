from tkinter import *
from tkinter import ttk, filedialog
from classes import *
from tkinter import messagebox
import shutil

#Create the window element
window = Tk()
window.title('Players info')
window.geometry('350x100')
window.configure(background = 'white')
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)

#Create the variables for the paths of the images 
imgPathPlayerOne = ''
imgPathPlayerTwo = ''

#Creates strings for the inputs
playerOneVar = StringVar()
playerTwoVar = StringVar()

#Creates players and session
pOne = Player()
pTwo = Player()
session = Session(pOne, pTwo)

#Gets the players names and set their paths to the images.
def getPlayersNames():
    playerOneName = playerOneVar.get()
    playerTwoName = playerTwoVar.get()
    if not playerOneName or not playerTwoName:
        messagebox.showwarning("NO NAME WAS PROBIDED", 'ONE OR MORE PLAYER NAME FIELDS ARE EMPTY' ) 
    elif len(playerOneName) > 7 or len(playerTwoName) > 7:
        messagebox.showwarning("STRING TOO LONG", 'NAMES CAN\'T CONTAIN MORE THAN 7 LETTERS' ) 
    else:        
        print(pOne.imgPath)
        pOne.setName(playerOneName)
        pTwo.setName(playerTwoName)
        window.destroy()


#Moves image of player one to 'images' folder
def moveFilePlayerOne():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("jpeg files",
                                                        "*.jpg"),
                                                       ("all files",
                                                        "*.*")))
    if filename:  
        shutil.copyfile(filename, 'face_segmentation/images/imagePlayerOne.jpg')
        pOne.setImgPath('face_segmentation/images/imagePlayerOne.jpg')
    
        
#Moves image of player two to 'images' folder
def moveFilePlayerTwo():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("jpeg files",
                                                        "*.jpg"),
                                                       ("all files",
                                                        "*.*")))
    
    if filename:
        shutil.copyfile(filename, 'face_segmentation/images/imagePlayerTwo.jpg')
        pTwo.setImgPath('face_segmentation/images/imagePlayerTwo.jpg')


#Creates input labels
playerOne = Label(window, text='Player 1: ').grid(row=0, column=0)
playerTwo = Label(window, text='Player 2: ').grid(row=1, column=0)

#Creates input fields
playerOneInput = Entry(window, justify=CENTER, width = 18, textvariable=playerOneVar).grid(row = 0,column = 1)
playerTwoInput = Entry(window, justify=CENTER, width = 18, textvariable=playerTwoVar).grid(row = 1,column = 1)

# Creates browse files buttons
button_explore = Button(window, text = "Browse Files", command = moveFilePlayerOne).grid(row=0, column=2)
button_explore = Button(window, text = "Browse Files", command = moveFilePlayerTwo).grid(row=1, column=2)

#Creates button
btn = ttk.Button(window ,text="Start Game", command=getPlayersNames).place(x=85, y = 65)

def newSession():
    window.mainloop()
    return session
    