"""Este modulo almacena todo los atributos y metodos del jugador"""

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Constantes import *

class Juan(Sprite):
    def __init__(self, contenedor):
        super().__init__()
        self.puntos = 0
        self.vida = 3
        self.angulo = 0
        self.contenedor = contenedor
        self.cont = 0
        self.cont2 = 0
        self.imagenes_derecha = jugador2
        self.imagenes_izquierda = jugador1
        self.imagen = self.imagenes_derecha[self.cont]
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(60, -130)
        self.rect.x %= self.contenedor[0]
        self.rect.y %= self.contenedor[1]
        self.bolas = bola[self.cont2]
        self.rect2 = self.bolas.get_rect()
        self.rect2.move_ip(130, -47)
        self.rect2.x %= self.contenedor[0]
        self.rect2.y %= self.contenedor[1]
        self.balas = pygame.sprite.Group()
        self.espadas = pygame.sprite.Group()
        self.cooldown_bala = 0
        self.cooldown_espada = 0
        self.cooldown_time_bala = 5000
        self.cooldown_time_espada = 2500
        self.last_shot_time_bala = 0
        self.last_shot_time_espada = 0

    def animar(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_RIGHT]:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_derecha[self.cont]
            pygame.time.delay(100)
            if self.rect.x + self.rect.width < 800:
                self.rect.x += 5
        elif teclas[K_LEFT]:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_izquierda[self.cont]
            pygame.time.delay(100)
            if self.rect.x > 0:
                self.rect.x -= 5
        else:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_derecha[self.cont]
            pygame.time.delay(200)
        if self.cooldown_bala > 0:
            self.cooldown_bala -= pygame.time.get_ticks() - self.last_shot_time_bala
        else:
            self.cooldown_bala = 0    
        if teclas[K_z] and self.cooldown_bala <= 0:
            if self.imagen in self.imagenes_derecha:
                nueva_bala = Bala(self.rect.right, self.rect.centery + 10, "right")
            else:
                nueva_bala = Bala(self.rect.left, self.rect.centery + 10, "left")
            self.balas.add(nueva_bala)
            self.cooldown_bala = self.cooldown_time_bala
            self.last_shot_time_bala = pygame.time.get_ticks()
        if self.cooldown_espada > 0:
            self.cooldown_espada -= pygame.time.get_ticks() - self.last_shot_time_espada
        else:
            self.cooldown_espada = 0    
        if teclas[K_x] and self.cooldown_espada <= 0:
            if self.imagen in self.imagenes_derecha:
                nueva_espada = Espada(self.rect.right, self.rect.centery + 10, "right")
            else:
                nueva_espada = Espada(self.rect.left, self.rect.centery + 10, "left")
            self.espadas.add(nueva_espada)
            self.cooldown_espada = self.cooldown_time_espada
            self.last_shot_time_espada = pygame.time.get_ticks()
        self.balas.update()
        self.espadas.update()
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.images = bola
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 10
        self.direction = direction
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        if self.direction == "right":
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad

        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
class Espada(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        if self.direction == "right":
            self.images = sword1
        else:
            self.images = sword2
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 1
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.life_time = 1000
        self.creation_time = pygame.time.get_ticks()
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.creation_time > self.life_time:
            self.kill()
        else:
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.index += 1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]
            if self.direction == "right":
                self.rect.x += self.velocidad
            else:
                self.rect.x -= self.velocidad

            if self.rect.right < 0 or self.rect.left > 800:
                self.kill()