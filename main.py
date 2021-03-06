import pygame
import cv2
import numpy
import time
from datetime import datetime
import os

pygame.init()
pygame.display.set_mode()
pygame.display.toggle_fullscreen()

pygame.display.set_caption("ELECTROMAG")
icono = pygame.image.load("assets/neutron.png")
pygame.display.set_icon(icono)

musica1 = pygame.mixer.music.load("musica1.ogg")
musica1 = pygame.mixer.music.play(-1)

n = 0

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
        if self.tipo=='jugar':
            mouse1=mouseover(imagen,coordenadas)
            if mouse1==True:
                self.ima = pygame.image.load("botones/jugar_1.png").convert_alpha()
                self.mouse=True
            if mouse1==False:
                self.ima = pygame.image.load("botones/jugar_0.png").convert_alpha()
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
                
        if self.tipo=='continuar':
            mouse4=mouseover(imagen,coordenadas)
            if mouse4==True:
                self.ima = pygame.image.load("botones/continuar_1.png").convert_alpha()
                self.mouse=True
            if mouse4==False:
                self.ima = pygame.image.load("botones/continuar_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='salir':
            mouse5=mouseover(imagen,coordenadas)
            if mouse5==True:
                self.ima = pygame.image.load("botones/salir_1.png").convert_alpha()
                self.mouse=True
            if mouse5==False:
                self.ima = pygame.image.load("botones/salir_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='n1':
            mouse6=mouseover("botones/1_1.png",coordenadas)
            if mouse6==True:
                self.ima = pygame.image.load("botones/1_1.png").convert_alpha()
                self.mouse=True
            if mouse6==False:
                self.ima = pygame.image.load("botones/1_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='n2':
            mouse7=mouseover("botones/2_1.png",coordenadas)
            if mouse7==True:
                self.ima = pygame.image.load("botones/2_1.png").convert_alpha()
                self.mouse=True
            if mouse7==False:
                self.ima = pygame.image.load("botones/2_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='n3':
            mouse8=mouseover("botones/3_1.png",coordenadas)
            if mouse8==True:
                self.ima = pygame.image.load("botones/3_1.png").convert_alpha()
                self.mouse=True
            if mouse8==False:
                self.ima = pygame.image.load("botones/3_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='n4':
            mouse9=mouseover("botones/4_1.png",coordenadas)
            if mouse9==True:
                self.ima = pygame.image.load("botones/4_1.png").convert_alpha()
                self.mouse=True
            if mouse9==False:
                self.ima = pygame.image.load("botones/4_0.png").convert_alpha()
                self.mouse=False
                
        if self.tipo=='n5':
            mouse10=mouseover("botones/5_1.png",coordenadas)
            if mouse10==True:
                self.ima = pygame.image.load("botones/5_1.png").convert_alpha()
                self.mouse=True
            if mouse10==False:
                self.ima = pygame.image.load("botones/5_0.png").convert_alpha()
                self.mouse=False

class Objeto():
    def __init__(self,nombre,ubx,uby):

        self.image = pygame.image.load(
            "assets/carga_pos_2.png").convert_alpha()
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
  def __init__(self,nombre,ubx,uby, sentido='0'):
    super().__init__(nombre,ubx,uby)
    
    
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
    
        
fondo1 = pygame.image.load("assets/fondo1.png").convert()
fondo2 = pygame.image.load("assets/fondo2.png").convert()
fondo3 = pygame.image.load("assets/fondo3.png").convert()
fondo4 = pygame.image.load("assets/fondo4.png").convert()
fondo5 = pygame.image.load("assets/fondo5.png").convert()
fondo_niveles= pygame.image.load("assets/fondo_niveles.png").convert()
menu_pausa = pygame.image.load("assets/menu_pausa_.png").convert()
menu_pausa.set_colorkey([0,0,0])
    

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
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    global timer_limit
                    global inicio
                    timer_limit=100
                    inicio=time.time()
                    self.state='nivel_1'
                if boton2.mouse==True:
                    
                    inicio=time.time()
                    self.state='niveles'
          
        pygame.display.flip()
    def niveles(self):
        global done
        global carga1pos
        global carga2pos
        global playerpos
        
        global timer_limit
        global inicio
        coorxy=[192,232]
        coorxy2=[192+153,232]
        coorxy3=[192+(153*2),232]
        coorxy4=[192+(153*3),232]
        coorxy5=[192+(153*4),232]
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
            #print('intro')
            if event.type == pygame.QUIT:
                done = True
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    
                    carga1pos=pos(2,1)
                    carga2pos=pos(5,5)
                    playerpos=pos(0,0)
                    self.state='nivel_1'
                if boton2.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    
                    carga1pos=pos(2,1)
                    carga2pos=pos(5,5)
                    playerpos=pos(0,0)
                    self.state='nivel_2'
                if boton3.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos=pos(2,1)
                    carga2pos=pos(5,5)
                    playerpos=pos(0,0)
                    self.state='nivel_3'
                if boton4.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos=pos(2,1)
                    carga2pos=pos(5,5)
                    playerpos=pos(0,0)
                    self.state='nivel_4'
                if boton5.mouse==True:
                    # global timer_limit
                    # global inicio
                    timer_limit=100
                    inicio=time.time()
                    inicio=time.time()
                    
                    carga1pos=pos(2,1)
                    carga2pos=pos(5,5)
                    playerpos=pos(0,0)
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
            #print('intro')
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
        global done
        global n
        n = 1
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), False, (255, 255, 255))
        
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        print("pygame.cycle",timer_text)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                 done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    
                    self.state='menu_pausa'
            print('pygame event')
            #if event.type == pygame.QUIT:
             #   done = True
            screen.blit(fondo1, [0, 0])

            # L=[carga1pos, carga2pos]
            # #Crea copia de L en q
            # while not equilibrio:
            #   q=[]
            #   for i in range(len(L)):
            #     q.append(i)
            #   print('recurrencia')
            #   cercania(L)
            #   #Verifica si ya no hay interacciones
            #   for i in L:      
            #   for j in q: 

            #print(sentido)
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            # screen.blit(imagenboton3,coorxy)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            
            

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

              if event.key == pygame.K_ESCAPE:
                  done = True
              
              if event.key == pygame.K_SPACE:        
                  grab=True
                  #print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(carga1pos,'right',parent)

            
            #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1090, 19])
        pygame.display.flip()

    def nivel_2(self):
        #Cositas para el Reloj           
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global done
        global n
        n = 2
        
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), False, (255, 255, 255))
        
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    
                    self.state='menu_pausa'
            print('pygame event')
            #if event.type == pygame.QUIT:
             #   done = True
            screen.blit(fondo2, [0, 0])

            # L=[carga1pos, carga2pos]
            # #Crea copia de L en q
            # while not equilibrio:
            #   q=[]
            #   for i in range(len(L)):
            #     q.append(i)
            #   print('recurrencia')
            #   cercania(L)
            #   #Verifica si ya no hay interacciones
            #   for i in L:      
            #   for j in q: 

            #print(sentido)
            
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            # screen.blit(imagenboton3,coorxy)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            
            

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
                  #print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(carga1pos,'right',parent)

            
            #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1090, 19])
        pygame.display.flip()
    
    def nivel_3(self):
        #Cositas para el Reloj           
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global done
        global n
        n = 3
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), False, (255, 255, 255))
        
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    
                    self.state='menu_pausa'
            print('pygame event')
            #if event.type == pygame.QUIT:
             #   done = True
            screen.blit(fondo3, [0, 0])

            # L=[carga1pos, carga2pos]
            # #Crea copia de L en q
            # while not equilibrio:
            #   q=[]
            #   for i in range(len(L)):
            #     q.append(i)
            #   print('recurrencia')
            #   cercania(L)
            #   #Verifica si ya no hay interacciones
            #   for i in L:      
            #   for j in q: 

            #print(sentido)
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            # screen.blit(imagenboton3,coorxy)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            
            

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
                  #print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(carga1pos,'right',parent)

            
            #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1090, 19])
        pygame.display.flip()
    
    def nivel_4(self):
        #Cositas para el Reloj           
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global done
        global n
        n = 4
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), False, (255, 255, 255))
        
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    
                    self.state='menu_pausa'
            print('pygame event')
            #if event.type == pygame.QUIT:
             #   done = True
            screen.blit(fondo4, [0, 0])

            # L=[carga1pos, carga2pos]
            # #Crea copia de L en q
            # while not equilibrio:
            #   q=[]
            #   for i in range(len(L)):
            #     q.append(i)
            #   print('recurrencia')
            #   cercania(L)
            #   #Verifica si ya no hay interacciones
            #   for i in L:      
            #   for j in q: 

            #print(sentido)
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            # screen.blit(imagenboton3,coorxy)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            
            

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
                  #print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(carga1pos,'right',parent)

            
            #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1090, 19])
        pygame.display.flip()
    
    def nivel_5(self):
        #Cositas para el Reloj           
        timer_font = pygame.font.Font('fuentes\joystix monospace.ttf', 35)
        global timer_limit 
        global grab
        global parent
        global sentido
        global done
        global n
        n = 5
        
        
        tactual=inicio-(time.time())
        timer_sec=int(timer_limit+tactual)
        #print(timer_sec,'=========',tactual)
        pygame.display.update()
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), False, (255, 255, 255))
        
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton3.mouse==True:
                    
                    self.state='menu_pausa'
            print('pygame event')
            #if event.type == pygame.QUIT:
             #   done = True
            screen.blit(fondo5, [0, 0])

            # L=[carga1pos, carga2pos]
            # #Crea copia de L en q
            # while not equilibrio:
            #   q=[]
            #   for i in range(len(L)):
            #     q.append(i)
            #   print('recurrencia')
            #   cercania(L)
            #   #Verifica si ya no hay interacciones
            #   for i in L:      
            #   for j in q: 

            #print(sentido)
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            # screen.blit(imagenboton3,coorxy)
            screen.blit(player.image,player.posip)
            screen.blit(carga1.image,carga1.posip)
            screen.blit(carga2.image,carga2.posip)
            
            

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
                  #print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  #print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  #print('grab false')

            

              if grab==True:
                player.grab=True
                
            
              if player.grab==True:
                  if event.key == pygame.K_DOWN:
                    playerpos.changeparent(carga1pos,'down',parent)
                  if event.key == pygame.K_UP:
                    playerpos.changeparent(carga1pos,'up',parent)
                  if event.key == pygame.K_LEFT:
                    playerpos.changeparent(carga1pos,'left',parent)
                  if event.key == pygame.K_RIGHT:
                    playerpos.changeparent(carga1pos,'right',parent)

            
            #Reloj
        timer_text = timer_font.render(datetime.utcfromtimestamp(timer_sec).strftime('%M:%S'), True, (255, 255, 255))
        screen.blit(UI,[0,0])
        screen.blit(imagenboton3,coorxy)
        screen.blit(timer_text, [1090, 19])
        pygame.display.flip()
