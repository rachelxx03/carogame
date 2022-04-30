import os.path
import button

import pygame
WIDTH,HEIGHT=750,750
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("caro")
gray=(36,36,36)
background=pygame.transform.scale(pygame.image.load(os.path.join("art", "back.png")),(WIDTH,HEIGHT))
logo=pygame.transform.scale(pygame.image.load(os.path.join("art", "carologo.png")),(750,800))
start_img=pygame.transform.scale(pygame.image.load(os.path.join("art", "start.png")),(950,1000)).convert_alpha()
quit_img=pygame.transform.scale(pygame.image.load(os.path.join("art", "quit.png")),(950,1000)).convert_alpha()


start_button = button.Button(-250,-30 , start_img, 0.8)
exit_button = button.Button(220, -110, quit_img, 0.8)
def main():
   run=True
   while run:
        WIN.blit(background,(0,0))
        WIN.blit(logo, (-10, 0))

        if start_button.draw(WIN):
            print('START')
        if exit_button.draw(WIN):
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        pygame.display.update()
   pygame.quit()




if __name__=="__main__":

    main()
