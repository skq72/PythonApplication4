#Esimene mäng
import pygame
import sys

# from pygame import event
# pygame.init() #Pygame'i tööle rakendamiseks
# #värvid
# lRoheline = [153, 255, 153]
# lSinine = [153, 204, 255]

# ekraani_pind = pygame.display.set_mode( (640, 480))
# ekraani_pind.fill( lRoheline )
# pygame.display.set_caption("Esimene mäng")
# gameover = False
# while not gameover:
#     #Lisame pildid
#     sinaVõidad = pygame.image.load("pilti.png")
#     sinaVõidad = pygame.transform.scale(sinaVõidad, [300, 200])
#     ekraani_pind.blit(sinaVõidad, [180,100])

#     pygame.display.flip()
#     #mängu sulgemine ristist
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
# pygame.quit() #Pygame välja lülitamine




#Juhuslikud kujundit
import random
# pygame.init()
# #värvid
# r=random.randint(0, 255)
# g=random.randint(0, 255)
# b=random.randint(0, 255)

# varv = [r, g, b]
# lRoheline = [153, 255, 153]

# pind=pygame.display.set_mode([640,480])
# pygame.display.set_caption("Juhuslikud kujundid")
# pind.fill(lRoheline)

# for i in range (1,10):
#     x = random.randint(0, 620)
#     y = random.randint(0, 460)
#     pygame.draw.rect(pind, varv, [x, y, 20, 20])

#     pygame.display.flip()

# while True:
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         break
# pygame.quit()


#Majake
pygame.init()
#värvid
punane = [255,0,0]
roheline = [0, 255, 0]
sinine = [0, 0, 255]
roosa = [255, 153, 255]
lRoheline = [153, 255, 153]
#ekraani seaded
pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Majake")
pind.fill(lRoheline)

#funktsioonid
def drawHouse(x, y, laius, kõrgus, ekraan, värv):
    punktid = [(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius, y-(3/4.0) * kõrgus), (x,y- ((3/4.0) * kõrgus)), (x + laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    lineThickness = 5
    pygame.draw.lines(ekraan, värv, False, punktid, lineThickness)
#kutsun funktsiooni välja
drawHouse(100,400,300,400,pind, punane)
pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()