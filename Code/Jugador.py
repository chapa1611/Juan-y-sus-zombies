"""Este modulo almacena todo los atributos y metodos del jugador"""

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Constantes import *

class Juan(Sprite):
    def __init__(self, contenedor):
        super().__init__()
        self.puntos = 0            #los puntos que se generaran cuando pase por las tumbas (todavia no esta programado)
        self.vida = 3      #el personaje tendra 3 vidas (todavia no esta programado)
        self.contenedor = contenedor
        self.cont = 0
        self.cont2 = 0
        self.imagenes_derecha = jugador2  #referencia los sprites de cuando el personaje este caminando para la derecha, o cuando este quieto que es cuando esta caminando a la derecha por determinado en el mismo lugar
        self.imagenes_izquierda = jugador1 #referencia los sprites de cuando el personaje este caminando para la izq
        self.imagen = self.imagenes_derecha[self.cont] 
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(60, -130)    #donde va a aparecer el jugador
        self.rect.x %= self.contenedor[0] 
        self.rect.y %= self.contenedor[1]
        self.bolas = bola[self.cont2]  
        self.rect2 = self.bolas.get_rect()
        self.rect2.move_ip(130, -47)
        self.rect2.x %= self.contenedor[0]
        self.rect2.y %= self.contenedor[1]
        self.balas = pygame.sprite.Group()     #para la animacion de la bala, que ps seria que vaya girando xd(en este caso bolas de nieve xd)
        self.espadas = pygame.sprite.Group()  #la animacion de la espada, o slash como quieran llamarlo
        self.cooldown_bala = 0
        self.cooldown_espada = 0
        self.cooldown_time_bala = 5000       #cooldown pa que no parezca metralleta xd
        self.cooldown_time_espada = 2500  #cooldown pa que no se la pase spameando tanto xd
        self.last_shot_time_bala = 0
        self.last_shot_time_espada = 0

    def animar(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_RIGHT]:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_derecha[self.cont]       
            pygame.time.delay(100)            #se mueve con la flechita derecha y hace la animacion, modificando el tiempo provoca que vaya mas rapido o lenta la animacion xd
            if self.rect.x + self.rect.width < 800:
                self.rect.x += 5     #para que no se salga de la pantalla xd
        elif teclas[K_LEFT]:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_izquierda[self.cont] 
            pygame.time.delay(100) #lo mismo de arriba pero hacia la izq xd
            if self.rect.x > 0:
                self.rect.x -= 5  #para que no se salga de la pantalla x2 xd
        else:
            self.cont = (self.cont + 1) % 4
            self.imagen = self.imagenes_derecha[self.cont]
            pygame.time.delay(200)     #para hacer que cuando se quede quieto ps vaya avanzando en el mismo lugar por el hecho de que la pantalla se mueve xd
        if self.cooldown_bala > 0:
            self.cooldown_bala -= pygame.time.get_ticks() - self.last_shot_time_bala    
        else:       #aqui ps va incluido lo del cooldown de la bala xd, pa que funcione dicho cooldwon vaya xd
            self.cooldown_bala = 0    
        if teclas[K_z] and self.cooldown_bala <= 0:
            if self.imagen in self.imagenes_derecha:   #esto es que ps dispare con la z y que solo lo haga cuando se haya reseteado el cooldown xd
                nueva_bala = Bala(self.rect.right, self.rect.centery + 10, "right")
            else:                     #esto seria ps donde spawnea la bala, modificando los numeritos ps sale mas cerca del pj, o mas arriba etc.
                nueva_bala = Bala(self.rect.left, self.rect.centery + 10, "left")
            self.balas.add(nueva_bala)
            self.cooldown_bala = self.cooldown_time_bala       #y esto es para ir reseteando la bala en si xd
            self.last_shot_time_bala = pygame.time.get_ticks()
        if self.cooldown_espada > 0:
            self.cooldown_espada -= pygame.time.get_ticks() - self.last_shot_time_espada
        else:          #lo mismo que con la bala pero en este caso ps la espada
            self.cooldown_espada = 0    
        if teclas[K_x] and self.cooldown_espada <= 0:
            if self.imagen in self.imagenes_derecha:    #se usa con la x
                nueva_espada = Espada(self.rect.right, self.rect.centery + 10, "right")
            else:       #y tambien se pueden modificar estos numeros xd (los "10" que aparecen)
                nueva_espada = Espada(self.rect.left, self.rect.centery + 10, "left")
            self.espadas.add(nueva_espada)     #lo mismo que con la bala xd
            self.cooldown_espada = self.cooldown_time_espada
            self.last_shot_time_espada = pygame.time.get_ticks()
        self.balas.update()
        self.espadas.update()
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.images = bola            #aqui se carga ps las imagenes para la animacion de bala en si
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 10         #se le puede modificar la velocidad si quieren que la bala vaya mas lento o rapida segun sea el caso xd
        self.direction = direction     #esto es ps si el jugador la dispara ya sea mirando pa la derecha o izq xd
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50     #pa que se vea medianamente fluido xd

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):   #toda la parte de la animacion de la bala xd
                self.index = 0 
            self.image = self.images[self.index]
        if self.direction == "right":
            self.rect.x += self.velocidad
        else:            #esto ps es para cuando lo que les decia de si el jugador mira a la derecha o izq
            self.rect.x -= self.velocidad

        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()        #pa que la bala desaparezca si cruza los limites (pa que no se laguee luego luego de tantas balas por alla xd)
class Espada(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        if self.direction == "right":
            self.images = sword1
        else:              #lo mismo que con la bala pero con la espada
            self.images = sword2  #aunque en este caso ps se usaron 2 listas de imagenes pa la animacion xd
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 1    #pa que no parezca bala la wea xd (si se le pone un valor alto, ps es como si lo hubiera lanzado xd)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.life_time = 1000    #esto es para que parezca espada, ya que si no se le pone esto, ps es como si fuera una especie de bala invisible, que seguira avanzando hasta tocar el borde
        self.creation_time = pygame.time.get_ticks()
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.creation_time > self.life_time:
            self.kill()
        else:
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.index += 1
            if self.index >= len(self.images):            #toda la parte de la animacion de la espada
                self.kill()
            else:
                self.image = self.images[self.index]
            if self.direction == "right":
                self.rect.x += self.velocidad
            else:          #y aqui ps si es que el jugador mira pa la derecha o izquierda
                self.rect.x -= self.velocidad

            if self.rect.right < 0 or self.rect.left > 800:
                self.kill()   #para que no pueda matar zombies con la espada que todavia no han llegado a pantalla xd
    #Ahora bien, esto se uso ps para ir comprobando como iba quedando la wea, toncs
    #si por alguna razon algo no carga quizas se deban colocar algo de lo que hay aca xd
"""
import pygame
import sys
from Jugador import *
from Constantes import *

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    background_image = pygame.image.load("imagenes/negro.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption("Inserte titulo creativo xd")
    juanito = Juan(size)

    while 1:
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

if __name__ == "__main__":
    main()
"""