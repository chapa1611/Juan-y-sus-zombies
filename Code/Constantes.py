"""Este modulo se encarga de almacenar todos los valores fundamentales que se usaran en el resto del codigo como son las imagenes, sonido y valores"""

import pygame 

Tamaño_pantalla = Ancho, Altura = 942, 490


jugador1 = [
    pygame.image.load("../imagenes/Juaniz1.png"),
    pygame.image.load("../imagenes/Juaniz2.png"),
    pygame.image.load("../imagenes/Juaniz3.png"),     #animacion pa cuando camine pa la derecha xd
    pygame.image.load("../imagenes/Juaniz2.png")
]
jugador2 = [
    pygame.image.load("../imagenes/Juan1.png"),
    pygame.image.load("../imagenes/Juan2.png"),     #animacion pa la izq
    pygame.image.load("../imagenes/Juan3.png"),
    pygame.image.load("../imagenes/Juan2.png")
]
bola = [
    pygame.image.load("../imagenes/bola.png"),
    pygame.image.load("../imagenes/bola (1).png"),
    pygame.image.load("../imagenes/bola (2).png"),  #animacion de la bolita de nieve que seria la bala xd
    pygame.image.load("../imagenes/bola (3).png")
]
sword1=[
    pygame.image.load("../imagenes/sword1.png"),
    pygame.image.load("../imagenes/sword2.png"),
    pygame.image.load("../imagenes/sword3.png"),     #animacion cuando se use la espada cuando el pj este mirando pa la der xd
    pygame.image.load("../imagenes/sword4.png"),
    pygame.image.load("../imagenes/sword5.png"),
    pygame.image.load("../imagenes/sword6.png")
]
sword2=[
    pygame.image.load("../imagenes/swordiz1.png"),
    pygame.image.load("../imagenes/swordiz2.png"), #animacion cuando se use la espada cuando el pj este mirando pa la izq xd
    pygame.image.load("../imagenes/swordiz3.png"),
    pygame.image.load("../imagenes/swordiz4.png"),
    pygame.image.load("../imagenes/swordiz5.png"),
    pygame.image.load("../imagenes/swordiz6.png")
]
