import pygame
import cv2
import numpy
import time
from datetime import datetime
import os
pygame.init()


pygame.display.set_caption("ELECTROMAG")
icono = pygame.image.load("assets/neutron.png")
pygame.display.set_icon(icono)

musica1 = pygame.mixer.music.load("musica1.ogg")
musica1 = pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
w= screen.get_width()
h=screen.get_height()

#Colores 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
amarillo = (255, 255, 0)
green = (0, 255, 0)
blue= (0, 0, 255)

FPS = 60
reloj = pygame.time.Clock()
x=0
x_a=0

# Fondos-Imágenes Científicas.
fondo = pygame.image.load("ImagenesCientificas/Fondopaola.png").convert()
fondodiana = pygame.image.load("ImagenesCientificas/fondodiana.png").convert()
fondolise = pygame.image.load("ImagenesCientificas/fondolise.png").convert()
fondonubia = pygame.image.load("ImagenesCientificas/fondonubia.png").convert()
fondomarie = pygame.image.load("ImagenesCientificas/fondomarie.png").convert()
fondorosalind = pygame.image.load("ImagenesCientificas/fondoRosalind.png").convert()
pinilla= pygame.image.load("ImagenesCientificas/2.png").convert()
pinilla.set_colorkey(red)
diana= pygame.image.load("ImagenesCientificas/DianaT.png").convert()
diana.set_colorkey(red)
lise= pygame.image.load("ImagenesCientificas/lisem.png").convert()
lise.set_colorkey(white)
nubia= pygame.image.load("ImagenesCientificas/nubia1.png").convert()
nubia.set_colorkey(blue)
marie= pygame.image.load("ImagenesCientificas/mariec.png").convert()
marie.set_colorkey(amarillo)
rosalind= pygame.image.load("ImagenesCientificas/Rosalind1.png").convert_alpha()
rosalind.set_colorkey(blue)
#VARIABLE NIVEL
n=0
pygame.display.set_mode()

def mouseover(imagen,coordenadas):
    mouse=False
    y,x,_ = cv2.imread(imagen).shape
    mx,my = pygame.mouse.get_pos()
    tx,ty=coordenadas[0],coordenadas[1]
    if tx+x > mx >tx:
        if ty+y > my > ty:      
            mouse=True
    #print(coordenadas,x,y,imagen)
    return mouse

