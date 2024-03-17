import sys 
import pygame 
import random
import time
from pygame.sprite import Sprite

class Tumbas(Sprite):
    def __init__(self,contenedor):
        Sprite.__init__(self)
        self.contenedor = contenedor
        self.base_image = pygame.image.load("Tumbas.jpg")
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.velocidad = 50
        self.rect.x = size[0] + 236
        self.rect.y = 300

    def update(self): 

          self.rect.x -= self.velocidad
          if self.rect.x + 236 < 0: #236 es el ancho de la imagen de referencia
            self.rect.x = size[0] + 236
          self.mano()
         
         
    def mano(self):
        if self.rect.x <= size[0]:
            num = random.randint(1,5)
            pygame.time.wait(400) 
            if num == 5:
                self.image = pygame.image.load("Tumbasmano.jpg")
            else: 
                self.image = pygame.image.load("Tumbas.jpg")
    
 """   def detectar(self, rect):
        for t in range(self.rect.bottomleft, self.rect.topleft):
            if t == rect.left or t == rect.right:
                print('choque')"""
        

    
 """           
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
tumbas = Tumbas(size)

pygame.init()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit() 
    screen.fill((0,0,0))
    
    tumbas.update() 
             
    screen.blit(tumbas.image, tumbas.rect)
    screen.blit(tumbe.image, tumbe.rect)
    pygame.display.update()
 
    pygame.time.delay(10)"""