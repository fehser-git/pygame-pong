import pygame
import sys

pygame.init()

"""
schriftart = pygame.font.SysFont(None, 50)
alle_schriftarten = pygame.font.get_fonts()
for schriftart in alle_schriftarten:
    print(schriftart)

schriftart = pygame.font.SysFont("comicsansms", 50, italic=True, bold=False)
text = schriftart.render("Hello World!", True, pygame.Color("blue"), pygame.Color("red"))

bildschirm.blit(text, (0, 0))

"""


SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)

FENSTERHOEHE = 600
FENSTERBREITE = 800
FENSTERMITTEY = FENSTERHOEHE/2
FENSTERMITTEX = FENSTERBREITE/2

SCHLAEGERABSTAND = 20
SCHLAEGERBREITE = 16
SCHLAEGERHOEHE = 90
RECHTERSCHLAEGERX = FENSTERBREITE - SCHLAEGERABSTAND - SCHLAEGERBREITE

BALLGROESSE = 10


# Fenster
bildschirm = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
pygame.display.set_caption("Pong")

# Schläger​
linkerSchlaegerY = 50
rechterSchlaegerY = 50

SCHLAEGERGESCHWINDIGKEIT = 0.1
BALLGESCHWINDIGKEIT = 0.1

ballX = FENSTERMITTEX
ballY = FENSTERMITTEY

ballbewegungX = BALLGESCHWINDIGKEIT
ballbewegungY = BALLGESCHWINDIGKEIT

# MainLoop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 #   pygame.display.flip()
    
    # Tastenaktionen​
    tasten = pygame.key.get_pressed()
    if tasten[pygame.K_UP]:
        rechterSchlaegerY -= SCHLAEGERGESCHWINDIGKEIT
    if tasten[pygame.K_DOWN]:
        rechterSchlaegerY += SCHLAEGERGESCHWINDIGKEIT

    if tasten[pygame.K_w]:
        linkerSchlaegerY -= SCHLAEGERGESCHWINDIGKEIT
    if tasten[pygame.K_s]:
        linkerSchlaegerY += SCHLAEGERGESCHWINDIGKEIT

# Schläger definieren
    linkerSchlaeger = pygame.Rect(SCHLAEGERABSTAND, linkerSchlaegerY, SCHLAEGERBREITE, SCHLAEGERHOEHE)
    rechterSchlaeger = pygame.Rect(RECHTERSCHLAEGERX, rechterSchlaegerY, SCHLAEGERBREITE, SCHLAEGERHOEHE)

 # Elemente zeichnen​
    bildschirm.fill(SCHWARZ)  
    pygame.draw.rect(bildschirm, WEISS, rechterSchlaeger)
    pygame.draw.circle(bildschirm, WEISS, (FENSTERMITTEX, FENSTERMITTEY), BALLGROESSE)
    pygame.draw.rect(bildschirm, WEISS, linkerSchlaeger)

 #   pygame.display.flip()​

    if linkerSchlaegerY < 0:
       linkerSchlaegerY = 0
    if linkerSchlaegerY > FENSTERHOEHE - SCHLAEGERHOEHE:
       linkerSchlaegerY = FENSTERHOEHE - SCHLAEGERHOEHE

    if rechterSchlaegerY <= 0:
       rechterSchlaegerY = 0
    if rechterSchlaegerY >= FENSTERHOEHE - SCHLAEGERHOEHE:
       rechterSchlaegerY = FENSTERHOEHE - SCHLAEGERHOEHE

    ballX += ballbewegungX
    ballY += ballbewegungY

    if ballY < BALLGROESSE:
        ballbewegungY = BALLGESCHWINDIGKEIT
    if ballY > FENSTERHOEHE - BALLGROESSE:
        ballbewegungY = -BALLGESCHWINDIGKEIT

    if ballX <= BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY -100
        ballbewegungX = BALLGESCHWINDIGKEIT
        ballbewegungY = BALLGESCHWINDIGKEIT

    if ballX >= FENSTERBREITE - BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY - 100
        ballbewegungX *= -1
        ballbewegungY = BALLGESCHWINDIGKEIT

            # Kollision oben und unten
    if ballY < BALLGROESSE:
        ballbewegungY = BALLGESCHWINDIGKEIT

    if ballY > FENSTERHOEHE - BALLGROESSE:
        ballbewegungY = -BALLGESCHWINDIGKEIT

    # Kollision links und rechts
    if ballX <= BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY
        ballbewegungX = BALLGESCHWINDIGKEIT
        ballbewegungY = BALLGESCHWINDIGKEIT

    if ballX >= FENSTERBREITE - BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY
        ballbewegungX *= -1
        ballbewegungY = BALLGESCHWINDIGKEIT

    # Kollision Schläger
    ballRechteck = pygame.Rect(ballX-BALLGROESSE, ballY-BALLGROESSE, 2*BALLGROESSE, 2*BALLGROESSE)

    if linkerSchlaeger.colliderect(ballRechteck):
        ballX = linkerSchlaeger.right + BALLGROESSE
        ballbewegungX *= -1

    if rechterSchlaeger.colliderect(ballRechteck):
        ballX = rechterSchlaeger.left - BALLGROESSE
        ballbewegungX *= -1

    # Elemente zeichnen
    bildschirm.fill(SCHWARZ)

    pygame.draw.rect(bildschirm, WEISS, rechterSchlaeger)
    pygame.draw.circle(bildschirm, WEISS, (ballX, ballY), BALLGROESSE)
    pygame.draw.rect(bildschirm, WEISS, linkerSchlaeger)

    pygame.display.flip()

