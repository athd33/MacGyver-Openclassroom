
import sys
import time
from mapp import *
from player import *
import pygame
from pygame.locals import *
from fonctions import initMapp, displayHelp

menu = True
game = False
sound = True
entries = ['Q', 'HELP']
directions = ['N', 'S', 'E', 'O']
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

pygame.init()  # initialyzing all pygame modules

window = pygame.display.set_mode((500, 500))  # non-resizable

pygame.display.set_caption('Escape-Game: MacGyver')  # window title

# convert to convert and display faster

backgroundImage = pygame.image.load(background_image).convert()
menuImage = pygame.image.load(menuBackground).convert()
winEndImage = pygame.image.load(winImageToDisplay).convert()
loseImage = pygame.image.load(gameOverImage).convert()


window.blit(window, (0, 0))  # adding the image on the window


while menu:  # first while used for menu display
    mappOnline = MappToDisplay(initMapp())  # instanciation of object mappOnline
    macGyver = Player(mappOnline)  # instanciation of macGyver as a player class
    menuMusic.play()
    window.blit(menuImage, (-50, 0))  # adding the image on the window
    window.blit(commandQuitGame, (50, 400))
    window.blit(commandEnterGame, (50, 430))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == KEYDOWN and event.key == K_q:
            menu = False
        if event.type == KEYDOWN and event.key == K_RETURN:            
            menu = False
            menuMusic.stop()
            game = True

    while game:
        pygame.display.flip()
        pygame.time.Clock().tick(30)    
        mappOnline.render_mapp(window)  # method used tu display the mapp
        # inGameMusic.play()

        if macGyver.winGame:  # wining conditions all good
            game = False
            inGameMusic.stop()
            victoryMusic.play()
            window.blit(winEndImage, (0, 0))
            window.blit(winMessage, (130, 0))
            pygame.display.flip()
            pygame.time.wait(19000)
            menu = True

        if macGyver.looseGame:  # wining conditions all good
            game = False
            inGameMusic.stop()
            gameOverMusic.play()
            window.blit(loseImage, (-80, 0))
            pygame.display.flip()
            pygame.time.wait(7000)
            menu = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == KEYDOWN and event.key == K_UP:
                macGyver.moveMac("N")
            if event.type == KEYDOWN and event.key == K_q:

                pygame.display.flip()
                game = False
                menu = True

            if event.type == KEYDOWN and event.key == K_DOWN:
                macGyver.moveMac("S")
            if event.type == KEYDOWN and event.key == K_LEFT:
                macGyver.moveMac("O")
            if event.type == KEYDOWN and event.key == K_RIGHT:
                macGyver.moveMac("E")

        window.blit(backgroundImage, (0, 0))  # adding the image on the window
        mappOnline.render_mapp(window)  # method used tu display the mapp

        

            
