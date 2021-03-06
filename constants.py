import pygame
import os


menu = True
game = False
sound = True
entries = ['Q', 'HELP']
directions = ['N', 'S', 'E', 'O']
pygame.font.init()
white = (255, 255, 255)
black = (0, 0, 0)
sprite_size = 50
clock = pygame.time.Clock()
arial_fonts = pygame.font.SysFont("arial", 20)
endFont = pygame.font.SysFont("arial", 50)
winFont = pygame.font.SysFont("arial", 30)

pygame.mixer.init()
menuMusic = pygame.mixer.Sound("./sounds/menuMusic.wav")
grabSound = pygame.mixer.Sound("./sounds/grab.wav")
inGameMusic = pygame.mixer.Sound("./sounds/inGame.wav")


commandQuitGame = arial_fonts.render("Press 'Q' for EXIT", True, white)
commandEnterGame = arial_fonts.render("Press 'ENTER' to START", True, white)
desactivateSound = arial_fonts.render("'M' turn off the music", True, white)
activateSound = arial_fonts.render("'S' turn on the music", True, white)


endMessage = endFont.render("END GAME", True, black)

background_image = "./images/background.jpg"
menuBackground = "./images/macGyverWallpaper.png"
winImageToDisplay = "./images/winImage.png"
gameOverImage = "./images/gameOver.png"

wall_image = "./images/wall.png"
mac_img = "./images/MacGyver.png"
keeper = "./images/Gardien.png"
ether = "./images/ether.png"
syringe = "./images/seringue.png"
needle = "./images/aiguille.png"
tube = "./images/tube_plastique.png"

firstLoader = "./images/firstLoader.png"
secondLoader = "./images/secondLoader.png"
thirdLoader = "./images/thirdLoader.png"
fourthLoader = "./images/fourthLoader.png"
finalLoader = "./images/finalLoader.png"
