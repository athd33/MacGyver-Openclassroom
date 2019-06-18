
import sys
import time
from mapp import *
from player import *
import pygame
from pygame.locals import *
from fonctions import initMapp, displayHelp
from items import ObjectItems

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window

pygame.init()  # initialyzing all pygame modules

window = pygame.display.set_mode((750, 750))  # non-resizable

pygame.display.set_caption('Escape-Game: MacGyver')  # window title

            ###### loadings ##########
backgroundImage = pygame.image.load(background_image).convert()
menuImage = pygame.image.load(menuBackground).convert()
winEndImage = pygame.image.load(winImageToDisplay).convert()
loseImage = pygame.image.load(gameOverImage).convert()

window.blit(window, (0, 0))  # adding the image on the window
clock.tick(5) #refresh limit 5/sec

mappOnline = MappToDisplay(initMapp(), window)  # instanciation
macGyver = Player(mappOnline)  # instanciation

objects = False # no objects displayed


while menu:  # first while used for menu display
    pygame.time.Clock().tick(5)

    window.blit(menuImage, (100, 50))  # adding the image on the window
    window.blit(commandEnterGame, (180, 400))
    window.blit(commandQuitGame, (180, 430))
    window.blit(activateSound, (180, 460))
    window.blit(desactivateSound, (180, 490))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == KEYDOWN and event.key == K_q:
            menu = False
        if event.type == KEYDOWN and event.key == K_s:
            menuMusic.play()
        if event.type == KEYDOWN and event.key == K_m:
            menuMusic.stop()
        if event.type == KEYDOWN and event.key == K_RETURN:  
            mappOnline = MappToDisplay(initMapp(), window)  # instanciation
            macGyver = Player(mappOnline)  # instanciation          
            menu = False
            menuMusic.stop()
            game = True

    while game:     # second while used for the in-game display
        
        if objects == False:
            objectsToDisplay = ObjectItems(mappOnline)
            objectsToDisplay.getFreeCases()
            objectsToDisplay.setObjectsPositions()
            objects = True

        pygame.time.Clock().tick(20)
        mappOnline.render_mapp(window)  # method used tu display the mapp
        loaderToShow = Loader(macGyver.win)            
        loaderToDisplay = pygame.image.load(loaderToShow.displayLoader()).convert_alpha()
        loaderToDisplay = pygame.transform.scale(loaderToDisplay, (130, 130))
        window.blit(loaderToDisplay, (320, -30))
        pygame.display.flip()

        while macGyver.winGame:

            game = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == KEYDOWN and event.key == K_q:
                    macGyver.winGame = False
                    objects = False
                    menu = True

            pygame.display.flip()
            inGameMusic.stop()
            victoryMusic.play()
            window.blit(winEndImage, (100, 100))
            window.blit(commandQuitGame, (150, 550))
            pygame.display.flip()
            menu = True

        while macGyver.looseGame:  # wining conditions all good

            game = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == KEYDOWN and event.key == K_q:
                    macGyver.looseGame = False
                    objects = False
                    menu = True
                    
            inGameMusic.stop()
            window.blit(loseImage, (0, 150))            
            window.blit(commandQuitGame, (150, 550))
            pygame.display.flip()
            menu = True
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == KEYDOWN and event.key == K_q:
                inGameMusic.stop()
                pygame.display.flip()
                game = False
                objects = False
                menu = True
            if event.type == KEYDOWN and event.key == K_s:
                inGameMusic.play()
            if event.type == KEYDOWN and event.key == K_m:
                inGameMusic.stop()
            if event.type == KEYDOWN and event.key == K_UP:
                macGyver.moveMac("N")
            if event.type == KEYDOWN and event.key == K_DOWN:
                macGyver.moveMac("S")
            if event.type == KEYDOWN and event.key == K_LEFT:
                macGyver.moveMac("O")
            if event.type == KEYDOWN and event.key == K_RIGHT:
                macGyver.moveMac("E")

        window.blit(backgroundImage, (0, 0))  # adding the image on the window
        mappOnline.render_mapp(window)  # method used tu display the mapp