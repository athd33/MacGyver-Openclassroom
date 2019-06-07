
import sys
import time
from mapp import *
from player import *
import pygame
from pygame.locals import *
from fonctions import initMapp, displayHelp

menu = True
game = False
entries = ['Q', 'HELP']
directions = ['N', 'S', 'E', 'O']
background_image = "./images/background.jpg"
menuBackground = "./images/menumacgyver.png"

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

pygame.init()  # initialyzing all pygame modules

window = pygame.display.set_mode((500, 500))  # non-resizable

pygame.display.set_caption('Escape-Game: MacGyver')  # window title

# convert to convert and display faster
backgroundImage = pygame.image.load(background_image).convert()
menuImage = pygame.image.load(menuBackground).convert()

window.blit(window, (0, 0))  # adding the image on the window

mappOnline = MappToDisplay(initMapp())  # instanciation of object mappOnline

macGyver = Player(mappOnline)  # instanciation of macGyver as a player class


while menu:  # first while used for menu display
    window.blit(menuImage, (0, 80))  # adding the image on the window
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == KEYDOWN and event.key == K_q:
            print('stop')
            menu = False
        if event.type == KEYDOWN and event.key == K_g:
            print('stop')
            menu = False
            game = True

    while game:
        pygame.display.flip()
        pygame.time.Clock().tick(30)    
        mappOnline.render_mapp(window)  # method used tu display the mapp
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False 
            if event.type == KEYDOWN and event.key == K_UP:
                macGyver.moveMac("N")
            if event.type == KEYDOWN and event.key == K_q:
                exit(0)
            if event.type == KEYDOWN and event.key == K_DOWN:
                macGyver.moveMac("S")
            if event.type == KEYDOWN and event.key == K_LEFT:
                macGyver.moveMac("O")
            if event.type == KEYDOWN and event.key == K_RIGHT:
                macGyver.moveMac("E")

        window.blit(backgroundImage, (0, 0))  # adding the image on the window
        mappOnline.render_mapp(window)  # method used tu display the mapp

        

            
