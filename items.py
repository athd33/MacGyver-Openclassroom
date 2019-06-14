
import pygame
from pygame.locals import *
from constants import sprite_size
import random
import mapp

class ObjectItems():
    def __init__(self, mapp):
        self.mapp = mapp
        self.mapp.item = self
        self.mapp.grid

        for index_x, x in enumerate(self.mapp.grid):
            for index_y, y in enumerate(x):
                if y == "T":
                    self.mapp.item = [index_x, index_y]

    def getFreeCases(self):
        self.freeCases = []        
        for index_x, x in enumerate(self.mapp.grid):
            for index_y, y in enumerate(x):
                #Px = (index_x * sprite_size)
                #Py = (index_y * sprite_size)
                if y == " ":
                    self.freeCases.append([index_x, index_y])
        self.new = random.choice(self.freeCases)   
        return self.new

    def displayObjects(self):
    
        Px = self.mapp.item[0]
        Py = self.mapp.item[1]
        Nx = self.new[0]
        Ny = self.new[1]

        for index_x, x in enumerate(self.mapp.grid):
            for index_y, y in enumerate(x):
                if y == "T":
                    self.mapp.item = [index_x, index_y]
                    self.mapp.grid[Px][Py] = " "
                    self.mapp.grid[Nx][Ny] = "T"
                if y == "N":
                    self.mapp.item = [index_x, index_y]
                    self.mapp.grid[Px][Py] = " "
                    self.mapp.grid[Nx][Ny] = "S"
                if y == "E":
                    self.mapp.item = [index_x, index_y]
                    self.mapp.grid[Px][Py] = " "
                    self.mapp.grid[Nx][Ny] = "E"
                if y == "S":
                    self.mapp.item = [index_x, index_y]
                    self.mapp.grid[Px][Py] = " "
                    self.mapp.grid[Nx][Ny] = "A"

