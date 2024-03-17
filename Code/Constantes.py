"""Este modulo se encarga de almacenar todos los valores fundamentales que se usaran en el resto del codigo como son las imagenes, sonido y valores"""

import pygame

Tamaño_pantalla = ancho, altura = 800, 600

#imagenes
#POR CIERTO, si por alguna razon les genera error de las imagenes, pueden usar pwd en la terminal pa mirar donde estan parados, y de ahi usar el cd ./para ir una carpeta mas o una menos
#o simplemente lo agregan la direccion en las imagenes (lo digo por que en algunos computadores, por alguna razon era necesario salirse de las carpetas, dejarlo tal cual, o meterse a otras; pa encontrar la imagen xd)
jugador1 = [
    pygame.image.load("imagenes/Juaniz1.png"),
    pygame.image.load("imagenes/Juaniz2.png"),
    pygame.image.load("imagenes/Juaniz3.png"),     #animacion pa cuando camine pa la derecha xd
    pygame.image.load("imagenes/Juaniz2.png")
]
jugador2 = [
    pygame.image.load("imagenes/Juan1.png"),
    pygame.image.load("imagenes/Juan2.png"),     #animacion pa la izq
    pygame.image.load("imagenes/Juan3.png"),
    pygame.image.load("imagenes/Juan2.png")
]
bola = [
    pygame.image.load("imagenes/bola.png"),
    pygame.image.load("imagenes/bola (1).png"),
    pygame.image.load("imagenes/bola (2).png"),  #animacion de la bolita de nieve que seria la bala xd
    pygame.image.load("imagenes/bola (3).png")
]
sword1=[
    pygame.image.load("imagenes/sword1.png"),
    pygame.image.load("imagenes/sword2.png"),
    pygame.image.load("imagenes/sword3.png"),     #animacion cuando se use la espada cuando el pj este mirando pa la der xd
    pygame.image.load("imagenes/sword4.png"),
    pygame.image.load("imagenes/sword5.png"),
    pygame.image.load("imagenes/sword6.png")
]
sword2=[
    pygame.image.load("imagenes/swordiz1.png"),
    pygame.image.load("imagenes/swordiz2.png"), #animacion cuando se use la espada cuando el pj este mirando pa la izq xd
    pygame.image.load("imagenes/swordiz3.png"),
    pygame.image.load("imagenes/swordiz4.png"),
    pygame.image.load("imagenes/swordiz5.png"),
    pygame.image.load("imagenes/swordiz6.png")
]
"""Imagen_zombie = null
Imagen_tumba = null
Fondo_inicio = null
Fondo_juego = null
Fondo_fin_juego = null"""



