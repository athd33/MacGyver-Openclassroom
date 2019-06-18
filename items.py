import pygame
from pygame.locals import *
from constants import sprite_size
import random
import mapp


class ObjectItems():
    """Class defined to attribute a random position for objects in game"""

    def __init__(self, mapp):
        self.mapp = mapp
        self.mapp.item = self
        self.mapp.grid

    def getFreeCases(self):
        """Method used to get all the free cases in the mapp"""

        self.freeCases = []        
        for index_x, x in enumerate(self.mapp.grid):
            for index_y, y in enumerate(x):
                if y == " ":

                    self.freeCases.append([index_x, index_y])
        self.new = random.choice(self.freeCases)        
        return self.new

    def setObjectsPositions(self):
        """Method used to attribute a random position to all objects"""

        items = ["T", "A", "E", "S"]

        for i in items:
            newPos = self.getFreeCases()
            Nx = newPos[0]
            Ny = newPos[1]
            self.mapp.grid[Nx][Ny] = i

