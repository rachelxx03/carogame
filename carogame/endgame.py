import os
from button import Button
import pygame
from pygame import mixer
from button import Button
import Pgm
def endgame():
    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    width = 750
    height = 750
    BLACK = (36, 36, 36)
    WHITE = (230, 241, 243)
    window = pygame.display.set_mode((width, height))
    poplft = width // 8
    poptop = height // 3
    popwdt = width * (6 / 8)
    pophgt = height // 3
    winpop = pygame.Rect(poplft, poptop, popwdt, pophgt)
    pygame.draw.rect(window, BLACK, winpop)
    pygame.draw.rect(window, WHITE, winpop, 1)
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(45).render("YOU WIN", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(370, 300))

    REPLAY_BUTTON = Button(image=None, pos=(220, 400),
                           text_input="REPLAY", font=get_font(25), base_color="White", hovering_color="#8cdb6a")

    QUIT_BUTTON = Button(image=None, pos=(550, 400),
                         text_input="QUIT", font=get_font(25), base_color="White", hovering_color="#8cdb6a")

    window.blit(MENU_TEXT, MENU_RECT)

    for button in [REPLAY_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                play()
                Pgm.rungame()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

    pygame.display.update()