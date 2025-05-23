#Majake
import random
import pygame
import sys
pygame.init()
#värvid
punane = [255,0,0]
roheline = [0, 255, 0]
sinine = [0, 0, 255]
roosa = [255, 153, 255]
black=[255,255,255]
lRoheline = [153, 255, 153]
#ekraani seaded
ekraani_laius=1000
ekraani_kõrgus=650
pind=pygame.display.set_mode([ekraani_laius,ekraani_kõrgus])
pygame.display.set_caption("Majake")
pind.fill(lRoheline)


maja_l=ekraani_laius*(1/3)
maja_k=ekraani_kõrgus*(1/2)
x=(ekraani_laius-maja_l)/2
y=(ekraani_kõrgus+maja_k*(3/4))/2
#funktsioonid
def drawHouse(x, y, laius, kõrgus, ekraan, värv):
    punktid = [(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius, y-(3/4.0) * kõrgus), (x,y- ((3/4.0) * kõrgus)), (x + laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    lineThickness = 5
    pygame.draw.lines(ekraan, värv, False, punktid, lineThickness)
def drawDoor(x, y, laius, kõrgus, ekraan, värv):
    door_width=laius/4
    door_height=kõrgus/2
    door_x= x+(laius-door_width)/2
    door_y= y-door_height
    points = [(door_x,y), (door_x,door_y), (door_x+door_width,door_y), (door_x+door_width, y),(door_x,y)]
    lineThickness = 5
    pygame.draw.lines(ekraan, värv, False, points, lineThickness)
def drawWindow(x, y, laius, kõrgus, ekraan, värv):
    window = laius / 5
    wx=x+laius *(1/6)
    wy=y-kõrgus *(1/2)
    aken=[(wx, wy),(wx + window, wy),(wx + window, wy + window),(wx, wy + window),(wx, wy)]
    lineThickness = 5
    pygame.draw.lines(ekraan, True, värv, aken , lineThickness)

def drawDimahod(x, y, laius, kõrgus, ekraan, värv):
    d_l = laius/10
    d_k = kõrgus/4
    d_x = x + laius*0.7
    d_y =y-kõrgus-d_k+60
    dimahod = [(d_x, d_y + d_k),(d_x, d_y),(d_x + d_l, d_y),(d_x + d_l, d_y + d_k),(d_x, d_y + d_k)]
    lineThickness = 3
    pygame.draw.lines(ekraan, False, värv, dimahod, lineThickness)

#kutsun funktsiooni välja
drawHouse(x,y,maja_l,maja_k,pind, punane)
drawDoor(x,y,maja_l,maja_k,pind, punane)
drawWindow(x,y,maja_l,maja_k,pind, black)
drawDimahod(x,y,maja_l,maja_k,pind,black)
pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
