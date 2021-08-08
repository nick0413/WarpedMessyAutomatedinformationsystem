import pygame 
from pygame.locals import *
import sys
pygame.init()

#Colores 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Pantalla
tamaño = (1280,720)
screen = pygame.display.set_mode(tamaño)
w, h = screen.get_width(), screen.get_height()


#reloj
FPS = 60
reloj = pygame.time.Clock()

#Fondo
fondo = pygame.image.load("C:/Users/FAMILIA/.spyder-py3/Imagenes/space (1).png").convert()
x = 0
screen.blit(fondo,(x,0))
#Personaje 
#Físisca Pinilla 
pinilla= pygame.image.load("C:/Users/FAMILIA/.spyder-py3/Imagenes/2.png").convert()
pinilla.set_colorkey(red)

#Letra 
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
        
        
        
k = Text('¡Hola!, mi nombre es Paola Pinilla ', (w/2.5,h-600), 60, white ) 

    
   
#dialogo= Text("Astrofísica Colombiana", (w/4, h-300), 40, white)
done = False        
while not done:
    x_a = x % fondo.get_rect().width
    screen.blit(fondo, (x_a - fondo.get_rect().width ,0))
    if x_a < 1280:
        screen.blit(fondo,(x_a,0))
        screen.blit(pinilla, [384+400, 104])
        k.draw()
#        dialogo.draw()
    x-=1 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        screen.blit(fondo, [x_a,0])
        screen.blit(pinilla, [384+400, 104])  
        k.draw()
 #       dialogo.draw()
              
    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()