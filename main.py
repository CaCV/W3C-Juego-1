# -*- coding: utf-8 -*-
"""
Created on Mon May 08 19:39:46 2017

@author: Carlos
"""

import pygame, sys
from pygame import *

pygame.init()

#Variables para pantalla
display_width = 640
display_height = 480

#Colores en RGB
negro = (0,0,0)
blanco = (255,255,255)



def load_image(filename,transparent=False):    
    #	Intentamos	cargar	la	imagen,	si	no	se	puede	
    #	lanzamos	un	mensaje	de	error.	
    try:    image = pygame.image.load(filename)	
    except pygame.error, message:
        raise SystemExit, message
    #	Convertimos	la	imagen	al	tipo	interno	de	
    #	Pygame	que	hace	que	sea	mucho	más	eficiente.	
    image =  image.convert()	
    #	Si	la	imagen	es	transparente,	tomamos	el		
    #	color	de	su	esquina	superior	izquierda	y	lo	
    #	definimos	como	color	transparente	de	la	imagen.	
    if transparent:	
        color=image.get_at((0,0))
        image.set_colorkey(color , RLEACCEL)	
    return image
	
		
		
		
		#Clase cursor 
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
       #clase boton 
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)
	


def main():

	#Inicia pantalla declarando ancho y alto
	pantalla = pygame.display.set_mode((display_width,display_height))
	#Mensaje en ventana
	pygame.display.set_caption("Prototipo2 Fastclick")
	
	#Variable clock para el tiempo por frame
	clock	= pygame.time.Clock()
	
	
	#Carga de musica de fondo
	pygame.mixer.music.load("temaprincipal.mp3")
	
	#Reproduce de manera infinita el tema
	pygame.mixer.music.play(-1, 0.0)
	
	
	#botones
	jugar=pygame.image.load("jugar.png")
	jugar1=pygame.image.load("jugar1.png")
	boton1=Boton(jugar,jugar1,(display_width / 2) - 85, (display_height / 4))
	boton2=Boton(jugar,jugar1,(display_width / 2) - 85, (display_height / 2))
	boton3=Boton(jugar,jugar1,(display_width / 2) - 85, 3*(display_height / 4))
	cursor1=Cursor()
	cursor2=Cursor()	
	cursor3=Cursor()
	
	while True:
		
		#Dibujamos la pantalla de blanco
		pantalla.fill(blanco)
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		cursor1.update()
		cursor2.update()
		cursor3.update()
		
		boton1.update(pantalla,cursor1)
		boton2.update(pantalla,cursor2)
		boton3.update(pantalla,cursor3)
		pygame.display.flip()
		
	return 0

if __name__ == "__main__":
	pygame.init()
	main()