# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:09:09 2021

@author: robin
"""

import pygame
import cv2
import numpy
import time

pygame.init()


W,H = 1280,720
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
done = False

pygame.display.set_caption("ELECTROMAG")
icono = pygame.image.load("assets/neutron.png")
pygame.display.set_icon(icono)

portada=tablero = pygame.image.load("assets/portada.png").convert()
tablero = pygame.image.load("assets/tablero.png").convert()


boton1a=pygame.image.load('botones/boton_0.png').convert_alpha()
boton1b=pygame.image.load('botones/boton_1.png').convert_alpha()


#Colores
black = (0, 0, 0)

## musica
musica1 = pygame.mixer.music.load("musica1.ogg")
musica1 = pygame.mixer.music.play(-1)

#video1 = pygame.movie.Movie("cat.MP4")
#video1_screen = pygame.Surface(movie.get_size()).convert()
#video1.set_display(video_screen)
#video1.play()

UI = pygame.image.load('botones/margenes.png').convert_alpha()

parent = None
timer_sec = 60
grab = False

#aprobados = {nivel_1:0, nivel_2:0, nivel_3:0, nive_4:0, nivel_5:0}

def mouseover(imagen,coordenadas):
  mouse=False
  y,x,_ = cv2.imread(imagen).shape
  mx,my = pygame.mouse.get_pos()
  tx,ty=coordenadas[0],coordenadas[1]
  if tx+x>mx>tx:
    if ty+y>my>ty:      
      mouse=True
  #print(coordenadas,x,y,imagen)
  return mouse
    
class Boton():

  def __init__(self,tipo,imagen,coordenadas):
    self.mouse=False
    self.tipo=tipo
    self.coordenadas=coordenadas
    self.ima = pygame.image.load("botones/boton_1.png").convert_alpha()
    if self.tipo=='jugar':
      mouse1=mouseover(imagen,coordenadas)
      if mouse1==True:
        self.ima = pygame.image.load("botones/boton_1.png").convert_alpha()
        self.mouse=True
      if mouse1==False:
        self.ima = pygame.image.load("botones/boton_0.png").convert_alpha()
        self.mouse=False

    if self.tipo=='nivel':
      mouse2=mouseover(imagen,coordenadas)
      if mouse2==True:
        self.ima = pygame.image.load("botones/niveles_1.png").convert_alpha()
        self.mouse=True
      if mouse2==False:
        self.ima = pygame.image.load("botones/niveles_0.png").convert_alpha()
        self.mouse=False
        
    if self.tipo=='pausa':
      mouse3=mouseover(imagen,coordenadas)
      if mouse3==True:
        self.ima = pygame.image.load("botones/pausa_1.png").convert_alpha()
        self.mouse=True
      if mouse3==False:
        self.ima = pygame.image.load("botones/pausa_0.png").convert_alpha()
        self.mouse=False
        
    if self.tipo=='info':
      mouse4=mouseover(imagen,coordenadas)
      if mouse4==True:
        self.ima = pygame.image.load("botones/info_1.png").convert_alpha()
        self.mouse=True
      if mouse4==False:
        self.ima = pygame.image.load("botones/info_0.png").convert_alpha()
        self.mouse=False

class Objeto(pygame.sprite.Sprite):
  def __init__(self, nombre):
    super().__init__()
    self.image = pygame.image.load("proton.png").convert_alpha()
    self.nombre = nombre
    if nombre == "positivo":
        self.image = pygame.image.load("proton.png").convert_alpha()
        
    elif nombre == "negativo":
        self.image = pygame.image.load("electron.png").convert_alpha()
            
    elif nombre == "neutro":
        self.image = pygame.image.load("neutron.png").convert_alpha()
            
    elif nombre == "maquina":
        self.image = pygame.image.load("maquina.png").convert_alpha()
        
    elif nombre == "personaje":
        self.image = pygame.image.load("personaje.png").convert_alpha()

        self.rect = self.image.get_rect()


class Casilla(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.objeto = Objeto("")
        self.posX = posX
        self.posY = posY
        self.tieneJugador = False
        
class Tablero():
    def __init__(self):
        super().__init__()
        self.matriz = []
        self.iniX = 390
        self.iniY = 110

        for i in range(8):
            self.matriz.append([])
            for j in range(8):
                self.matriz[i].append(
                    Casilla(self.iniX + (i * 64), self.iniY + (j * 64)))

        self.matriz[0][0].tieneJugador = True

        self.matriz[3][3].objeto = Objeto("positivo")
        self.matriz[6][3].objeto = Objeto("negativo")
        self.matriz[2][6].objeto = Objeto("maquina")

#Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("personaje.png").convert_alpha()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.currentX = 0
        self.currentY = 0
        
    def change_speed(self, x, y):
        self.currentX = self.speed_x
        self.currentY = self.speed_y
        if self.speed_y==0 and y == -1:
          return   
        if self.speed_x==0 and x == -1:
          return
        if self.speed_y==7 and y == 1:
          return
        if self.speed_x==7 and x == 1:
          return
        self.speed_x += x
        self.speed_y += y

    ''''
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    '''
    
    def setPos(self, posX, posY):
        self.rect.x = posX
        self.rect.y = posY
        playerposition=[posX,posY]
     
x = 0
fondo1 = pygame.image.load("fondo.png").convert() 
fondo2 = pygame.image.load("fondo2.png").convert()
fondo3 = pygame.image.load("fondo3.png").convert()
fondo4 = pygame.image.load("fondo4.png").convert()
fondo5 = pygame.image.load("fondo5.png").convert()
lista_fondos = [fondo1,fondo2,fondo3,fondo4,fondo5]

FPS = 15

class Gamestate():
  def __init__(self):
    self.state='intro'

  def cambia_nivel(self):
    if self.state=='intro':
      self.intro()
    if self.state=='menu_pausa':
      self.menu_pausa()
    if self.state=='menu_info':
      self.menu_info()
    if self.state=='niveles':
      self.niveles()
    if self.state=='nivel_1':
      self.nivel_1()
    if self.state=='nivel_2':
      self.nivel_2()
    if self.state=='nivel_3':
      self.nivel_3()
    if self.state=='nivel_4':
      self.nivel_4()
    if self.state=='nivel_5':
      self.nivel_5()

  def intro(self):
    coorxy=[640-152,420-32]
    coorxy2=[640-152,420+50]
    boton1=Boton('jugar','boton_0.png',coorxy)
    imagenboton1=boton1.ima
    boton2=Boton('nivel','boton_0.png',coorxy2)
    imagenboton2=boton2.ima
    screen.blit(portada, [0, 0])
    screen.blit(imagenboton1,coorxy)
    screen.blit(imagenboton2,coorxy2)

    if event.type==pygame.MOUSEBUTTONDOWN:
        if boton1.mouse==True:
           self.state='nivel_1'
           
    if event.type==pygame.MOUSEBUTTONDOWN:
        if boton2.mouse==True:
           self.state='niveles'
            

    #all_sprites_list.draw(screen)

    pygame.display.flip()
  def menu_pausa(self):
      screen.blit(fondo3,[0,0])
      
      pygame.display.flip()
  def menu_info(self):
      screen.blit(fondo4,[0,0])
      
      pygame.display.flip()
  def niveles(self):
      coorxy=[640-152,420-32]
      coorxy2=[640-152,420+50]
      boton1=Boton('jugar','boton_0.png',coorxy)
      imagenboton1=boton1.ima
      
      screen.blit(fondo4, [0, 0])
      screen.blit(imagenboton1,coorxy)
      #screen.blit(imagenboton2,coorxy2)
      pygame.display.flip()
  
  
  def nivel_1(self):
      x = 0
      fondo = pygame.image.load("fondo.png").convert() 
      screen.blit(fondo,(x,0))
      x_a = x % fondo.get_rect().width
      screen.blit(fondo, (x_a - fondo.get_rect().width ,0))
      if x_a < W:
          screen.blit(fondo,(x_a,0))
          screen.blit(tablero, [390,110])
      x -= 2
      screen.blit(UI,[0,0])
      
      coorxy=[8,8]
      coorxy2=[0,575]
      boton3=Boton('pausa','pausa_0.png',coorxy)
      imagenboton3=boton3.ima
      screen.blit(imagenboton3,coorxy)
      boton4=Boton('info','info_0.png',coorxy2)
      imagenboton4=boton4.ima
      screen.blit(imagenboton4,coorxy2)
      #pygame.mixer.music.play(-1)
      if event.type==pygame.MOUSEBUTTONDOWN:
        if boton3.mouse==True:
           self.state='menu_pausa'
      if event.type==pygame.MOUSEBUTTONDOWN:
        if boton4.mouse==True:
           self.state='menu_info'
              
      timer_font = pygame.font.SysFont('Consolas', 30)
      global timer_sec
      timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
      timer = pygame.USEREVENT + 1        
      pygame.time.set_timer(timer, 1000)
      global grab
      global parent
      
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player.change_speed(-1, 0)
              player.image = pygame.image.load("perleft.png").convert_alpha()
          if event.key == pygame.K_RIGHT:
              player.change_speed(1, 0)
              player.image = pygame.image.load("perright.png").convert_alpha()
          if event.key == pygame.K_UP:
              player.change_speed(0, -1)
              player.image = pygame.image.load("perup.png").convert_alpha()
          if event.key == pygame.K_DOWN:
              player.change_speed(0, 1)
              player.image = pygame.image.load("perdown.png").convert_alpha()
         
            
      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              player.change_speed(0, 0)
          if event.key == pygame.K_RIGHT:
              player.change_speed(0, 0)
          if event.key == pygame.K_UP:
              player.change_speed(0, 0)
          if event.key == pygame.K_DOWN:
              player.change_speed(0, 0)
      
      
          
#VALIDACIONES
      for i in range(8):
          for j in range(8):
              if tablero1.matriz[i][j].tieneJugador == True:
                  player.setPos(tablero1.matriz[i][j].posX,tablero1.matriz[i][j].posY)
                      #print(player.speed_x,player.speed_y)
              if tablero1.matriz[i][j].objeto.nombre != "":
                  screen.blit(tablero1.matriz[i][j].objeto.image, [tablero1.matriz[i][j].posX, tablero1.matriz[i][j].posY ])
                    
      tablero1.matriz[player.currentX][player.currentY].tieneJugador = False
      tablero1.matriz[player.speed_x][player.speed_y].tieneJugador = True
      all_sprites_list.draw(screen)
      
      #Reloj
      if event.type == timer: 
          if timer_sec > 0:
              timer_sec -= 1
              timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
              #print(timer_sec)
          else:
              pygame.time.set_timer(timer, 60000)
            
      screen.blit(timer_text, [300, 110])
      clock.tick(FPS)
      pygame.display.flip()
      
  def nivel_2(self):
      #pygame.mixer.music.play(-1)
      x = 0
      fondo2 = pygame.image.load("fondo2.png").convert() 
      screen.blit(fondo2,(x,0))
      x_a = x % fondo2.get_rect().width
      screen.blit(fondo2, (x_a - fondo2.get_rect().width ,0))
      if x_a < W:
          screen.blit(fondo2,(x_a,0))
          screen.blit(tablero, [390,110])
      x -= 2
      screen.blit(UI,[0,0])
      
      coorxy=[8,8]
      #coorxy2=[8,8]
      boton3=Boton('pausa','pausa_0.png',coorxy)
      imagenboton3=boton3.ima
      screen.blit(imagenboton3,coorxy)
      #boton2=Boton('pausa','pausa_0.png',coorxy2)
      #imagenboton2=boton2.ima
      #pygame.mixer.music.play(-1)
      if event.type==pygame.MOUSEBUTTONDOWN:
          if boton3.mouse==True:
              screen.blit(fondo3,[0,0])
              
      timer_font = pygame.font.SysFont('Consolas', 30)
      global timer_sec
      timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
      timer = pygame.USEREVENT + 1        
      pygame.time.set_timer(timer, 1000)
      global grab
      global parent
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player.change_speed(-1, 0)
              player.image = pygame.image.load("perleft.png").convert_alpha()
          if event.key == pygame.K_RIGHT:
              player.change_speed(1, 0)
              player.image = pygame.image.load("perright.png").convert_alpha()
          if event.key == pygame.K_UP:
              player.change_speed(0, -1)
              player.image = pygame.image.load("perup.png").convert_alpha()
          if event.key == pygame.K_DOWN:
              player.change_speed(0, 1)
              player.image = pygame.image.load("perdown.png").convert_alpha()
          if event.key == pygame.K_SPACE:
              grab=True
              parent,dx,dy=playerpos.parent(positivo)
            
          if event.type == pygame.K_e:
              if grab==True:
                  grab=False
                  player.grab=False
                  print('grab false')

              if grab==True:
                  player.grab=True
                
              if player.grab==True:
                  print('')
                  if event.key == pygame.K_DOWN:
                      playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                      playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                      playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                      playerpos.changeparent(carga1pos,'right',parent) 
            
      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              player.change_speed(0, 0)
          if event.key == pygame.K_RIGHT:
              player.change_speed(0, 0)
          if event.key == pygame.K_UP:
              player.change_speed(0, 0)
          if event.key == pygame.K_DOWN:
              player.change_speed(0, 0)
      
      
          
#VALIDACIONES
      for i in range(8):
          for j in range(8):
              if tablero1.matriz[i][j].tieneJugador == True:
                  player.setPos(tablero1.matriz[i][j].posX,tablero1.matriz[i][j].posY)
                      #print(player.speed_x,player.speed_y)
              if tablero1.matriz[i][j].objeto.nombre != "":
                  screen.blit(tablero1.matriz[i][j].objeto.image, [tablero1.matriz[i][j].posX, tablero1.matriz[i][j].posY ])
                    
      tablero1.matriz[player.currentX][player.currentY].tieneJugador = False
      tablero1.matriz[player.speed_x][player.speed_y].tieneJugador = True
      all_sprites_list.draw(screen)
      
      #Reloj
      if event.type == timer: 
          if timer_sec > 0:
              timer_sec -= 1
              timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
              #print(timer_sec)
          else:
              pygame.time.set_timer(timer, 60000)
            
      screen.blit(timer_text, [300, 300])
      clock.tick(FPS)
      pygame.display.flip()
      
  
game_state = Gamestate()

all_sprites_list = pygame.sprite.Group()
done = False

player = Player()
all_sprites_list.add(player)
tablero1 = Tablero()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    game_state.cambia_nivel()
    
 
pygame.quit()