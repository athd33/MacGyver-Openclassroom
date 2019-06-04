
import sys
from mapp import *
from player import *
import pygame
from pygame.locals import *
from fonctions import initMapp, displayHelp

game = True
entries = ['Q', 'HELP']
directions = ['N', 'S', 'E', 'O']



pygame.init()  #initialyzing all pygame modules

window = pygame.display.set_mode((500, 500)) # non-resizable
pygame.display.set_caption('Escape-Game: MacGyver')
backgroundImage = pygame.image.load("background.jpg").convert() # convert method to convert and display faster

window.blit(backgroundImage, (0,0)) # adding the image on the window




mappOnline = MappToDisplay(initMapp()) # instanciation of object mappOnline witch is a MappToDisplay class object
print(mappOnline)

macGyver = Player(mappOnline)


while game:
    pygame.display.flip()
    pygame.time.Clock().tick(30)
    mappOnline.render_mapp(window)
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_q:
            print('stop')
            game = False
    """
    entry = input(">")
    entry = entry.upper()
    if entry not in entries:
        print("Invalid direction, try again")
    if entry == "Q":
        print("Exit game")
        game = False
    elif entry == "HELP":
        displayHelp()
    else:
        macGyver.moveMac(entry)
        print(mappOnline)   # renderend mapp by mappToDisoplay class
    """