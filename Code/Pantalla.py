import pygame
import sys

size = width, height = 900, 490
screen = pygame.display.set_mode(size)


def main():
	pygame.init()

	background_image = pygame.image.load("imagenes/fondo.jpg")
	background_rect = background_image.get_rect() #Se forma el rectangulo del fondo 

	pygame.display.set_caption("Zombies") #Titulo del juego cuando se ejecuta

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.blit(background_image, background_rect)
		pygame.display.update()


if __name__ == '__main__': 
	main()