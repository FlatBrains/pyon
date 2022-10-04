from ...pyon.Main import *
from pyonEngine.window import *

import pygame
import sys

FPSCap = 60
clock = pygame.time.Clock()

start()

class input:
    def getkey(self, key):
        print()

while True:
    clock.tick(FPSCap)
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.update()
    