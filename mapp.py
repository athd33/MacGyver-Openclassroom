import pygame
from pygame.locals import *

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


    def __repr__(self):
        self.mappRebuilded = [] #empty list        
        for i in self.grid: # joining elements in lines
            self.mappRebuilded.append("".join(i))
        
        self.mappToDisplay = "\n".join(self.mappRebuilded) # joining lines in list

        return f"{self.mappToDisplay}"

    def render_mapp(self, window):
        self.window = window
        sprit_size = 50
        self.line_number = 0
        self.case_number = 0

        wall = pygame.image.load("wall.png")
        wall = pygame.transform.scale(wall, (50,50)) # rezise wall image to fit in mapp
        
        for line in self.lines:
            self.line_number +=1
            for element in line:
                self.case_number +=1

                position_x = (self.line_number * sprit_size)
                position_y = (self.case_number * sprit_size)

                if element == "O":
                    window.blit(wall, (position_x, position_y))
                

        