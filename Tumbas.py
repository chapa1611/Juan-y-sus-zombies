
import sys 
import pygame 
import random
from pygame.sprite import Sprite

class Tumbas(Sprite):
    def __init__(self,contenedor):
        Sprite.__init__(self)
        self.contenedor = contenedor
        self.base_image = pygame.image.load("Tumbas.jpg")
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.velocidad = [-1,0]
        self.rect.x = size[0]-100#random.randint(0,contenedor[0]-50)
        self.rect.y = 300

    def move(self): 
          self.velocidad[0] *= 1
          self.rect = self.rect.move(self.velocidad) 
        

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
tumbas = Tumbas(size)
pygame.init()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()               
    screen.blit(tumbas.image, tumbas.rect)
    tumbas.move()
    pygame.display.update()
    pygame.display.clear()
    pygame.time.delay(10)
