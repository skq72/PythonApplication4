import pygame
def paike():
    x=400
    y=0
    for i in range(50):
        x-=10
        y+=10
        if i in [10, 20]:
            pygame.draw.line(ekraani_pind, kollane, (0, 0), (x+i, y+i), 5)
        else:
             pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y),5)


def cvetok():
    x=400
    y=300
    i=2
    for k in range(16):
        i+=6
        pygame.draw.circle(ekraani_pind, hall, (x, y),i,3)

def p4ela():
    pilt1=pygame.image.load("p4ela.png")
    pilt1=pygame.transform.scale(pilt1, (100, 100))
    ekraani_pind.blit(pilt1, (300, 200))
    ekraani_pind.blit(pilt1, (500, 350))

def oblako():
    pygame.draw.circle(ekraani_pind, hall, (600, 200), 60)
    pygame.draw.circle(ekraani_pind, hall, (550, 150), 50)

pygame.init()
roheline=[0,255,0]
kollane=[255, 255, 0]
punane=[255, 0, 0]
sinine=[0, 0, 255]
hall=[128, 128, 128]
pruun=[139, 69, 19]
lilla=[255,50,230]
ekraani_pind=pygame.display.set_mode((800, 600))


ekraani_pind=pygame.display.set_mode((800, 600))
pygame.display.set_caption("ül 1.1")
ekraani_pind.fill(sinine)
pygame.draw.rect(ekraani_pind, roheline, (0, 400, 800, 300))
paike()
pygame.draw.rect(ekraani_pind, pruun, (390, 400, 25, 125))
pygame.draw.circle(ekraani_pind, lilla, (400, 300), 100)
font=pygame.font.SysFont("Arial", 50)
sõnum="Tere tulemast!!"
teksti_lisamine=font.render(sõnum, True, punane)
ekraani_pind.blit(teksti_lisamine, (500, 50))
cvetok()
p4ela()
oblako()
#-------------------------------------------------
pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()