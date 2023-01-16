
import pygame
import sys




class Spielfeld():

    SCHWARZ = (0, 0, 0)
    BLAU = (0, 0, 168)
    ROT = (200, 0, 0)
    WEISS = (255, 255, 255)
    BILDSCHIRM_RAND = 10

      
    def __init__(self):
        self.HoeheY = 600 
        self.BreiteX = 800 
        self.Farbe = self.SCHWARZ
        self.RandFarbe = self.SCHWARZ
        self.RandDicke = 1

        Spielfeld.Bildschirm = pygame.display.set_mode((self.BreiteX + self.BILDSCHIRM_RAND , self.HoeheY + self.BILDSCHIRM_RAND))
        pygame.display.set_caption("Pong")

        self.SetSpielfeldRand(2,self.ROT)
 

        print("Spielfeld: init ok")

    def SetSpielfeldGroesse(self, hoehe, breite):
        self.HoeheY = hoehe 
        self.BreiteX = breite 
        Spielfeld.Bildschirm = pygame.display.set_mode((self.BreiteX + self.BILDSCHIRM_RAND, self.HoeheY + self.BILDSCHIRM_RAND))
        self.UpdateSpielfeld()
        print("Spielfeldgröße gesetzt.")

    def SetSpielfeldFarbe(self, farbe):
        self.Farbe = farbe
        self.UpdateSpielfeld()
        print("Spielfeldgröße gesetzt.")


    def SetSpielfeldRand(self, staerke, farbe):
       self.RandDicke = staerke
       self.RandFarbe = farbe
       self.UpdateSpielfeld()

       print("SetSpielfeldRand gesetzt.")

    def UpdateSpielfeld(self):
        # Fenster
#        Spielfeld.Bildschirm.fill(self.Farbe)  
        pygame.draw.rect(Spielfeld.Bildschirm, self.RandFarbe, [self.BILDSCHIRM_RAND/2, self.BILDSCHIRM_RAND/2, self.BreiteX, self.HoeheY], self.RandDicke)  
        pygame.display.flip()

#        print("Spielfeld aktualisiert.")



