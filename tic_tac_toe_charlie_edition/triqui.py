import pygame as pg, sys
import time
from pygame.locals import *
from draws import *
from gameStatus import *
from newSession import *

session = newSession()

#Global variables
width = 400
height = 400
line_color = (10,10,10)

#Initializing pygame window
pg.init()
fps = 60
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+200), 0, 32)
pg.display.set_caption('Triqui - Charlie Edition')

#Load images
opening, x_img, o_img = loadImages(width, height)

#Start the game
gameStart(screen, width, height, line_color, opening, session)

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            session = userClick(width, height, screen, x_img, o_img, session)
            if(session.winner or session.draw):
                print('draw')
                session = resetGame(screen, width, height, line_color, opening, session)
        pg.display.update()
        CLOCK.tick(fps)



