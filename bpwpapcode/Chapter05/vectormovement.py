background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
import pygame.math as math

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = math.Vector2(100.0, 100.0)
heading = math.Vector2()

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
                    
    
    screen.blit(background, (0,0))
    screen.blit(sprite, position)
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    destination = math.Vector2(pygame.mouse.get_pos()) - math.Vector2(sprite.get_size())/2
    vector_to_mouse = destination - position
    vector_to_mouse = vector_to_mouse.normalize()
    heading = heading + vector_to_mouse    
    
    position += heading * time_passed_seconds

    pygame.display.update()
    