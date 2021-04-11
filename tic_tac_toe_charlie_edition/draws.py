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
    opening = pg.transform.scale (opening, (width, height+100))

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
def drawXO(row, col, board, XO, width, height, screen, x_img, o_img):
    
    posx = width*(row-1)/3 + 30
    posy = height*(col-1)/3 + 30

    board[row-1][col-1] = XO

    if(XO=='x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()

    return XO


#Defines if there is a draw
def drawStatus(XO, winner, draw, screen, width):

    if winner == None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"
    if draw:
        message = "Game Draw!"

    font = pg.font.Font(None, 30)
    '''render font with message, antialias=True and color'''
    text = font.render(message, 1, (255, 255, 255))

    '''fills screen with a color and inside the rect of 4 channels'''
    screen.fill((0,0,0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()