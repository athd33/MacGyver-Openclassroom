import pygame
from pygame.locals import *
from constants import *
import random


class MappToDisplay():
    """
    Class used to build a indexation of all elements on the mapp
    """
    def __init__(self, content, window):
        self.content = content
        self.grid = []  # self.grid is a list of of the elements on the mapp
        self.lines = self.content.split('\n')
        self.robot = None
        self.item = None

        for line in self.lines:  # creating grid for indexation
            self.grid.append([c for c in line])

    def render_mapp(self, window):
        """Method witch uses Pygame to render the images from the text file"""
        self.window = window
        sprit_size = 50
        self.line_number = 0
        wall = pygame.image.load(wall_image)
        wall = pygame.transform.scale(wall, (50, 50))  # rezise wall sprites
        self.toShuffle = []

        for line in self.grid:
            self.case_number = 0  # return to O after a full line pass
            for element in line:
                Px = (self.case_number * sprit_size)
                Py = (self.line_number * sprit_size)

                if element == "O":
                    window.blit(wall, (Px, Py))

                if element == "X":  # instanciation of ImageToDisplay
                    mac_image = ImageToDisplay(mac_img)
                    window.blit(mac_image.resize(), (Px, Py))
                if element == "U":
                    keeper_to_display = ImageToDisplay(keeper)
                    window.blit(keeper_to_display.resize(), (Px, Py))
                if element == "T":
                    tube_to_display = ImageToDisplay(tube)
                    window.blit(tube_to_display.resize(), (Px, Py))
                if element == "E":
                    ether_to_display = ImageToDisplay(ether)
                    window.blit(ether_to_display.resize(), (Px, Py))
                if element == "A":
                    needle_to_display = ImageToDisplay(needle)
                    window.blit(needle_to_display.resize(), (Px, Py))
                if element == "S":
                    syringe_to_display = ImageToDisplay(syringe)
                    window.blit(syringe_to_display.resize(), (Px, Py))

                self.case_number += 1  # adding 1 after each element pass
            self.line_number += 1  # adding 1 after passing each element


class ImageToDisplay:
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
        self.name_to_display = pygame.image.load(self.image)
        self.name_to_display.set_colorkey((255, 255, 255))
        self.name_to_display = pygame.transform.scale(self.name_to_display, (50, 50))

        return self.name_to_display


class Loader:
    """Class used to display the loader
    self.points is a parameter from the player class instanced"""
    def __init__(self, points):
        self.points = points

    def displayLoader(self):
        """Method used to define witch loader, depends on points"""
        if self.points == 0:
            return firstLoader
        if self.points == 1:
            return secondLoader
        if self.points == 2:
            return thirdLoader
        if self.points == 3:
            return fourthLoader
        if self.points == 4:
            return finalLoader
