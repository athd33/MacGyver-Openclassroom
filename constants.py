import pygame
from pygame import *
import os


pygame.font.init()
white = (255, 255, 255)
black = (0, 0, 0)
arial_fonts = pygame.font.SysFont("arial", 20)
endFont = pygame.font.SysFont("arial", 50)

pygame.mixer.init()
menuMusic = pygame.mixer.Sound("./sounds/menuMusic.wav")

commandQuitGame = arial_fonts.render("'Q' for EXIT", True, white)
commandEnterGame = arial_fonts.render("'ENTER' to START", True, white)
commandMuteSound = arial_fonts.render("'S' turn off the music", True, white)

endMessage = endFont.render("END GAME", True, black)

background_image = "./images/background.jpg"
menuBackground = "./images/macGyverWallpaper.png"

wall_image = "./images/wall.png"
mac_img = "./images/MacGyver.png"
keeper = "./images/Gardien.png"
ether = "./images/ether.png"
syringe = "./images/seringue.png"
needle = "./images/aiguille.png"
tube = "./images/tube_plastique.png"
