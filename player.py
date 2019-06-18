
from mapp import *
from constants import *
import pygame
from pygame.locals import *


class Player():
    """
    Class used for the players moves on the mapp
    """
    def __init__(self, mapp):
        self.mapp = mapp
        self.mapp.robot = self
        self.win = 0    # numbers of items collected
        grid = self.mapp.grid
        self.winGame = False
        self.looseGame = False
        self.sound = False

        for index_x, x in enumerate(grid): # used to get the player position
            for index_y, y in enumerate(x):
                if y == "X":
                    self.mapp.robot = [index_x, index_y]

    def check_next_case(self, direction):
        """Defines the next position of the player on the mapp"""

        self.direction = direction
        Rx = self.mapp.robot[0]
        Ry = self.mapp.robot[1]
        grid = self.mapp.grid

        if direction == "O":
            return grid[Rx][Ry - 1]
        elif direction == "E":
            return grid[Rx][Ry + 1]
        elif direction == "S":
            return grid[Rx + 1][Ry]
        elif direction == "N":
            return grid[Rx - 1][Ry]

    def check_event(self, direction):
        """Check if the next case is an event """
        entries = ["S", "T", "A", "E"] # objects names
        self.direction = direction
        nextCase = self.check_next_case(direction)

        if nextCase == "O":
            return False

        elif nextCase in entries:
            self.sound = True
            self.win += 1

        if self.win == 4 and nextCase == "U":
            self.winGame = True

        if self.win != 4 and nextCase == "U":
            self.looseGame = True

        return True

    def moveMac(self, direction):
        """
        Method witch checks and defines the next position of Macgyver
        on the mapp
        """
        Rx = self.mapp.robot[0]
        Ry = self.mapp.robot[1]
        robot = self.mapp.robot

        if self.check_event(direction):
            if direction == "N":
                self.mapp.grid[Rx - 1][Ry] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[0] -= 1
            if direction == "S":
                self.mapp.grid[Rx + 1][Ry] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[0] += 1
            if direction == "E":
                self.mapp.grid[Rx][Ry + 1] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[1] += 1
            if direction == "O":
                self.mapp.grid[Rx][Ry - 1] = "X"
                self.mapp.grid[Rx][Ry] = " "
                robot[1] -= 1