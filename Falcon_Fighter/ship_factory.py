# File: ship_factory.py
# Author: Steve Hommy
# Description: creating Ship class

from laser import Laser

HEIGHT = 600


# Creating the structer of the ships class
class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    # draw laser and with -24 I am centering it, otherwise it will shoot left side of the falcon
    def draw(self, screen):
        screen.blit(self.ship_img, (self.x-24, self.y))
        for laser in self.lasers:
            laser.draw(screen)

    # Implementing the movement of the laser and when the laser hits the player the player loses 20hp
    def laser_move(self, movement, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(movement)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 20
                self.lasers.remove(laser)

    # Implementing the cooldown method so you can't shoot rapidly
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    # Implementing shoot method
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
