import os
from button import Button
import pygame
from pygame import mixer
from button import Button
import sys
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#Importing Music
mixer.init()
pygame.mixer.music.load('Smells Like Burning Corpse.mp3')

#Looping Music
pygame.mixer.music.play(-1)
width = 750
height = 750

#Size of square
size = 48
window = pygame.display.set_mode((width,height))

#Setting Caption & Icon
caption = pygame.display.set_caption("Caro")
icon = pygame.image.load(os.path.join('ASSETS',"carologo.png"))

#Importing Sprites
picX = pygame.image.load(os.path.join('ASSETS',"Xtac.png"))
picO = pygame.image.load(os.path.join('ASSETS',"Otac.png"))
X = pygame.transform.scale(picX,(size,size))
O = pygame.transform.scale(picO,(size,size))

# Setting FPS And Colors
FPS = 70
BLACK = (36,36,36)
WHITE = (230,241,243)
RED = (153,0,0)
TURQUOISE = (72,209,204)

pygame.display.set_icon(icon)



dia=[1,15,16,14]


def rungame():
    #Creating Array-Backed Grid
    gridarr = [[0 for x in range(15)] for y in range(15)]
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    #Check If It Is Player 2's Turn
    p1t = True

    #Player 1 & PLayer 2 Input Lists
    plr1 = []
    plr2 = []
    p1w = True
    end = False



    #Cheking For Winner
    def win_able(plr,blockno):
        for k in range(4):
                dia=[1,15,16,14]
                def win_check(blockno,dia,k):
                        h=m=blockno
                        countlef=0
                        countrig=0
                        l=True
                        r=True
                        for j in range(5):
                            h+=dia[k]
                            if r==True:
                                if  k!= 1 :
                                    if ((h+1)%15==0 and (h+1) in plr) or (h%15==0 and h in plr):
                                        countrig+=1
                                        r=False
                            if r==True:
                                if h in plr:
                                    countrig+=1
                                else:
                                     h=blockno
                                     r=False
                            if l==True:
                                if k!= 1:
                                    if ((m+1)%15==0 and (m+1) in plr)or (m%15==0 and m in plr):

                                        countlef+=1
                                        l=False
                            if l==True:
                                if m in plr:
                                    countlef+=1
                                else:
                                     m=blockno
                                     l=False
                                m-=dia[k]
                        if countlef+countrig>=5:
                            return 1
                result= win_check(blockno,dia,k)
                if result==1:
                    print("you win")
                    return 1

    #Checking If Click Is First Click
    firstclick = True
    while run:
        #Setting Background Color
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                #Getting Mouse Position
                pos = pygame.mouse.get_pos()
                #Input Block Number
                blockno = (pos[0]//(2+size) + (pos[1]//(2+size))*15)
                #Update gridarr With X or O By Checking Player Turn (p1t)
                if gridarr[pos[0]//(2+size)][pos[1]//(2+size)] == 0:
                    if (blockno in plr1) or (blockno in plr2):
                        p1t = p1t
                    else:
                        p1t = not p1t
                    if not firstclick and not end:
                        if p1t:
                            gridarr[pos[0]//(2+size)][pos[1]//(2+size)] = 'X'
                            plr1.append(blockno)
                            result = win_able(plr1,blockno)
                            if result == 1:
                                end = True
                                p1w = True
                        else:
                            gridarr[pos[0]//(2+size)][pos[1]//(2+size)] = 'O'
                            plr2.append(blockno)
                            result = win_able(plr2,blockno)
                            if result==1:
                                end = True
                                p1w = False

                if firstclick == True:
                    firstclick = False

        #Printing Squares Using gridarr
        for x in range(0,15):
            for y in range(0, 15):
                if gridarr[x][y] == 0:
                    color = BLACK
                    rectum = pygame.Rect(x*(2+size), y*(2+size), size, size)
                    pygame.draw.rect(window,color, rectum)
                elif gridarr[x][y] == 'X':

                    window.blit(X, (x*(2+size), y*(2+size)))
                elif gridarr[x][y] == 'O':

                    window.blit(O, (x*(2+size), y*(2+size)))

        #Check If A Player Has Wonw
        if end:
            #Drawing End Screen
            poplft = width//8
            poptop = height//3
            popwdt = width*(6/8)
            pophgt = height//3
            winpop = pygame.Rect(poplft, poptop, popwdt, pophgt)
            pygame.draw.rect(window, BLACK, winpop)
            pygame.draw.rect(window,WHITE, winpop, 1)
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            #Checking Winner
            if p1w:
                MENU_TEXT = get_font(45).render("P1 WINS", True, "#b68f40")
            elif not p1w:
                MENU_TEXT = get_font(45).render("P2 WINS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(370, 300))

            #Replay and Quit Buttons
            REPLAY_BUTTON = Button(image=None, pos=(220, 400),
                                 text_input="REPLAY", font=get_font(25), base_color="White", hovering_color="#8cdb6a")

            QUIT_BUTTON = Button(image=None, pos=(550, 400),
                                 text_input="QUIT", font=get_font(25), base_color="White", hovering_color="#8cdb6a")
            #Drawing Text
            window.blit(MENU_TEXT, MENU_RECT)

            #Drawing Buttons
            for button in [REPLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)

            #Check For Replay Or Quit
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        end = False
                        firstclick = True
                        gridarr = [[0 for x in range(15)] for y in range(15)]
                        p1t = True
                        p1w = True
                        plr1 = []
                        plr2 = []

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
            pygame.display.update()

                

        pygame.display.update()
        clock.tick(FPS)



    pygame.quit()

if __name__ == "__main__":
    rungame()
