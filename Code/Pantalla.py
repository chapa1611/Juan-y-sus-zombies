
import pygame
from pygame.locals import *
import sys
from Jugador import *
from Constantes import *

size=width, height=800, 600
screen=pygame.display.set_mode(size)

def main():
    pygame.init()
    background_image=pygame.image.load("imagenes/negro.jpg")
    background_rect=background_image.get_rect()
    pygame.display.set_caption("Inserte titulo creativo xd")
    juan=Juan(size)

    while 1:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
        
        Jugador.animar()

        screen.blit(background_image, background_rect)
        screen.blit(juan.imagen, juan.rect)
        pygame.display.update()
        pygame.time.delay(10)

if __name__=="__main__":
    main()
