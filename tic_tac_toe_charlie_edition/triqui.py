import pygame as pg, sys
import time
from pygame.locals import *
from draws import *
from gameStatus import *

#Global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
line_color = (10,10,10)

#Board
board = [[None]*3, [None]*3, [None]*3]

#Initializing pygame window
pg.init()
fps = 60
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption('Triqui')

#Load images
opening, x_img, o_img = loadImages(width, height)

#Start the game
gameStart(screen, width, height, line_color, XO, winner, draw, opening)

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            XO, winner, draw = userClick(width, height, board, XO, screen, x_img, o_img, winner, draw)
            if(winner or draw):
                XO, draw, winner, board = resetGame(screen, width, height, line_color, XO, winner, draw, opening)
        pg.display.update()
        CLOCK.tick(fps)



