import pygame as pg, sys
import time
from pygame.locals import *
from draws import *

#Starts the game
def gameStart(screen, width, height, line_color, XO, winner, draw, opening):
    '''define the intro image and position its top left corner in 0,0'''
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill((250,250,250))

    '''draw the mesh inside screen'''
    drawMesh(screen, line_color, width, height)

    '''draw status of the game inside screen'''
    drawStatus(XO, winner, draw, screen, width)


# Resets the game
def resetGame(screen, width, height, line_color, XO, winner, draw):

    time.sleep(3)
    XO = 'x'
    draw = False
    gameStart(screen, width, height, line_color, XO, winner, draw, opening)
    winner = None
    board = [[None]*3, [None]*3, [None]*3]


#Checks if someone has won
def checkWin(board, winner, draw, height, width, XO, screen):
    
    '''check for winner in rows'''
    for row in range (3):
        if ((board[row][0] == board[row][1] == board[row][2]) and board[row][0] is not None):
            winner = board[row][0]
            pg.draw.line(screen, (250,0,0), (0, (row+1)*height/3 - height/6), (width, (row+1)*height/3 - height/6), 4)
            break
    
    '''check for winner in columns'''
    for col in range(3):
        if ((board[0][col] == board[1][col] == board[2][col]) and board[0][col] is not None):
            winner = board[0][col]
            pg.draw.line(screen, (250,0,0), (0, (col+1)*height/3 - height/6), (width, (col+1)*height/3 - height/6), 4)
            break

    '''check for winner in diagonals'''
    if ((board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None):
            winner = board[0][0]
            pg.draw.line(screen,(250,70,70), (50,50), (350,350), 4)
    
    if ((board[0][2] == board[1][1] == board[2][0]) and board[0][2] is not None):
            winner = board[0][2]
            pg.draw.line(screen,(250,70,70), (350,50), (50,350), 4)
    
    '''if all cells have value and there's no winner declare a draw'''
    if (all([all(row) for row in board]) and winner is None):
        draw = True

    drawStatus(XO, winner, draw, screen, width)


#Defines the actions when user clicks the mouse
def userClick(width, height, board, XO, screen, x_img, o_img, winner, draw):

    '''get coordinates of mouse'''
    x,y = pg.mouse.get_pos()

    '''get column of mouse click'''
    if(x < width/3):
        col = 1
    elif(x < width*2/3):
        col = 2
    elif(x < width):
        col = 3
    else:
        col = None
    
    '''get row of mouse click'''
    if(x < height/3):
        row = 1
    elif(x < height*2/3):
        row = 2
    elif(x < height):
        row = 3
    else:
        row = None

    if(row and col and board[row-1][col-1] is None):
        XO = drawXO(row, col, board, XO, width, height, screen, x_img, o_img)
        checkWin(board, winner, draw, height, width, XO, screen)



