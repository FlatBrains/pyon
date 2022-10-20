from pyonEngine import *
from pyonEngine.window import *
from main import update, start

import pygame
import sys

x = 0
y = 0

FPSCap = 60
tick = 0
clock = pygame.time.Clock()

start()

while True:
    clock.tick(FPSCap)
    tick = 1 + tick
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    
    pygame.display.update()    