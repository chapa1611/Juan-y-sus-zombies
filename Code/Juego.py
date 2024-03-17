

from Constantes import *
from Jugador import *
from Pantalla import *
#from Tumbas import *
from Zombies import *

import pygame 
import sys
import random
from pygame.sprite import Sprite


juanito = Juan(Tamaño_pantalla)
while 1:
    display()
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    sys.exit()
    juanito.animar()
    screen.blit(background_image, background_rect)
    screen.blit(juanito.imagen, juanito.rect)
    juanito.balas.draw(screen)
    juanito.espadas.draw(screen)

    pygame.display.update()
    pygame.time.delay(10)

