# File: tie_fighter.py
# Author: Steve Hommy
# Description: Tie fighter class and inheriting Ship class

from ship_factory import Ship
from laser import Laser
import pygame
import os


# Tie fighter
TIE_FIGHTER = pygame.image.load(os.path.join("images", "tie_fighter.png"))
# Laser
RED_LASER = pygame.image.load(os.path.join("images", "red_laser.png"))


# Creating the Tie Fighter class
class Tie_Fighter(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = TIE_FIGHTER
        self.laser_img = RED_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, movement):
        self.y += movement

    # Had to define this method because tie fighters were shooting off center
    # so to tie fighters shoot center of their ship i had to add +40 for lenght
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y+40, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
