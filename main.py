import pygame
from pygame.locals import *
import sys
import cv2
import numpy
import time
import os

pygame.init()
pygame.display.set_mode()
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
FPS = 60
x=0
fondo = pygame.image.load("C:/Users/FAMILIA/.spyder-py3/Imagenes/Fondopaola.png").convert()
pinilla= pygame.image.load("C:/Users/FAMILIA/.spyder-py3/Imagenes/2.png").convert()
pinilla.set_colorkey(red)

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


m=Grid(64,(500,100))





class Player(Objeto):
  def __init__(self,nombre,ubx,uby, sentido='0'):
    super().__init__(nombre,ubx,uby)
    
    
    self.grab=None

    if sentido=='down':
        self.image=pygame.image.load("assets/perdown.png").convert_alpha()
        print('cambio abajo')
    if sentido=='up':
        self.image=pygame.image.load("assets/perup.png").convert_alpha()
        print('cambio up')
    if sentido=='left':
        self.image=pygame.image.load("assets/perleft.png").convert_alpha()
        print('cambio izquiera')
    if sentido=='right':
        self.image=pygame.image.load("assets/perright.png").convert_alpha()
        print('cambio derecha')
    else:
        self.image=pygame.image.load("assets/personaje.png").convert_alpha()

        



class Gamestate():
    def __init__(self):
        self.state='videoCoulomb'

    def cambia_nivel(self):
        if self.state=='intro':
            self.intro()
        if self.state=='nivel_1':
            self.nivel_1()
        if self.state== "videoCoulomb":
            self.videoCoulomb()
        if self.state=='menu_pausa':
            self.menu_pausa()
            
    def menu_pausa(self):
        fondom()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
                screen.blit(fondo, [x_a,0])
                screen.blit(pinilla, [384+400, 104])  
                k.draw()
       

              
        pygame.display.update()
    
        reloj.tick(FPS)
      
        pygame.display.flip()
      
    def videoCoulomb(self):
        coulomb = "Coulomb"
        num_of_frames = len(os.listdir(coulomb))
        for i in range (0, 20):
            img1= pygame.image.load(f"Coulomb/myphotos{i}.png")
            screen.blit(img1, (0,0))
            pygame.display.update()
            time.sleep(0.02)
           
            self.state='nivel_1'
            print(self.state)     
            

        pygame.display.flip()
        

    def intro(self):
        coorxy=[640-152,420-32]
        coorxy2=[640-152,420+50]
        boton1=Boton('jugar','botones/jugar_0.png',coorxy)
        imagenboton1=boton1.ima
        boton2=Boton('nivel','botones/niveles_0.png',coorxy2)
        imagenboton2=boton2.ima
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.blit(portada, [0, 0])
            coorxy=[640-152,420-32]
            screen.blit(imagenboton1,coorxy)
            screen.blit(imagenboton2,coorxy2)
            #print('intro')
            if event.type==pygame.MOUSEBUTTONDOWN:
                if boton1.mouse==True:
                    self.state='nivel_1'
          
        pygame.display.flip()

    
    def fondom():
        global x
        x_a = x % fondo.get_rect().width
        screen.blit(fondo, (x_a - fondo.get_rect().width ,0))
        if x_a < 1280:
            screen.blit(fondo,(x_a,0))
            screen.blit(pinilla, [384+400, 104])
            k.draw()

        x-=1 

    def nivel_1(self):
        #videoCoulomb
        coorxy=[8,8]
        boton3=Boton('pausa','botones/pausa_0.png',coorxy)
        imagenboton3=boton3.ima
        screen.blit(imagenboton3,coorxy)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if boton3.mouse==True:
                self.state='menu_pausa'
        #Cositas para el Reloj
        timer_font = pygame.font.SysFont('Consolas', 30)
        global timer_sec      
        timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
        timer = pygame.USEREVENT + 1        
        pygame.time.set_timer(timer, 1000)
        global grab
        global parent
        global sentido

 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.blit(tablero2, [0, 0])



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

        



            print(sentido)
            player=Player('player',playerpos.posxn,playerpos.posyn,sentido)
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))
            carga2=Objeto('positivo',(carga2pos.posxn),(carga2pos.posxn))
            
            #print(carga1pos.posn,'====>',carga1pos.posxn)
            screen.blit(tablero.image, tablero.posip)
            screen.blit(UI,[0,0])
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
                  print('parent fue creado')
                  parent,dx,dy=playerpos.parent(carga1pos)
                  print(parent,dx,dy)

              if event.key == pygame.K_e:
                if grab==True:
                  grab=False
                  player.grab=False
                  print('grab false')

            

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
            if event.type == timer: 
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
                    #print(timer_sec)
                else:
                      pygame.time.set_timer(timer, 60000)
            
        screen.blit(timer_text, [300, 300])
        
         
        #Cientifica
        fondom()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
                screen.blit(fondo, [x_a,0])
                screen.blit(pinilla, [384+400, 104])  
                k.draw()
       

              
        pygame.display.update()
    
        reloj.tick(FPS)
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
            
          #TIENEN DIFERENTE CARGA
          if i.tipo !=o.tipo:
            print('atraido===>',i.tipo, i.pos, o.tipo, o.pos)
            if i.posxn>o.posxn:
              i.posxn=i.posxn-1

            if i.posxn<o.posxn:
              i.posxn=i.posxn+1


            
        #print('cumple cercania====>',i.tipo, i.pos, o.tipo, o.pos)

        q.remove(i)
        q.remove(o)


class Text:

    def __init__(self, text, pos, fontsize, color, fontname='C:/Users/FAMILIA/.spyder-py3/Letra/MP16OSF.ttf', ):
        self.text = text
        self.len = len(self.text)+1
        self.pos = pos
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = Color(color)
        self.set_font()
        self.move = True
        
            
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
     
    def tfin(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos
        screen.blit(self.img, self.rect)
        #pygame.display.update()
        
    def draw(self):
        while self.move:
            for n in range(0, self.len):
                if n == self.len-1:
                    self.move = False
                self.img = self.font.render(self.text[0:n], True, self.fontcolor)
                self.rect = self.img.get_rect()
                self.rect.center = self.pos
                R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
                pygame.draw.rect(screen, (0,0,0), R)
                screen.blit(self.img, self.rect)
                pygame.display.update()
                pygame.time.wait(400)
        self.tfin()
        
        
        
        
k = Text('¡Hola!, soy Paola Pinilla. Astrofísica Colombiana ', (w/2.0,h-650), 35, white ) 

#def listapos()



sentido='0'

game_state = Gamestate()

carga1pos=pos(2,1)

carga2pos=pos(5,5)

playerpos=pos(0,0)
carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))

tablero = Objeto('tablero',0,0)
tablero2 = pygame.image.load("assets/tablero2.png").convert()





portada = pygame.image.load("assets/title card.png").convert()

boton1a = pygame.image.load('botones/jugar_0.png').convert_alpha()
boton1b = pygame.image.load('botones/jugar_1.png').convert_alpha()
boton1 = Boton('jugar', 'botones/jugar_0.png', [640 - 152, 420 - 32])

UI = pygame.image.load('botones/margenes.png').convert_alpha()

clock = pygame.time.Clock()

done = False
parent = None
timer_sec = 60
grab = False
#print(dir(Gamestate))

while not done:
 
    game_state.cambia_nivel()
    clock.tick(1)

pygame.quit()