import pygame

class img:
    def __init__(image):
        return pygame.image.load(image)

class input:
    def getkey(self, key):
        print()



class screen:
    def __init__(self, w, h, resizeable):
        self.width = w
        self.height = h
        self.resizeable = False
        self.resizeable = resizeable
        if resizeable == True:
            self = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        else:
            self = pygame.display.set_mode((w, h), pygame.RESIZABLE)
    
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
        pygame.display.set_icon(img(image))
