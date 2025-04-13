import pygame
pygame.mixer.init()
pygame.init()
running=True
screen=pygame.display.set_mode((600, 600))
mus1=pygame.transform.scale(pygame.image.load(r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\images\flag.jpg"),(612, 408))
mus2=pygame.transform.scale(pygame.image.load(r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\images\Sarah.png"),(600, 600))
mus3=pygame.transform.scale(pygame.image.load(r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\images\Rauf&Faik.jpeg"),(600, 600))
arrP=[mus1, mus2, mus3]
arrM=[
r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\audios\kazakhstan_2006.mp3",
r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\audios\Czardas.mp3",
r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab7\audios\Вечера.mp3"
]
index=0
pygame.mixer.music.load(arrM[index])
pygame.mixer.music.play()
paused=False
while running:
    screen.fill((0,0,0))
    screen.blit(arrP[index], (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                index=(index+1)%3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_a:
                index = (index - 1) % 3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