class pos():
    def __init__(self,ubx,uby):
        self.posxn=ubx
        self.posyn=uby
        self.posn=[self.posxn,self.posyn]
        self.posp=m.trannp(self.posxn,self.posyn)

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

              print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              if self.posyn!=6:
                self.posyn= self.posyn+1
                obj.posyn= self.posyn+1
              print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje  
            if parent=='abajo':
              self.posyn= self.posyn+1
              obj.posyn=self.posyn
              print('moviendo abajo',obj.posxn)


      if dirc=='left':
        if self.posyn!=0:
          #Carga a la izquierda del personaje
            if parent=='izquierda':
              if self.posyn!=1:
                self.posyn= self.posyn-1 
                obj.posyn= self.posyn-1
                print('moviendo izquierda',obj.posxn)
            #Carga a la derecha del personaje
            if parent=='derecha':
              self.posyn= self.posyn-1 
              obj.posyn= self.posyn+1
              print('moviendo derecha',obj.posxn)
            #Carga arriba del personaje
            if parent=='arriba':
              self.posyn= self.posyn-1 
              obj.posyn=self.posyn
              print('moviendo arriba',obj.posxn)
            #Carga abajo del personaje  
            if parent=='abajo':
              self.posyn= self.posyn-1 
              obj.posyn=self.posyn
              print('moviendo abajo',obj.posxn)
         


              
    def parent(self,obj):
        
        dy=self.posxn-obj.posxn
        dx=self.posyn-obj.posyn

       
          
        posobj=[0,0]
        if dx==1 and dy==0:
          parent='izquierda'
          print('1')
          
        elif dx==-1 and dy==0 :

          parent='derecha'
          print('2')

        elif dy==1 and dx==0:
          parent='arriba'
          print('3')
          
        elif dy==-1 and dx==0:
          parent='abajo'
          print('4')

        else:
          parent='no'
          
        return parent,dx,dy
          
          
          #posobj[1]=self.posn[1]-1
          #print(posobj, 'Funciona condicion1==========')
        return posobj



