import pygame
import sys

from Spielfeld_Module import Spielfeld
from Ball_Modul import Ball

pygame.init()

spielfeld = Spielfeld()
spielfeld.SetSpielfeldRand(2, spielfeld.ROT)
spielfeld.UpdateSpielfeld()

ball = Ball()
ball.start()

# MainLoop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ball.quit()
            pygame.quit()
            sys.exit()
     
    # Tastenaktionen​
    tasten = pygame.key.get_pressed()
    if tasten[pygame.K_UP]:
        spielfeld.SetSpielfeldGroesse(600, 800)
    if tasten[pygame.K_DOWN]:
        spielfeld.SetSpielfeldGroesse(400, 600)
    if tasten[pygame.K_w]:
        spielfeld.SetSpielfeldFarbe(spielfeld.BLAU)
    if tasten[pygame.K_s]:
        spielfeld.SetSpielfeldFarbe((80,150,220))
    if tasten[pygame.K_r]:
        spielfeld.SetSpielfeldRand(2, spielfeld.WEISS)

