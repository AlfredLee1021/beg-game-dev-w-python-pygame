import pygame.math as math

A = math.Vector2(10.0, 20.0)
B = math.Vector2(30.0, 35.0)
AB = B - A
print ("Vector AB is", AB)
print ("AB * 2 is", AB * 2)
print ("AB / 2 is", AB / 2)
print ("AB + (-10, 5) is", AB + (-10, 5))
print ("Magnitude of AB is", AB.length())
print ("AB normalized is", math.Vector2(AB.x/AB.length(), AB.y/AB.length()))