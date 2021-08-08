import pygame
import cv2
import numpy

#Colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

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
        


class Objeto(pygame.sprite.Sprite):
  def __init__(self, nombre):
    super().__init__()
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
        self.iniX = 384
        self.iniY = 204

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
        self.image = pygame.image.load("assets/pc_personaje.png").convert_alpha()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.currentX = 0
        self.currentY = 0
        #self.rect.x = 0
        #self.rect.y = posY
        #self.rect.height = 64
        #self.rect.width = 64

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

        if event.type==pygame.MOUSEBUTTONDOWN:
          if boton1.mouse==True:
            self.state='nivel_1'
        

    #all_sprites_list.draw(screen)

    pygame.display.flip()


  def nivel_1(self):
      

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.blit(tablero2, [0, 0])
        screen.blit(tablero, [384, 204])
        

        #Eventos del teclado
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-1, 0)
            if event.key == pygame.K_RIGHT:
                player.change_speed(1, 0)
            if event.key == pygame.K_UP:
                player.change_speed(0, -1)
            if event.key == pygame.K_DOWN:
                player.change_speed(0, 1)

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
                    player.setPos(tablero1.matriz[i][j].posX,
                                  tablero1.matriz[i][j].posY)
                    print(player.speed_x,player.speed_y)
                if tablero1.matriz[i][j].objeto.nombre != "":
                    screen.blit(tablero1.matriz[i][j].objeto.image, [
                        tablero1.matriz[i][j].posX, tablero1.matriz[i][j].posY
                    ])
                    #tablero1.matriz[i][j].objeto.rect.x = tablero1.matriz[i][j].posX
                    #tablero1.matriz[i][j].objeto.rect.y = tablero1.matriz[i][j].posY
                    #all_sprites_list.add(tablero1.matriz[i][j].objeto)
        tablero1.matriz[player.currentX][player.currentY].tieneJugador = False
        tablero1.matriz[player.speed_x][player.speed_y].tieneJugador = True
        screen.blit(UI, [0, 0])

    all_sprites_list.draw(screen)

    pygame.display.flip()



pygame.init()


size = (1280, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_state = Gamestate()

all_sprites_list = pygame.sprite.Group()
done = False

portada=tablero = pygame.image.load("assets/title card.png").convert()
tablero = pygame.image.load("assets/tablero MK II.png").convert()
tablero2 = pygame.image.load("assets/tablero2.png").convert()

boton1a=pygame.image.load('botones/jugar_0.png').convert_alpha()
boton1b=pygame.image.load('botones/jugar_1.png').convert_alpha()
boton1=Boton('jugar','botones/jugar_0.png',[640-152,420-32])
player = Player()
all_sprites_list.add(player)
tablero1 = Tablero()
UI=pygame.image.load('botones/margenes.png')


coorxy=[640,420]

#crear diferentes loops en esta clase, cada loop es un nivel o una pantalla


while not done:


  game_state.cambia_nivel()
  clock.tick(12)

pygame.quit()