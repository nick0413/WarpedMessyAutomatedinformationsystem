import pygame
import cv2
import numpy
import time

pygame.init()
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


class Gamestate():
    def __init__(self):
        self.state='intro'

    def cambia_nivel(self):
        if self.state=='intro':
            self.intro()
        if self.state=='nivel_1':
            self.nivel_1()

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


    def nivel_1(self):
        #Cositas para el Reloj
        timer_font = pygame.font.SysFont('Consolas', 30)
        global timer_sec
        timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
        timer = pygame.USEREVENT + 1        
        pygame.time.set_timer(timer, 1000)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.blit(tablero2, [0, 0])
            carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn)) 
            screen.blit(tablero.image, tablero.posip)
            screen.blit(carga1.image,carga1.posip)
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_DOWN:
                carga1pos.changepos('down')
            
            #Reloj
            if event.type == timer: 
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_text = timer_font.render(time.strftime('%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
                    #print(timer_sec)
                else:
                      pygame.time.set_timer(timer, 0)
            
        screen.blit(timer_text, [300, 300])
                

        pygame.display.flip()


class pos():
    def __init__(self,ubx,uby):
        self.posxn=ubx
        self.posyn=uby
        self.posn=(self.posxn,self.posyn)
        self.posp=m.trannp(self.posxn,self.posyn)
  
    def changepos(self,dirc):
        if dirc=='down':
            self.posxn= self.posxn+1


game_state = Gamestate()

carga1pos=pos(3,5)

carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn))

tablero = Objeto('tablero',0,0)
tablero2 = pygame.image.load("assets/tablero2.png").convert()
size = (1280, 720)
screen = pygame.display.set_mode(size)



portada = pygame.image.load("assets/title card.png").convert()

boton1a = pygame.image.load('botones/jugar_0.png').convert_alpha()
boton1b = pygame.image.load('botones/jugar_1.png').convert_alpha()
boton1 = Boton('jugar', 'botones/jugar_0.png', [640 - 152, 420 - 32])

UI = pygame.image.load('botones/margenes.png').convert_alpha()

clock = pygame.time.Clock()

done = False


'''
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.blit(tablero2, [0, 0])


        carga1=Objeto('positivo',(carga1pos.posxn),(carga1pos.posyn)) 
        screen.blit(tablero.image, tablero.posip)
        screen.blit(carga1.image,carga1.posip)
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            carga1pos.changepos('down')

  '''

timer_sec = 1800000000
#print(dir(Gamestate))
while not done:
 
    game_state.cambia_nivel()
    clock.tick()

pygame.quit()