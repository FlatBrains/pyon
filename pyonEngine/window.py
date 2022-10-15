import pygame
from classes import *

#screen = screen(1920, 1080, False)
WINDOW = pygame.display.set_mode((500, 500))
WINDOW.fill((0, 128, 128))
run = True
pygame.display.set_caption("Your Mom")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
    
    pygame.display.update()