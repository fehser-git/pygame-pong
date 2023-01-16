
import threading
import time
from random import randint

import pygame
import sys
import math

from Spielfeld_Modul import Spielfeld

pygame.init()

spielfeld = Spielfeld()


class Ball(threading.Thread):

    SCHWARZ = (0, 0, 0)
    BLAU = (0, 0, 168)
    ROT = (200, 0, 0)
    WEISS = (255, 255, 255)

 
    def __init__(self):
        threading.Thread.__init__(self)
        self.SpeedAccelarator = 0
        self.Durchmesser = 10 
        self.Farbe = self.SCHWARZ
        self.PositionX = 200
        self.PositionY = 200
        self.Speed = 400

        self.Winkel = 270
 

        self.Bildschirm = spielfeld.Bildschirm

        pygame.draw.circle(self.Bildschirm, Ball.ROT, (self.PositionX, self.PositionY), self.Durchmesser)
        print("Ball: init ok")

    def Bewege(self, winkel, speed):
        self.Winkel = winkel
        self.Speed = speed

    def SetPosition(self, x, y):
        self.PositionX = x
        self.SpPositionX = y

    def CalculatePosition(self):
        if (self.PositionX <= spielfeld.BILDSCHIRM_RAND + self.Durchmesser/2):
            self.Winkel = self.ReflectionX(self.Winkel)
        if (self.PositionX >= spielfeld.BreiteX - self.Durchmesser/2):
            self.Winkel = self.ReflectionX(self.Winkel)
        if (self.PositionY <= spielfeld.BILDSCHIRM_RAND + self.Durchmesser/2):
            self.Winkel = self.ReflectionY(self.Winkel)
        if (self.PositionY >= spielfeld.HoeheY - self.Durchmesser/2):
            self.Winkel = self.ReflectionY(self.Winkel)

        self.Winkel = self.Winkel % 360


        deltaX = math.sin(math.radians(self.Winkel)) * 5
        deltaY = math.cos(math.radians(self.Winkel)) * 5
        self.PositionX += round(deltaX)
        self.PositionY += round(deltaY)

    def ReflectionX(self, winkel):

        linkerRand = (self.PositionX < spielfeld.BreiteX/2)

        quadrant = round((winkel / 90) + 0.5) # Calculate quartal 1 ... 4
 #       print("ReflectionX: winkel = " + str(winkel) + " quartal= " + str(quadrant))

        if (winkel == 90):
            return 290
        if (winkel == 270):
            return 60

        if (quadrant == 1 and not linkerRand):
            winkel = 360 - winkel
        if (quadrant == 2 and not linkerRand):
            winkel = 180 + (180 - winkel)
        if (quadrant == 3 and linkerRand):
            winkel = 90 + (270 - winkel)
        if (quadrant == 4 and linkerRand):
            winkel = 360 - winkel
            

        return winkel

    def ReflectionY(self, winkel):

        obererRand = (self.PositionY>spielfeld.HoeheY/2)
        quadrant = round((winkel / 90) + 0.5) # Calculate quartal 1 ... 4

 #       print("ReflectionY: winkel = " + str(winkel) + " quartal= " + str(quadrant))

        if (winkel == 0):
            return 160
        if (winkel == 180):
            return 20

        if (quadrant == 1 and obererRand):
            winkel = 90 + winkel
        if (quadrant == 2 and not obererRand):
            winkel = winkel-90
        if (quadrant == 3 and not obererRand):
            winkel = 270 + (winkel-180)
        if (quadrant == 4 and obererRand):
            winkel = 180 + (winkel-270)
        return winkel

        

    def run(self):
        while True:
            skipCounter = self.Speed / 100
            self.SpeedAccelarator += 1
            if (self.SpeedAccelarator > skipCounter):
                pause = 1/self.Speed    # (1 Sekunde / Speed) ---> je höher Speed desto kleiner die Pause!
                time.sleep(pause)
                self.SpeedAccelarator = 0
            self.CalculatePosition()
            spielfeld.Bildschirm.fill(spielfeld.Farbe)
            pygame.draw.circle(self.Bildschirm, Ball.ROT, (self.PositionX, self.PositionY), self.Durchmesser)
            spielfeld.UpdateSpielfeld()
#            pygame.display.flip()