class Boton():
    def __init__(self,tipo,imagen,coordenadas):
        self.mouse=False
        self.tipo=tipo
        self.coordenadas=coordenadas
        self.ima = pygame.image.load("botones/jugar_1.png").convert_alpha()
        
        #JUGAR
        if self.tipo=='jugar':
            mouse1=mouseover(imagen,coordenadas)
            if mouse1==True:
                self.ima = pygame.image.load("botones/jugar_1.png").convert_alpha()
                self.mouse=True
            if mouse1==False:
                self.ima = pygame.image.load("botones/jugar_0.png").convert_alpha()
                self.mouse=False

        #NIVEL
        if self.tipo=='nivel':
            mouse2=mouseover(imagen,coordenadas)
            if mouse2==True:
                self.ima = pygame.image.load("botones/niveles_1.png").convert_alpha()
                self.mouse=True
            if mouse2==False:
                self.ima = pygame.image.load("botones/niveles_0.png").convert_alpha()
                self.mouse=False
          
        #PAUSA        
        if self.tipo=='pausa':
            mouse3=mouseover(imagen,coordenadas)
            if mouse3==True:
                self.ima = pygame.image.load("botones/pausa_1.png").convert_alpha()
                self.mouse=True
            if mouse3==False:
                self.ima = pygame.image.load("botones/pausa_0.png").convert_alpha()
                self.mouse=False
                                 
        #CONTINUAR
        if self.tipo=='continuar':
            mouse4=mouseover(imagen,coordenadas)
            if mouse4==True:
                self.ima = pygame.image.load("botones/continuar_1.png").convert_alpha()
                self.mouse=True
            if mouse4==False:
                self.ima = pygame.image.load("botones/continuar_0.png").convert_alpha()
                self.mouse=False
        #SALIR
        if self.tipo=='salir':
            mouse5=mouseover(imagen,coordenadas)
            if mouse5==True:
                self.ima = pygame.image.load("botones/salir_1.png").convert_alpha()
                self.mouse=True
            if mouse5==False:
                self.ima = pygame.image.load("botones/salir_0.png").convert_alpha()
                self.mouse=False
                
        #NIVEL 1
        if self.tipo=='n1':
            mouse6=mouseover("botones/1_1.png",coordenadas)
            if mouse6==True:
                self.ima = pygame.image.load("botones/1_1.png").convert_alpha()
                self.mouse=True
            if mouse6==False:
                self.ima = pygame.image.load("botones/1_0.png").convert_alpha()
                self.mouse=False
        
        #NIVEL 2
        if self.tipo=='n2':
            mouse7=mouseover("botones/2_1.png",coordenadas)
            if mouse7==True:
                self.ima = pygame.image.load("botones/2_1.png").convert_alpha()
                self.mouse=True
            if mouse7==False:
                self.ima = pygame.image.load("botones/2_0.png").convert_alpha()
                self.mouse=False
                
        #NIVEL 3        
        if self.tipo=='n3':
            mouse8=mouseover("botones/3_1.png",coordenadas)
            if mouse8==True:
                self.ima = pygame.image.load("botones/3_1.png").convert_alpha()
                self.mouse=True
            if mouse8==False:
                self.ima = pygame.image.load("botones/3_0.png").convert_alpha()
                self.mouse=False        
        
        #NIVEL 4
        if self.tipo=='n4':
            mouse9=mouseover("botones/4_1.png",coordenadas)
            if mouse9==True:
                self.ima = pygame.image.load("botones/4_1.png").convert_alpha()
                self.mouse=True
            if mouse9==False:
                self.ima = pygame.image.load("botones/4_0.png").convert_alpha()
                self.mouse=False
                
        #NIVEL 5
        if self.tipo=='n5':
            mouse10=mouseover("botones/5_1.png",coordenadas)
            if mouse10==True:
                self.ima = pygame.image.load("botones/5_1.png").convert_alpha()
                self.mouse=True
            if mouse10==False:
                self.ima = pygame.image.load("botones/5_0.png").convert_alpha()
                self.mouse=False

        #INFO        
        if self.tipo=='info':
            mouse11=mouseover(imagen,coordenadas)
            if mouse11==True:
                self.ima = pygame.image.load("botones/info_1.png").convert_alpha()
                self.mouse=True
            if mouse11==False:
                self.ima = pygame.image.load("botones/info_0.png").convert_alpha()
                self.mouse=False        
class Objeto():
    def __init__(self,nombre,ubx,uby):

        self.image = pygame.image.load("assets/carga_pos_2.png").convert_alpha()
        self.nombre = nombre

        if nombre == "positivo":
            self.image = pygame.image.load("assets/carga_pos_2.png").convert_alpha()

        elif nombre == "negativo":
            self.image = pygame.image.load("assets/carga_neg_2.png").convert_alpha()

        elif nombre == "neutro":
            self.image = pygame.image.load("assets/carga_net_2.png").convert_alpha()

        elif nombre == "maquina":
            self.image = pygame.image.load("assets/maquina_fusion.png").convert_alpha()
        
        elif nombre == "tablero":
          self.image=pygame.image.load("assets/tablero MK II.png").convert_alpha()

        self.posip= m.trannp(ubx,uby)
        self.posin=[ubx,uby]


