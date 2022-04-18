# File: laser.py
# Author: Steve Hommy
# Description: Laser class

import pygame


# Here we are returning collision of two objects and asking that is object 1 overlaping object 2 with offset of (x, y) if not retrun None
# So if laser hits an object return True
# Had to subtract -20 of the width otherwise it would not hit left side of the tie fighter
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x - 20
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


# Creating the laser class
class Laser:
    def __init__(self, x, y, laser_img):
        self.x = x
        self.y = y
        self.laser_img = laser_img
        self.mask = pygame.mask.from_surface(self.laser_img)

    def draw(self, screen):
        screen.blit(self.laser_img, (self.x, self.y))

    def move(self, movement):
        self.y += movement

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    # Returning the value of collide function
    def collision(self, obj):
        return collide(self, obj)
