# File: falcon_fighter.py
# Author: Steve Hommy
# Description: Main function

from millenium_falcon import Millenium_Falcon
from tie_fighter import Tie_Fighter
import pygame
import os
import random


pygame.font.init()


# Creating the screen
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Caption and icon
pygame.display.set_caption("FALCON FIGHTER")
ICON = pygame.image.load('images/star_wars.png')
pygame.display.set_icon(ICON)

# Loading images
# --------------------------------------------------------------------------------- #
# Background (scaling it to proper screen size)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images", "background.png")), (WIDTH, HEIGHT))


# Defining the collision with the two objects
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60
    level = 0
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 35)
    lose_font = pygame.font.SysFont("comicsans", 100)

    # At the start of the level there will be 6 tie fighters
    tie_fighters = []
    level_length = 6
    fighter_speed = 1

    # Millenium falcons movement speed and laser speed
    falcon_speed = 6
    laser_speed = 5

    # Millenium falcons startnin position
    millenium_falcon = Millenium_Falcon(370, 480)

    # Controlling game's framerate.
    clock = pygame.time.Clock()

    lose = False
    lose_count = 0

    # Labeling level and lives on screen. Choosing their placement on screen. Drawing tie fighter and millenium falcon on screen. If you lose the game popup the Game Over on the screen.
    def redraw_screen():
        SCREEN.blit(BACKGROUND, (0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))

        SCREEN.blit(level_label, (10, 10))
        SCREEN.blit(lives_label, (WIDTH - lives_label.get_width() - 10, 10))

        for tie_fighter in tie_fighters:
            tie_fighter.draw(SCREEN)

        millenium_falcon.draw(SCREEN)

        if lose:
            lose_label = lose_font.render("!Game Over!", 1, (255, 255, 255))
            SCREEN.blit(lose_label, (WIDTH/2 - lose_label.get_width()/2, 250))

        pygame.display.update()

    # Creating the main loop that runs the game
    while run:
        clock.tick(FPS)
        redraw_screen()

        if lives <= 0 or millenium_falcon.health <= 0:
            lose = True
            lose_count += 1

        if lose:
            if lose_count > FPS * 3:
                run = False
            else:
                continue

        # If level is completed add 6 more tie fighters to next level. Tie fighers spawns have been randomized
        if len(tie_fighters) == 0:
            level += 1
            level_length += 6
            for i in range(level_length):
                tie_fighter = Tie_Fighter(random.randrange(50, WIDTH-75), random.randrange(-2000, -100))
                tie_fighters.append(tie_fighter)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # These are the keybinds.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and millenium_falcon.x - falcon_speed > 15:  # Left movement and blocking it so it can't move off the screen
            millenium_falcon.x -= falcon_speed
        if keys[pygame.K_RIGHT] and millenium_falcon.x + falcon_speed + millenium_falcon.get_width() - 25 < WIDTH:  # Right movement and blocking it so it can't move off the screen
            millenium_falcon.x += falcon_speed
        if keys[pygame.K_UP] and millenium_falcon.y - falcon_speed > 0:  # Up movement and blocking it so it can't move off the screen
            millenium_falcon.y -= falcon_speed
        if keys[pygame.K_DOWN] and millenium_falcon.y + falcon_speed + millenium_falcon.get_height() + 5 < HEIGHT:  # Down movement and blocking it so it can't move off the screen
            millenium_falcon.y += falcon_speed
        if keys[pygame.K_SPACE]:  # Press space to shoot
            millenium_falcon.shoot()

        for tie_fighter in tie_fighters[:]:
            tie_fighter.move(fighter_speed)
            tie_fighter.laser_move(laser_speed, millenium_falcon)

            # Randomize tie fighters shooting time
            if random.randrange(0, 2*60) == 1:
                tie_fighter.shoot()

            if collide(tie_fighter, millenium_falcon):
                millenium_falcon.health -= 20
                tie_fighters.remove(tie_fighter)
            elif tie_fighter.y + tie_fighter.get_height() > HEIGHT:
                lives -= 1
                tie_fighters.remove(tie_fighter)

        millenium_falcon.laser_move(-laser_speed, tie_fighters)


# Defining the starting screen for the game
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        SCREEN.blit(BACKGROUND, (0, 0))
        title_label = title_font.render("CLICK MOUSEBUTTON TO BEGIN", 1, (255, 255, 255))
        SCREEN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        pygame.quit


main_menu()