class Grid():
    def __init__(self,size,start):
        mb=[] 
        mb1=[]
        mn=[]

        for j in range(8):
            mb1=[]
            mn1=[]
            for i in range(8):
                b=(j,i)
                k=(((i*size)+start[0]),((j*size)+start[1]))
                mb1.append(b)
                mn1.append(k)
                #print(mb1)
            mb.append(mb1)
            mn.append(mn1)

        #print(mb[5][3])
        #print(mn[5][3])
        self.matrizp=mn
        self.matrizb=mb
      
    # traduce de numeros a pixeles 
    def trannp(self,x,y):
        p=self.matrizp[x][y]
        return p
    # traduce de pixeles a numeros
    def tranpn(self,x,y):
        p=self.matrizb[x][y]
        return p


m=Grid(64,(400,120))





class Player(Objeto):
  def __init__(self,nombre,posxn,posyn, sentido='0'):
    super().__init__(nombre,posxn,posyn)
    
    
    self.grab=None
    self.image=pygame.image.load("assets/personaje.png").convert_alpha()
    
    if sentido=='down':
        self.image=pygame.image.load("assets/perdown.png").convert_alpha()
        #print('cambio abajo')
    if sentido=='up':
        self.image=pygame.image.load("assets/perup.png").convert_alpha()
        # print('cambio up')
    if sentido=='left':
        self.image=pygame.image.load("assets/perleft.png").convert_alpha()
        # print('cambio izquiera')
    if sentido=='right':
        self.image=pygame.image.load("assets/perright.png").convert_alpha()
        # print('cambio derecha')
    
        

