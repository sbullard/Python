#pygame games vid series vid 2 - sentdex username

import pygame #imports pygame module
import sys
from pygame.locals import *

pygame.init() #initializes pygame
setDisplay = pygame.display.set_mode((400,300)) #sets screen size
pygame.display.set_caption('this title sucks')  #sets game title

#game loop
while True:
    for event in pygame.event.get(): #gets all events that happen
        print event #way to debug and see event coordinates and actions debugging
        if event.type == QUIT: #when user clicks window exit button, then exits game             

    pygame.display.update()
