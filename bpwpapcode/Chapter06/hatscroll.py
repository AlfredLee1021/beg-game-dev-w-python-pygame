picture_file = 'cat.jpg'

import pygame
from pygame.locals import *
from sys import exit
from pygame.math import Vector2


pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

picture = pygame.image.load(picture_file)
picture_pos = Vector2(0, 0)
scroll_speed = 1000.

clock = pygame.time.Clock()

joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

if joystick is None:
    print ("Sorry, you need a joystick for this!")
    exit()

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    scroll_direction = Vector2(*joystick.get_hat(0))    
    scroll_direction.normalize()    
                
    screen.fill((255, 255, 255))
    screen.blit(picture, (-picture_pos.x, picture_pos.y))    
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    picture_pos += scroll_direction * scroll_speed * time_passed_seconds    
    
    pygame.display.update()    
