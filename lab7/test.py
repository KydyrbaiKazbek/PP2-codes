import pygame as g
g.init()

win = g.display.set_mode((500, 500))

g.display.set_caption("Test Prog")

x=50
y=50
width = 40
hight = 60
vel = 5

run = True

while run:
    g.time.delay(100)
    for event in g.event.get():
        if event.type == g.QUIT:
            run = False
    keys = g.key.get_pressed()
    
    if keys[g.K_LEFT]: x-=vel
    if keys[g.K_RIGHT]: x+=vel
    if keys[g.K_UP]: y-=vel
    if keys[g.K_DOWN]: y+=vel
    win.fill((0,0,0))
    g.draw.rect(win, (100, 200, 50), (x, y, width, hight))
    g.display.update()


g.quit()