#FONDOS        
fondo1 = pygame.image.load("assets/fondo1.png").convert()
fondo2 = pygame.image.load("assets/fondo2.png").convert()
fondo3 = pygame.image.load("assets/fondo3.png").convert()
fondo4 = pygame.image.load("assets/fondo4.png").convert()
fondo5 = pygame.image.load("assets/fondo5.png").convert()
fondo_niveles= pygame.image.load("assets/fondo_niveles.png").convert()
menu_pausa = pygame.image.load("assets/menu_pausa_.png").convert()
menu_pausa.set_colorkey([0,0,0])
tutorial = pygame.image.load("assets/tutorial.png").convert()
tutorial.set_colorkey([0,0,0])
class Gamestate():
    def __init__(self):
        self.state='intro'

    def cambia_nivel(self):
        if self.state=='intro':
           self.intro()
        if self.state=='menu_pausa':
           self.menu_pausa()
          
        if self.state=='continuar':
           self.continuar()
        if self.state=='salir':
           self.salir()
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
        if self.state=='info':
           self.info()
           
    def intro(self):
        global done
        coorxy=[640-152,420-32]
        coorxy2=[640-152,420+50]
        boton1=Boton('jugar','botones/jugar_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('nivel','botones/niveles_0.png',coorxy2)
        imagenboton2=boton2.ima
        for event in pygame.event.get():            
            screen.blit(portada, [0, 0])
            coorxy=[640-152,420-32]
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            #print('intro')
            #SALIR
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                #NIVEL 1
                if boton1.mouse==True:
                    global timer_limit
                    global inicio
                    timer_limit=100
                    inicio=time.time()
                    self.state='nivel_1'
                    
                #MENÚ NIVELES    
                if boton2.mouse==True:                    
                    inicio=time.time()
                    self.state='niveles'         
        pygame.display.flip()

    def info(self):
        global done
        coorxy=[482,232]        
        boton1=Boton('continuar','botones/continuar_0.png',coorxy)
        imagenboton1=boton1.ima
        for event in pygame.event.get():            
            screen.blit(tutorial, [0, 0])
            screen.blit(menu_pausa, [0, 0])
            coorxy=[482,232]
            screen.blit(imagenboton1,coorxy)            
            #SALIR
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    if n == 1:
                        self.state='nivel_1'
                    if n == 2:
                        self.state='nivel_2'
                    if n == 3:
                        self.state='nivel_3'
                    if n == 4:
                        self.state='nivel_4'    
                    if n == 5:
                        self.state='nivel_5'
                
                
                    
        pygame.display.flip()

    #GENERA MENÚ NIVELES
    def niveles(self):
        global done
        global carga1pos_pos
        global carga2pos_pos
        global carga1neg_pos
        global playerpos
        
        global timer_limit
        global inicio
        
        #COORDENADAS DE LOS BOTONES DE LOS NIVELES
        coorxy=[192,232]
        coorxy2=[192+153,232]
        coorxy3=[192+(153*2),232]
        coorxy4=[192+(153*3),232]
        coorxy5=[192+(153*4),232]
        
        #BOTONES
        boton1=Boton('n1','botones/1_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('n2','botones/2_0.png',coorxy2)
        imagenboton2=boton2.ima
        boton3=Boton('n3','botones/3_0.png',coorxy3)
        imagenboton3=boton3.ima
        boton4=Boton('n4','botones/4_0.png',coorxy4)
        imagenboton4=boton4.ima
        boton5=Boton('n5','botones/5_0.png',coorxy5)
        imagenboton5=boton5.ima
     
        
        for event in pygame.event.get():
            screen.blit(fondo_niveles, [0, 0])
            #coorxy=[492,232]
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            screen.blit(imagenboton3,coorxy3)
            screen.blit(imagenboton4,coorxy4)
            screen.blit(imagenboton5,coorxy5)
            if event.type == pygame.QUIT:
                done = True
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                #BOTÓN NIVEL 1
                if boton1.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    
                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    
                    carga3pos_pos=pos('positivo', [4,2])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])
                    
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [6,2])
                    self.state='nivel_1'
                
                #BOTÓN NIVEL 2    
                if boton2.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    
                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    
                    carga3pos_pos=pos('positivo', [4,2])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])
                    
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [6,2])
                    self.state='nivel_2'    
                   
                #BOTÓN NIVEL 3    
                if boton3.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    
                    carga3pos_pos=pos('positivo', [4,2])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])
                    
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [6,2])
                    self.state='nivel_3'
                    
                #BOTÓN NIVEL 4    
                if boton4.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    
                    carga3pos_pos=pos('positivo', [4,2])
                    carga1neg_pos = pos('negativo', [3,6])
                    carga2neg_pos = pos('negativo', [7,3])
                    
                    carga1net_pos=pos('neutro', [3,5])
                    carga2net_pos= pos('neutro', [1,5])
                    
                    playerpos=pos('personaje',[0,0])
                    maquinapos=pos('maquina', [6,2])
                    self.state='nivel_4'
                    
                #BOTÓN NIVEL 5    
                if boton5.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos_pos=pos('positivo',[2,1])
                    carga2pos_pos=pos('positivo', [5,5])
                    playerpos=pos('personaje',[0,0])
                    self.state='nivel_5'                        
        pygame.display.flip()

    def salir(self):
        self.state='intro'
        pygame.display.flip()
    
    def menu_pausa(self):
        global done
        coorxy=[482,232]
        coorxy2=[482,328]
        coorxy3=[482,424]
        boton1=Boton('continuar','botones/continuar_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('nivel','botones/niveles_0.png',coorxy2)
        imagenboton2=boton2.ima
        boton3=Boton('salir','botones/niveles_0.png',coorxy3)
        imagenboton3=boton3.ima
        for event in pygame.event.get():
            screen.blit(menu_pausa, [0, 0])
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            screen.blit(imagenboton3,coorxy3)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    if n == 1:
                        self.state='nivel_1'
                    if n == 2:
                        self.state='nivel_2'
                    if n == 3:
                        self.state='nivel_3'
                    if n == 4:
                        self.state='nivel_4'    
                    if n == 5:
                        self.state='nivel_5'    
                        
                if boton2.mouse==True:                    
                    self.state='niveles'
                    
                if boton3.mouse==True:                    
                    self.state='salir'                    
        pygame.display.flip() 

        
    def nivel_1(self):
        #Cositas para el Reloj        
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        n = 1
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','botones/info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos]  #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]
        for event in pygame.event.get():
            #print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:                    
                    self.state='menu_pausa'
                if boton4.mouse==True:                    
                    self.state='info'    
            screen.blit(fondo1, [0, 0])
            
         
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn))
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn))
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn))
            maquina=Objeto('maquina', (maquinapos.posxn), (maquinapos.posyn))
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(maquina.image, maquina.posip)
            
            

            if event.type == pygame.KEYDOWN:
              
              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

                

              if event.key == pygame.K_SPACE:        
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      #print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(imagenboton4,coorxy2)
        screen.blit(timer_text, [1100, 25])
        
        pygame.display.flip()


    def nivel_2(self):
        #Cositas para el Reloj        
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        n = 2
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','botones/info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos]  #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]
        for event in pygame.event.get():
            #print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:                    
                    self.state='menu_pausa'
                if boton4.mouse==True:                    
                    self.state='info'    
            screen.blit(fondo2, [0, 0])
            
         
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn))
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn))
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn))
            maquina=Objeto('maquina', (maquinapos.posxn), (maquinapos.posyn))
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(maquina.image, maquina.posip)
            
            

            if event.type == pygame.KEYDOWN:
              
              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

                

              if event.key == pygame.K_SPACE:        
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      #print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  #print('grab false')            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(imagenboton4,coorxy2)
        screen.blit(timer_text, [1100, 25])
        
        pygame.display.flip()
    
    def nivel_3(self):
        #Cositas para el Reloj        
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        n = 3
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','botones/info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos]  #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]
        for event in pygame.event.get():
            #print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:                    
                    self.state='menu_pausa'
                if boton4.mouse==True:                    
                    self.state='info'    
            screen.blit(fondo3, [0, 0])
            
         
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn))
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn))
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn))
            maquina=Objeto('maquina', (maquinapos.posxn), (maquinapos.posyn))
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(maquina.image, maquina.posip)
            
            

            if event.type == pygame.KEYDOWN:
              
              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

                

              if event.key == pygame.K_SPACE:        
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      #print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(imagenboton4,coorxy2)
        screen.blit(timer_text, [1100, 25])
        
        pygame.display.flip()
    
    def nivel_4(self):
        #Cositas para el Reloj        
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        n = 4
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','botones/info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos]  #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]
        for event in pygame.event.get():
            #print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:                    
                    self.state='menu_pausa'
                if boton4.mouse==True:                    
                    self.state='info'    
            screen.blit(fondo4, [0, 0])
            
         
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn))
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn))
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn))
            maquina=Objeto('maquina', (maquinapos.posxn), (maquinapos.posyn))
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(maquina.image, maquina.posip)
            
            

            if event.type == pygame.KEYDOWN:
              
              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

                

              if event.key == pygame.K_SPACE:        
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      #print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(imagenboton4,coorxy2)
        screen.blit(timer_text, [1100, 25])
        
        pygame.display.flip()
    
    def nivel_5(self):
        #Cositas para el Reloj        
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global proximo
        global done
        global n
        n = 5
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        coorxy2=[0,576]
        boton4=Boton('info','botones/info_0.png',coorxy2)
        imagenboton4=boton4.ima
        L=[carga1neg_pos, carga1pos_pos, carga2pos_pos]  #,carga3pos,carganeg1,carganeg2,carganet1,carganet2]
        for event in pygame.event.get():
            #print('pygame event')
            equilibrio(L)
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:                    
                    self.state='menu_pausa'
                if boton4.mouse==True:                    
                    self.state='info'    
            screen.blit(fondo5, [0, 0])
            
         
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos_pos.posxn),(carga1pos_pos.posyn))
            carga2=Objeto('positivo',(carga2pos_pos.posxn),(carga2pos_pos.posyn))
            carga3=Objeto('negativo', (carga1neg_pos.posxn), (carga1neg_pos.posyn))
            maquina=Objeto('maquina', (maquinapos.posxn), (maquinapos.posyn))
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            screen.blit(carga3.image, carga3.posip)
            screen.blit(maquina.image, maquina.posip)
            
            

            if event.type == pygame.KEYDOWN:
              
              if not grab:
                  #movimiento jugador
                  if event.key == pygame.K_DOWN:
                    playerpos.changepos('down')
                    sentido='down'
                  if event.key == pygame.K_UP:
                    playerpos.changepos('up')
                    sentido='up'
                  if event.key == pygame.K_LEFT:
                    playerpos.changepos('left')
                    sentido='left'
                  if event.key == pygame.K_RIGHT:
                    playerpos.changepos('right')
                    sentido='right'
                  #funcion de coger

                

              if event.key == pygame.K_SPACE:        
                  grab=True
                  proximo=proximidad(L, playerpos.posxn, playerpos.posyn) #busca la partícula más cercana al jugador
                  print('aquí debería existir encontrado =============>')
                  if proximo==False:
                      grab=False
                  if proximo!=False:
                      #print('parent fue creado')
                      parent,dx,dy=playerpos.parent(proximo)
                      #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  proximo.grabbed = False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  print('aquí debería referenciar encontrado =============>')
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(proximo,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(proximo,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(proximo,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(proximo,'right',parent)

        #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(imagenboton4,coorxy2)
        screen.blit(timer_text, [1100, 25])
        
        pygame.display.flip()
    
    
class pos():
    def __init__(self,tipo,pos):
        self.tipo=tipo
        self.pos=pos
        self.posxn=pos[0]
        self.posyn=pos[1]
        self.posn=[self.posxn,self.posyn]
        self.posp=m.trannp(self.posxn,self.posyn)
        self.grabbed = False

    def changepos(self,dirc):
        if self.posxn!=7:
            if dirc=='down':
                self.posxn= self.posxn+1
        if self.posxn!=0:       
            if dirc=='up':
                self.posxn= self.posxn-1
        if self.posyn!=7:               
            if dirc=='right':
                self.posyn= self.posyn+1
        if self.posyn!=0: 
            if dirc=='left':
                self.posyn= self.posyn-1                
            self.posn=[self.posxn,self.posyn]

    
    def changeparent(self,obj,dirc,parent):
    
      print(parent,'parent')
      print(dirc,'direccion')

      #MOVIMIENTO HACIA ABAJO
      if dirc=='down':
        if self.posxn!=7:
            #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posxn= self.posxn+1
              obj.posxn= self.posxn
              print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posxn= self.posxn+1
              obj.posxn= self.posxn
              print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posxn= self.posxn+1
              obj.posxn=self.posxn-1
              print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje  
            if parent=='abajo':
              if self.posxn!=6:
                self.posxn= self.posxn+1
                obj.posxn=self.posxn+1

              print('moviendo abajo',obj.posxn)



      if dirc=='up':
        if self.posxn!=0:
            #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posxn= self.posxn-1
              obj.posxn= self.posxn
              print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posxn= self.posxn-1
              obj.posxn= self.posxn
              print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              if self.posxn!=1:
                self.posxn= self.posxn-1
                obj.posxn=self.posxn-1
              print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje  
            if parent=='abajo':
              self.posxn= self.posxn-1
              obj.posxn=self.posxn+1
              print('moviendo abajo',obj.posxn)


      
      if dirc=='right':
        if self.posyn!=7:
          #Carga a la izquierda del personaje
            if parent=='izquierda':
              self.posyn= self.posyn+1
              obj.posyn= self.posyn-1

              print('moviendo izquierda',obj.posyn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              if self.posyn!=6:
                self.posyn= self.posyn+1
                obj.posyn= self.posyn+1
              print('moviendo derecha',obj.posyn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              print('moviendo arriba',obj.posyn)
            #Carga abajo del personaje  
            if parent=='abajo':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              print('moviendo abajo',obj.posyn)


      if dirc=='left':
        if self.posyn!=0:
          #Carga a la izquierda del personaje
            if parent=='izquierda':
              if self.posyn!=1:
                self.posyn= self.posyn-1 
                obj.posyn= self.posyn-1
                print('moviendo izquierda',obj.posyn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posyn= self.posyn-1 
              obj.posyn= self.posyn+1
              print('moviendo derecha',obj.posyn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn-1 
              obj.posyn=self.posyn
              print('moviendo arriba',obj.posyn)
            #Carga abajo del personaje  
            if parent=='abajo':
              self.posyn= self.posyn-1 
              obj.posyn=self.posyn
              print('moviendo abajo',obj.posyn)
         


              
    def parent(self,obj):
        
        dy=self.posxn-obj.posxn
        dx=self.posyn-obj.posyn

       
          
        posobj=[0,0]
        if dx==1 and dy==0:
          parent='izquierda'
          obj.grabbed = True
          print('1')
          
        elif dx==-1 and dy==0 :
          parent='derecha'
          obj.grabbed = True
          print('2')

        elif dy==1 and dx==0:
          parent='arriba'
          obj.grabbed = True
          print('3')
          
        elif dy==-1 and dx==0:
          parent='abajo'
          obj.grabbed = True
          print('4')

        else:
          parent='no'
          
        return parent,dx,dy
       
        return posobj



def proximidad(L,posxn,posyn):
    encontrado=False
    for i in L:
        k=i.posxn
        j=i.posyn
        print('posicion obj===',k,j,'posicion player===', posxn, posyn)
        
        if abs(k-posxn)==1 and abs(j-posyn)==0:
            print('k=',k, 'posxn=', posxn)
            return i
        
        if abs(j-posyn)==1 and abs(k-posxn)==0:
            print('j=',j, 'posyn=', posyn)
            return i
        
    else:
        return encontrado
        
            


#INTERACCIÓN OBJETO A OBJETO
def cercania(L):
  q=[]
  for i in L:
    q.append(i)
  for i in q:    
    k=i.posxn
    j=i.posyn 
    #print('nuevo i', 'k=',k,'j=', j)
    for o in q:
      g= o.posxn
      h = o.posyn
      #print('nuevo o', 'k=',k,'j=', j)



      
#REPELER 

      #REPELER VERTICAL
      if abs(k-g)==1:   #uno esta encima del otro    
        if abs(j-h)==0:
            if i.tipo!='neutro' and o.tipo!='neutro':
            
              if i.tipo==o.tipo:

                if i.posxn>o.posxn:
                  print('alejo')
                  if i.grabbed==False:                      
                      i.posxn=i.posxn+1
                  if o.grabbed==False:    
                      o.posxn=o.posxn-1
                  
                if i.posxn<o.posxn:
                  print('alejo2')
                  if i.grabbed==False:
                      i.posxn=i.posxn-1
                  if o.grabbed==False:
                      o.posxn=o.posxn+1

                print('repeler===>vertical',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))

            
                q.remove(i)
                q.remove(o)
                
                
      #REPELER HORIZONTAL
      if abs(j-h)==1:   #uno esta al lado del otro    
        if abs(k-g)==0:
            
            if i.tipo!='neutro' and o.tipo!='neutro':
                
              if i.tipo==o.tipo:
            
                if i.posyn>o.posyn:
                  print('alejo')
                  if i.grabbed==False:
                      i.posyn=i.posyn+1
                  if o.grabbed==False:
                      o.posyn=o.posyn-1
                  
                if i.posyn<o.posyn:
                  print('alejo2')
                  if i.grabbed==False:
                      i.posyn=i.posyn-1
                  if o.grabbed==False:
                      o.posyn=o.posyn+1

                print('repeler===>lados',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))

            
                q.remove(i)
                q.remove(o)
#ACABA REPELER
                
      
#ATRAER
 
     #ATRAER VERTICAL
      if abs(k-g)==2 and abs(j-h)==0:   #uno esta encima del otro
          if i.tipo!='neutro' and o.tipo!='neutro':
              if i.tipo!=o.tipo:                  
                  if i.posxn>o.posxn:
                      print('atrae')
                      if i.grabbed==False:
                          i.posxn=i.posxn-1
                      if o.grabbed==False:
                          o.posxn=o.posxn+1
                  
                  if i.posxn<o.posxn:
                      print('atare2')
                      if i.grabbed==False:
                          i.posxn=i.posxn+1
                      if o.grabbed==False:
                        o.posxn=o.posxn-1
                      
                      
                  print('atraer===>VERTICAL',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))
                  
                  q.remove(i)
                  q.remove(o)
                  
                  
                  
      #ATRAER HORIZONTAL  
      if abs(j-h)==2 and abs(k-g)==0:
            
            if i.tipo!='neutro' and o.tipo!='neutro':
                
              if i.tipo!=o.tipo:
            
                if i.posyn>o.posyn:
                  print('atrae')
                  if i.grabbed==False:
                      i.posyn=i.posyn-1
                  if o.grabbed==False:
                      o.posyn=o.posyn+1
                  
                if i.posyn<o.posyn:
                  print('atrae2')
                  if i.grabbed==False:
                      i.posyn=i.posyn+1
                  if o.grabbed==False:    
                      o.posyn=o.posyn-1

                print('atraer===>LADOS',i.tipo, (i.posxn,i.posyn), o.tipo, (o.posxn,o.posyn))
                print(i.grabbed, o.grabbed)
            
                q.remove(i)
                q.remove(o)                
      
#MISMA POSICIÓN
      print('tipo i=',i.tipo,'tipo o= ',o.tipo,i.posxn,'-',o.posxn,'===0               ',i.posyn,'-',o.posyn,'=====0')
      if abs(i.posxn-o.posxn)==0 and abs(i.posyn-o.posyn)==0:
          print('posiciones iguales')
  return q
'''          
          if i.posxn==7:
              i.posxn=i.posxn-1
          elif i.posyn==7:
              i.posyn=i.posyn-1
          elif i.posxn==0:
              i.posxn=i.posxn+1
          elif i.posyn==0:
              i.posyn=i.posyn+1
          elif 0<i.posxn<7:
              i.posyn=i.posyn+1
          elif 0<i.posyn<7:
              i.posxn=i.posxn+1
'''              
  
  

def equilibrio(l):
    q=cercania(l)
    if q!=l:
        equi=False
        #print('equilibrio ============>', equi)
    if q==l:
        equi=True
        #print('q y l son iguales')
        #print('equilibrio ============>', equi)   





sentido='0'

game_state = Gamestate()

carga1pos_pos=pos('positivo', [2,1])
carga2pos_pos=pos('positivo', [5,5])
carga3pos_pos=pos('positivo', [4,2])

carga1neg_pos = pos('negativo', [3,6])
carga2neg_pos = pos('negativo', [7,3])

carga1net_pos=pos('neutro', [3,5])
carga2net_pos= pos('neutro', [1,5])

maquinapos=pos('maquina', [6,2])

playerpos=pos('personaje',[0,0])


tablero = Objeto('tablero',0,0)
fondo2 = pygame.image.load("assets/fondo2.png").convert()

portada = pygame.image.load("assets/title card.png").convert()

boton1a = pygame.image.load('botones/jugar_0.png').convert_alpha()
boton1b = pygame.image.load('botones/jugar_1.png').convert_alpha()
boton1 = Boton('jugar', 'botones/jugar_0.png', [640 - 152, 420 - 32])

UI = pygame.image.load('botones/margenes.png').convert_alpha()

clock = pygame.time.Clock()

done = False
parent = None
timer_limit = 360
grab = False
proximo=False
#print(dir(Gamestate))
inicio=time.time()
while not done:
    
    game_state.cambia_nivel()
    clock.tick(60)


pygame.quit()