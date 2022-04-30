import os

import pygame
from pygame import mixer
mixer.init()
pygame.mixer.music.load('Smells Like Burning Corpse.mp3')
#play the music infinitely
pygame.mixer.music.play(-1)
width = 750
height = 750
#Size of square
size = 48
window = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("The Eye")
icon = pygame.image.load(os.path.join('ASSETS',"Jupe.png"))
#Importing Sprites
picX = pygame.image.load(os.path.join('ASSETS',"Xtac.png"))
picO = pygame.image.load(os.path.join('ASSETS',"Otac.png"))
X = pygame.transform.scale(picX,(size,size))
O = pygame.transform.scale(picO,(size,size))


FPS = 30
BLACK = (36,36,36)
WHITE = (230,241,243)
RED = (153,0,0)
TURQUOISE = (72,209,204)

pygame.display.set_icon(icon)
#Creating array-backed grid
gridarr = [[0 for x in range(15)] for y in range(15)]

dia=[1,15,16,14]


def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    #Check if it is Player 1's turn
    p2t = True
    #Check if Player 1'

    #Player 1 and PLayer 2 input lists
    plr1 = []
    plr2 = []
    #Win Display
    def windisplay():
        poplft = width//8
        poptop = height//3
        popwdt = width *(6/8)
        pophgt = height//3
        winpop = pygame.Rect(poplft, poptop, popwdt, pophgt)
        pygame.draw.rect(window, TURQUOISE, winpop)

    #Cheking for wins
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
                        print('left, right:',countlef,countrig)
                        if countlef+countrig>=5:
                            return 1
                result= win_check(blockno,dia,k)
                if result==1:
                    print("you win")
                    return 1

    while run:

        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                #Getting mouse position
                pos = pygame.mouse.get_pos()
                #Input block number
                blockno = (pos[0]//(2+size) + (pos[1]//(2+size))*15)
                blocklefttop = (pos[0]//(2+size)*(2+size), pos[1]//(2+size)*(2+size))
                #Update gridarr with X or O
                if gridarr[pos[0]//(2+size)][pos[1]//(2+size)] == 0:
                    if (blockno in plr1) or (blockno in plr2):
                        p2t = p2t
                    else:
                        p2t = not p2t
                    if not p2t:
                        gridarr[pos[0]//(2+size)][pos[1]//(2+size)] = 'X'
                        plr1.append(blockno)
                        result = win_able(plr1,blockno)
                        if result == 1:
                            run = False
                    else:
                        gridarr[pos[0]//(2+size)][pos[1]//(2+size)] = 'O'
                        plr2.append(blockno)
                        result = win_able(plr2,blockno)
                        if result==1:
                            run = False

                print('blk:',blockno)
                print('plr1:', plr1)
                print('plr2:', plr2)


        for x in range(0,15):
            for y in range(0, 15):

                if gridarr[x][y] == 0:
                    color = BLACK
                    rectum = pygame.Rect(x*(2+size), y*(2+size), size, size)
                    pygame.draw.rect(window,color, rectum)
                elif gridarr[x][y] == 'X':
                    #color = RED
                    #rectum = pygame.Rect(x*(2+size), y*(2+size), size, size)
                    #pygame.draw.rect(window,color, rectum)
                    window.blit(X, (x*(2+size), y*(2+size)))
                elif gridarr[x][y] == 'O':
                    #color = TURQUOISE
                    #rectum = pygame.Rect(x*(2+size), y*(2+size), size, size)
                    #pygame.draw.rect(window,color, rectum)
                    window.blit(O, (x*(2+size), y*(2+size)))
        pygame.display.update()
        clock.tick(FPS)



    pygame.quit()

if __name__ == "__main__":
    main()
