# -*- coding: utf-8 -*-
"""
Created on Mon May 08 21:47:54 2017

@author: Carlos
"""

import pygame
from pygame.locals import *
import os
import sys


#colores
azul = ( 0, 0, 255)
blanco= ( 255, 255, 255)
negro= ( 0, 0, 0)
verde= ( 0, 255, 0)
amarillo= ( 255, 255, 0)

       #clase cursor 
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

       #clase boton 
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
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
    pygame.init()
    
    #botones
    jugar=pygame.image.load("jugar.png")
    jugar1=pygame.image.load("jugar1.png")
    botonjugar=Boton(jugar,jugar1)
    cursor1=Cursor()
    
    
    #pantalla dimensiones
    
    ancho =500
    alto =400
    
    pantalla = pygame.display.set_mode((ancho, alto))

    pygame.display.set_caption('Fast Click')

    reloj=pygame.time.Clock()

    salir=False
    while salir!=True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
             
        reloj.tick(20)#20 fps
        cursor1.update()
        pantalla.fill(blanco)
        
        botonjugar.update(pantalla,cursor1)
        
        pygame.display.update()
        
    pygame.quit()

main()
    