picture_file = 'cat.jpg'

import pygame
from pygame.locals import *
from sys import exit
from pygame.math import Vector2


pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

picture = pygame.image.load(picture_file).convert()
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
    
    scroll_direction = Vector2(0, 0)
    if joystick.get_numhats() > 0:
        scroll_direction = Vector2(*joystick.get_hat(0))    
        scroll_direction.normalize()

    analogue_scroll = Vector2(0, 0)
    if joystick.get_numaxes() >= 2:
        axis_x = joystick.get_axis(0)
        axis_y = joystick.get_axis(1)        
        analogue_scroll = Vector2(axis_x, -axis_y)        
        analogue_scroll *= scroll_speed
                
    screen.fill((255, 255, 255))
    screen.blit(picture, (-picture_pos.x, picture_pos.y))    
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    picture_pos += scroll_direction * scroll_speed * time_passed_seconds    
    picture_pos += analogue_scroll * time_passed_seconds  
    
    pygame.display.update()    