def cercania(L):
  q=[]
  for i in L:
    q.append(i)
  
  for i in q: 
    k=i.posxn
    j=i.posyn
    
    for o in q:
      g= o.posxn
      h = o.posyn
      if abs(k-g)==1:

        print('aaaaaaaaaaaaa',i.tipo, i.pos, o.tipo, o.pos)
        #no son neutros
        if i.tipo!='neutro' and o.tipo!='neutro':
          
          #TIENEN CARGA IGUAL
          if i.tipo==o.tipo:
            #print('repeler===>',i.tipo, i.pos, o.tipo, o.pos)
            
    
            if i.pos>o.pos:
              i.posxn=i.posxn+1
              o.posxn=o.posxn-1
            if i.posxn<o.posxn:
              i.posxn=i.posxn-1
              o.posxn=o.posxn+1
            #print('repelido===>',i.tipo, i.pos, o.tipo, o.pos)


        q.remove(i)
        q.remove(o)


sentido='0'

game_state = Gamestate()

carga1pos=pos(2,1)

carga2pos=pos(5,5)

playerpos=pos(0,0)
#carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))

tablero = Objeto('tablero',0,0)

size = (1280, 720)
screen = pygame.display.set_mode(size)



portada = pygame.image.load("assets/portada.png").convert()

# boton1a = pygame.image.load('botones/jugar_0.png').convert_alpha()
# boton1b = pygame.image.load('botones/jugar_1.png').convert_alpha()
# boton1 = Boton('jugar', 'botones/jugar_0.png', [640 - 152, 420 - 32])

UI = pygame.image.load('botones/margenes.png').convert_alpha()

clock = pygame.time.Clock()

done = False
parent = None
timer_limit = 360
grab = False
#print(dir(Gamestate))
inicio=time.time()
while not done:
    
    game_state.cambia_nivel()
    clock.tick(60)
    # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     done = True
    # for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 done = True
    
pygame.quit()


