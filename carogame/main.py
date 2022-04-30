import pygame, sys
import os.path
from button import Button
import Pgm

pygame.init()

SCREEN = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "back.png")),(750,750))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        Pgm.rungame()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
    


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(120).render("CARO", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(370, 130))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(370, 320),
                            text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#8cdb6a")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(370, 500),
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#8cdb6a")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,  QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()