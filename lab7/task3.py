import pygame

pygame.init()
running=True
screen=pygame.display.set_mode((500,500))

fon=(0,255,0)
screen.fill(fon)
cordX=250
cordY=250
step = 20
while running:
    screen.fill(fon)
    pygame.draw.circle(screen,"red",(cordX,cordY),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and cordY>45:
                    cordY-=step
            if event.key==pygame.K_s and cordY<455:
                    cordY+=step
            if event.key==pygame.K_d and cordX<455:
                    cordX+=step
            if event.key==pygame.K_a and cordX>45:
                    cordX-=step