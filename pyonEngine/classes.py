import pygame

class input:
    def getkey(self, key):
        print()

class Screen:
    def __init__(self, w, h):
        if w is None:
            self.width = 1920
        else:
            self.width = w
            
        if h is None:
            self.height = 1080
        else:
            self.height = h
    
    def set(self, w, h):
        self.width = w
        self.height = h
        
    def getscreen(self):
        return (self.w, self.h)
    
    def get(self, input):
        if input == self.w:
            return self.w
        
        elif input == self.y:
            return self.h
        
    def setTitle(self, title):
        pygame.display.set_caption(title)
        
    def setImg(self, image):
        pygame.display.set_icon()