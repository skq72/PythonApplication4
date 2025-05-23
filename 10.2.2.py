import pygame
import random
pygame.init()
lfon = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
ekraan_k=random.randint(400,800)
ekraan_l=random.randint(400,800)

pind=pygame.display.set_mode([ekraan_k,ekraan_l])
pygame.display.set_caption("Harjutamine")
pind.fill(lfon)

def joonista_ruudustik(pind,ruudu_l,ruudu_k, rida, veerud):
    for rida in range(rida):
        for veerg in range(veerud):
            värv=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            x=veerg*ruudu_l
            y=rida*ruudu_k
            pygame.draw.rect(pind,värv,(x,y,ruudu_l, ruudu_k),1)
            
ruudu_k=random.randint(10,50)
ruudu_l=random.randint(10,50)
read=ekraan_l//ruudu_l+1
veerud=ekraan_k//ruudu_k+1

joonista_ruudustik(pind,ruudu_k,ruudu_l,read,veerud)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()

hh