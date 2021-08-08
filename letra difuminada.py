import pygame 

pygame.init()
clock = pygame.time.Clock()
tamaño = (1280,720)
screen = pygame.display.set_mode(tamaño)
fondo = pygame.image.load("C:/Users/FAMILIA/.spyder-py3/Imagenes/space (1).png").convert()

def main():
   
    font = pygame.font.Font("C:/Users/FAMILIA/.spyder-py3/Letra/MP16OSF.ttf", 64)
    orig_surf = font.render('hola', True, pygame.Color('royalblue'))
    txt_surf = orig_surf.copy()
    alpha = 255  
    timer = 60  
    done = False


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
        if timer > 0:
            timer -= 1
        else:
            if alpha > 0:
                # Reduce alpha each frame, but make sure it doesn't get below 0.
                alpha = max(0, alpha-4)
                # Create a copy so that the original surface doesn't get modified.                
                txt_surf = orig_surf.copy()
                txt_surf.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)

        screen.blit(fondo, (0,0))
        screen.blit(txt_surf, (30, 60))
        clock.tick(30)
        pygame.display.update()
         
                      
if __name__ == '__main__':
    main()
    pygame.quit()        
    
pygame.init()