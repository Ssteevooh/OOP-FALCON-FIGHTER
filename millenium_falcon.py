# File: millenium_falcon.py
# Author: Steve Hommy
# Description: Millenium falcon class and inheriting Ship class

from ship_factory import Ship
import pygame
import os


HEIGHT = 600
# Millenium falcon
MILLENIUM_FALCON = pygame.image.load(os.path.join("images", "millenium_falcon.png"))
# Laser
BLUE_LASER = pygame.image.load(os.path.join("images", "blue_laser.png"))


# Creating the Millenium Falcon class
class Millenium_Falcon(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = MILLENIUM_FALCON
        self.laser_img = BLUE_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def laser_move(self, movement, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(movement)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # Overwriting the method from the subclass Ship(draw) and called it with super and calling the healthbar so it will display healthbar
    def draw(self, screen):
        super().draw(screen)
        self.healthbar(screen)

    def healthbar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x - 23, self.y + self.ship_img.get_height() + 2, self.ship_img.get_width(), 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.x - 23, self.y + self.ship_img.get_height() + 2, self.ship_img.get_width() * (self.health/self.max_health), 5))
