# -*- coding: utf-8 -*-

"""
Created on Wed April
@author: W3C Games factory
"""

import pygame

import os
import sys
import random


#Constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "F:\ARCHIVOS PROYECT\PRESENTACION 1\Prototipo1\imagenes"

lista_imagenes = ["gato1.png","gato2.jpg","pelota1.jpg","pelota2.jpg","perro1.png",
                  "perro2.jpg","pez.jpg","pez1.jpg","triangulo1.png","triangulo2.jpg"]



#Fuentes y texto



                   
#Clases y funciones

def load_image(nombre, dir_imagen, alpha = False):

    #Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen,nombre)

    try:
        image= pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + str(ruta))
        sys.exit(1)

    #Comprobar si la imagen tiene canal "alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image



class cursor(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)   

    def update(self):
        self.left , self.top = pygame.mouse.get_pos()

class boton(pygame.sprite.Sprite):

    def __init__(self, imagen, x=35 , y=380):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen ,IMG_DIR,alpha = True)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (x,y)


        
        
        
class Cuadro (pygame.sprite.Sprite):

    "Cuadro que contendra la imagen"

    def __init__ (self , imagen , coordenadax):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen, IMG_DIR, alpha = True)
        self.rect = self.image.get_rect()
        self.rect.centerx = coordenadax
        self.rect.centery = SCREEN_HEIGHT / 2

    def update(self):
        x=random.randint(0,9)
        self.image = load_image(lista_imagenes[x], IMG_DIR, alpha = True)
       
        
        
#Funcion principal del juego

def main():

    pygame.init()
    pygame.mixer.init()

    #Creamos la ventana e indicamos titulo
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    pygame.display.set_caption("Prototipo1")

    #Cargar objetos
    fondo = load_image("fondo.png",IMG_DIR, alpha = True)


    #Crear los dos objetos tipo Cuadro
    imagen1 = Cuadro (lista_imagenes[0],150)
    imagen2 = Cuadro (lista_imagenes[2],SCREEN_WIDTH - 150)



    #Sincronizacion
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1,25) #Activa repeticion teclas

    
    cursor1 = cursor()
    boton1 = boton("boton.png")
    boton2 = boton("boton2.png",350,380)

    #Bucle principal
    done = True

    while done:

        clock.tick(60)

        cursor1.update()

        pos_mouse = pygame.mouse.get_pos()
        mov_mouse = pygame.mouse.get_rel()

        #Salir
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    imagen1.update()
                    imagen2.update()
                elif event.key == K_DOWN:
                    imagen1.update()
                    imagen2.update()
            
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.K_ESCAPE:
                done = False
            

        #Actualizar pantalla
        screen.blit(fondo, (0,0))
        
        todos = pygame.sprite.RenderPlain(imagen1, imagen2, boton1, boton2)
        todos.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()










        















    










    










        




















        




