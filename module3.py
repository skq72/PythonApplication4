import pygame

pygame.init()
sinine=[0, 0, 255]
hall=[128, 128, 128]
v=[255,255,255]
ekraani_pind=pygame.display.set_mode((640, 480))
pygame.display.set_caption("3")
ekraani_pind.fill(sinine)
pilt1=pygame.image.load("fonnn.webp")
pilt1=pygame.transform.scale(pilt1, (640, 480))
ekraani_pind.blit(pilt1, (0, 0))
pilt1=pygame.image.load("mes.png")
pilt1=pygame.transform.scale(pilt1, (100, 100))
ekraani_pind.blit(pilt1, (140, 200))
font=pygame.font.SysFont('Arial',10)
sõnum="On vaja KOJU!!"
teksti_lisamine=font.render(sõnum, True, v)
ekraani_pind.blit(teksti_lisamine, (150, 200))



#--------------
pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()