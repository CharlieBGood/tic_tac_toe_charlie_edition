import pygame as pg, sys
import time
from pygame.locals import *
from draws import *

#Starts the game
def gameStart(screen, width, height, line_color, opening, session):
    '''define the intro image and position its top left corner in 0,0'''
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill((250,250,250))

    '''draw the mesh inside screen'''
    drawMesh(screen, line_color, width, height)

    '''draw status of the game inside screen'''
    drawStatus(screen, width, session)
    
    drawScoreboard(screen, width, session)


# Resets the game
def resetGame(screen, width, height, line_color, opening, session):

    time.sleep(3)
    session.XO = 'x'
    session.draw = False
    session.winner = None
    session.resetBoard()
    gameStart(screen, width, height, line_color, opening, session)

    drawStatus(screen, width, session)

    return session


#Checks if someone has won
def checkWin(height, width, screen, session):

    '''check for winner in rows'''
    for row in range (3):
        if ((session.board[row][0] == session.board[row][1] == session.board[row][2]) and session.board[row][0] is not None):
            session.setWinner(session.turn)
            pg.draw.line(screen, (250,0,0), (0, (row+1)*height/3 - height/6), (width, (row+1)*height/3 - height/6), 4)
            break
    
    '''check for winner in columns'''
    for col in range(3):
        if ((session.board[0][col] == session.board[1][col] == session.board[2][col]) and session.board[0][col] is not None):
            session.setWinner(session.turn)
            pg.draw.line(screen, (250,0,0), ((col+1)*width/3 - width/6, 0), ((col+1)*width/3 - width/6, height), 4)
            break

    '''check for winner in diagonals'''
    if ((session.board[0][0] == session.board[1][1] == session.board[2][2]) and session.board[0][0] is not None):
            session.setWinner(session.turn)
            pg.draw.line(screen,(250,70,70), (50,50), (350,350), 4)
    
    if ((session.board[0][2] == session.board[1][1] == session.board[2][0]) and session.board[0][2] is not None):
            session.setWinner(session.turn)
            pg.draw.line(screen,(250,70,70), (350,50), (50,350), 4)
    
    if session.winner == session.playerOne:
        session.playerOne.addWin()
    if session.winner == session.playerTwo:
        session.playerTwo.addWin()    
            
    '''if all cells have value and there's no winner declare a draw'''
    if (all([all(row) for row in session.board]) and session.winner is None):
        session.draw = True

    drawStatus(screen, width, session)
    
    return session


#Defines the actions when user clicks the mouse
def userClick(width, height, screen, x_img, o_img, session):

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
    if(y < height/3):
        row = 1
    elif(y < height*2/3):
        row = 2
    elif(y < height):
        row = 3
    else:
        row = None

    if(row and col and session.board[row-1][col-1] is None):
        session = drawXO(row, col, width, height, screen, x_img, o_img, session)
        session = checkWin(height, width, screen, session)
        session.nextTurn()
        drawStatus(screen, width, session)
    return session

