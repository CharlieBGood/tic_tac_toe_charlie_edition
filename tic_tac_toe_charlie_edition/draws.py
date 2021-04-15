import pygame as pg, sys


#Returns images
def loadImages(width, height):
    '''Load images'''
    opening = pg.image.load('images/opening.png')
    x_img = pg.image.load('images/X.png')
    o_img = pg.image.load('images/O.png')

    '''Resizing images'''
    x_img = pg.transform.scale(x_img, (80,80))
    o_img = pg.transform.scale(o_img, (80, 80))
    opening = pg.transform.scale (opening, (width, height+200))

    return opening, x_img, o_img

#Draws mesh inside screen
def drawMesh(screen, line_color, width, height):
    '''Drawing vertical lines
    Draws a vertical line inside screen of color line_color, that starts in pos1, ends in pos2 and of width 7'''
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (width*2/3, 0), (width*2/3, height), 7)

    '''Drawing horizontal lines'''
    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height*2/3), (width, height*2/3), 7)


# draws XO inside the board
def drawXO(row, col, width, height, screen, x_img, o_img, session):
    
    posx = width*(row-1)/3 + 30
    posy = height*(col-1)/3 + 30

    session.board[row-1][col-1] = session.XO

    if(session.XO=='x'):
        screen.blit(x_img, (posy, posx))
        session.XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        session.XO = 'x'
    pg.display.update()
    
    return session


#Defines if there is a draw
def drawStatus(screen, width, session):

    messageTurn = ''
    if session.winner == None and not session.draw:
        message = session.XO.upper() + "'s Turn"
        messageTurn = session.turn.name
    elif session.draw:
        message = "Game Draw!"
    else:
        message = session.winner.name.upper() + " Won!"

    font = pg.font.Font(None, 40)
    '''render font with message, antialias=True and color'''
    text = font.render(message, 1, (255, 255, 255))

    '''fills screen with a color and inside the rect of 4 channels'''
    screen.fill((0,0,0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)

    
    fontTurn = pg.font.Font(None, 20)
    textName = fontTurn.render(messageTurn, 1, (255, 255, 255))
    textName_rect = textName.get_rect(center=(width/2, 500-25))
    screen.blit(textName, textName_rect)
    
    pg.display.update()
    

def drawScoreboard(screen, width, session):
    
    '''Draw player One name'''
    playerOneName = session.playerOne.name
    font = pg.font.Font(None, 30)
    '''render font with message, antialias=True and color'''
    textPOneName = font.render(playerOneName, 1, (0, 0, 0))
    textPOneName_rect = textPOneName.get_rect(center=(width/6, 550-25))
    screen.blit(textPOneName, textPOneName_rect)
    
    '''Draw player One score'''
    playerOneScore = str(session.playerOne.score)
    font = pg.font.Font(None, 30)
    '''render font with message, antialias=True and color'''
    textPOneScore = font.render(playerOneScore, 1, (0, 0, 0))
    textPOneScore_rect = textPOneScore.get_rect(center=(width/6, 600-25))
    screen.blit(textPOneScore, textPOneScore_rect)
    
    messageVs = 'VS'
    font = pg.font.Font(None, 45)
    '''render font with message, antialias=True and color'''
    textVs = font.render(messageVs, 1, (0, 0, 0))
    textVs_rect = textVs.get_rect(center=(width/2, 600-50))
    screen.blit(textVs, textVs_rect)
    
    '''Draw player Two name'''
    playerTwoName = session.playerTwo.name 
    font = pg.font.Font(None, 30)
    '''render font with message, antialias=True and color'''
    textPTwoName = font.render(playerTwoName, 1, (0, 0, 0))
    textPTwoName_rect = textPTwoName.get_rect(center=(width*5/6, 550-25))
    screen.blit(textPTwoName, textPTwoName_rect)
    
    '''Draw player Two score'''
    playerTwoScore = str(session.playerTwo.score)
    font = pg.font.Font(None, 30)
    '''render font with message, antialias=True and color'''
    textPTwoScore = font.render(playerTwoScore, 1, (0, 0, 0))
    textPTwoScore_rect = textPTwoScore.get_rect(center=(width*5/6, 600-25))
    screen.blit(textPTwoScore, textPTwoScore_rect)
    
    pg.display.update()
    