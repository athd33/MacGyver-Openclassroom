
import sys
import time
from mapp import *
from player import *
import pygame
from pygame.locals import *
from fonctions import initMapp, displayHelp


os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

pygame.init()  # initialyzing all pygame modules

window = pygame.display.set_mode((750, 750))  # non-resizable

pygame.display.set_caption('Escape-Game: MacGyver')  # window title

# convert to convert and display faster

backgroundImage = pygame.image.load(background_image).convert()
menuImage = pygame.image.load(menuBackground).convert()
winEndImage = pygame.image.load(winImageToDisplay).convert()
loseImage = pygame.image.load(gameOverImage).convert()

window.blit(window, (0, 0))  # adding the image on the windowq

mappOnline = MappToDisplay(initMapp())  # instanciation
macGyver = Player(mappOnline)  # instanciation


while menu:  # first while used for menu display
   
    menuMusic.play()
    window.blit(menuImage, (100, 50))  # adding the image on the window
    window.blit(commandEnterGame, (50, 600))
    window.blit(commandQuitGame, (50, 630))
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
        mappOnline.render_mapp(window)  # method used tu display the mapp

        loaderToShow = Loader(macGyver.win)            
        loaderToDisplay = pygame.image.load(loaderToShow.displayLoader()).convert_alpha()
        loaderToDisplay = pygame.transform.scale(loaderToDisplay, (130, 130))
        window.blit(loaderToDisplay, (320, -30))

        inGameMusic.play()
        pygame.display.flip()

        if macGyver.winGame:
            game = False
            inGameMusic.stop()
            victoryMusic.play()
            window.blit(winEndImage, (100, 100))
            window.blit(winMessage, (200, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
            pygame.time.wait(17000)
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
            

            pygame.display.flip()
            if event.type == pygame.QUIT:
                game = False
            if event.type == KEYDOWN and event.key == K_UP:
                macGyver.moveMac("N")
            if event.type == KEYDOWN and event.key == K_q:
                inGameMusic.stop()
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