

from Constantes import *
from Jugador import *
from Pantalla import *
#from Tumbas import *
from Zombies import *

import pygame 
import sys
import random
from pygame.sprite import Sprite

def main():
  pygame.init()
  background_image = pygame.image.load("../imagenes/fondo.jpg").convert()  
  screen = pygame.display.set_mode(Tamaño_pantalla)
  juanito = Juan(Tamaño_pantalla)
  zombies = []
  x = 0
  while 1:

      for event in pygame.event.get():
  	    if event.type == pygame.QUIT:
  		    sys.exit()
      x_relativa = x % background_image.get_rect().width
      screen.blit(background_image, (x_relativa -
                    background_image.get_rect().width, 0))
      if x_relativa < Tamaño_pantalla[0]:
            screen.blit(background_image, (x_relativa, 0))
      x -= 1
      RELOJ.tick(FPS)

      juanito.animar()
      screen.blit(juanito.imagen, juanito.rect)
      juanito.balas.draw(screen)
      juanito.espadas.draw(screen)
      si(juanito,zombies)
   
      pygame.display.update()
      pygame.time.delay(10)

if __name__ == "__main__":
    main()