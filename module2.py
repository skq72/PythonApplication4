import pygame
pygame.init()
roheline=[0,255,0]
kollane=[255, 255, 0]
punane=[255, 0, 0]
black=[0,0,0]
hall=[128, 128, 128]
ekraani_pind=pygame.display.set_mode((300, 300))
pygame.display.set_caption("ül 1.1")
ekraani_pind.fill(black)
def korkaz():
    pygame.draw.rect(ekraani_pind, hall, (130, 70, 60, 180))

def cveta():
    pygame.draw.circle(ekraani_pind, roheline, (160, 220), 30)
    pygame.draw.circle(ekraani_pind, kollane, (160, 160), 30)
    pygame.draw.circle(ekraani_pind, punane, (160, 100), 30)
korkaz()
cveta()

#----------------
pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()