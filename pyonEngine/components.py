from  pyonEngine.window import *
from pyonEngine.color import *

import pygame

class transform:
    def __init__(self, x, y, w, h, velx, vely, rot):
        self.x = x
        self.y = y
        
        self.width = w
        self.height = h
        
        self.velx = velx
        self.vely = vely
        
        self.rotation = rot
        self.gravity = 1
    
    def physics(self):
        self.vely += self.gravity
        self.x += self.velx
        self.y += self.vely
        
        

class renderer:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        
    def renderCol(self):
        pygame.draw.rect(WINDOW, white, self.rect)