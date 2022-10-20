import pygame
import os


class img:
    def __init__(image):
        return pygame.image.load(image)

class input:
    def getkey(self, key):
        print()



class window:
    def __init__(self, w, h, resizeable):
        
        self.width = w
        self.height = h
        self.resizeable = False
        self.resizeable = resizeable
        
        if resizeable == True:
            self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        else:
            self.window = pygame.display.set_mode((self.width, self.height))
    
    def fill(self, r, g ,b):
        self.window.fill(tuple((r, g ,b)))
    
    def fillhex(self, color):
        self.window.fill(tuple((int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))))
    
    
    def set(self, w, h):
        self.width = w
        self.height = h
        
    def getscreen(self):
        return (self.w, self.h)
    
    def get(self, input):
        if input == "w":
            return self.width
        
        elif input == "h":
            return self.height
        
    def setTitle(self, title):
        pygame.display.set_caption(title)
        
    def setImg(self, image):
        pygame.display.set_icon(img(image))
