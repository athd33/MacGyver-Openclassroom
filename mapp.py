import pygame
from pygame.locals import *
from constants import *
class MappToDisplay():
    """
    Class used to build a indexation of all elements on the mapp
    """
    def __init__(self, content):
        self.content = content
        self.grid = []          #self.grid is a list of of the elements on the mapp
        self.lines = self.content.split('\n')
        self.robot = None

        for line in self.lines:             # creating grid for indexation of each element of the game lab
            self.grid.append([c for c in line])

    def render_mapp(self, window):
        self.window = window
        sprit_size = 50
        self.line_number = 0
        cases = ["X", " ", "U"]
        wall = pygame.image.load(wall_image)
        wall = pygame.transform.scale(wall, (50,50)) # rezise wall image to fit in mapp
        
        for line in self.grid:
            self.case_number = 0 # return to O after a full line pass
            for element in line:
                position_x = (self.case_number * sprit_size)
                position_y = (self.line_number * sprit_size)
               
                if element == "O":
                    window.blit(wall, (position_x, position_y))      
               
                if element == "X":
                    mac_image = ImageToDisplay(mac_img) # instanciation of class ImageToDisplay objet                  
                    window.blit(mac_image.resize(), (position_x, position_y)) # use classe method resize()

                if element == "U":
                    keeper_to_display = ImageToDisplay(keeper) # instanciation of class ImageToDisplay objet
                    window.blit(keeper_to_display.resize(), (position_x, position_y)) # use classe method resize()            
                
                if element == "E":
                    ether_to_display = ImageToDisplay(ether)
                    window.blit(ether_to_display.resize(), (position_x, position_y)) # use classe method resize()            


                self.case_number +=1 # adding 1 after each element pass
            self.line_number +=1 # adding 1 after passing each element of a line


        



class ImageToDisplay:           # Class créated to resize elements before display with pygame
    """
    Class used to set the image for render
    """

    def __init__(self, image): 
        """
        Function used to resize the images before render
        """
        self.image = image

    def resize(self):
        """
        Method used to resize the choosen image into 50/50 pixels size
        """
        self.name_to_display = pygame.image.load(self.image).convert_alpha()# convert alpha for transparent background
        self.name_to_display = pygame.transform.scale(self.name_to_display, (50,50))
        return self.name_to_display