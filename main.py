import pygame
import time

pygame.init()
ekran = pygame.display.set_mode((350, 500))
krecha = []
run = True
szary = (125, 125, 125)
zielony = (0, 255, 0)
niebieski = (0, 0, 255)
kolo = zielony
kolej = 0
font = pygame.font.Font('freesansbold.ttf', 20)
wygrana = 0
clock = pygame.time.Clock()


class Linie:
    def __init__(self, kolor, x, y, xx, yy):
        self.kolor = kolor
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy

    def rysowanie(self):
        pygame.draw.line(ekran, self.kolor, (self.x, self.y), (self.xx, self.yy), 5)


def zmiana():
    for x in range(1, i):
        krecha[x].kolor = szary


def liczenie():
    global i
    i = 0
    for x in krecha:
        i += 1


def sciany():
    for y in range(25, 450, 25):
        krecha.append(Linie(szary, 25, y, 25, y + 25))
        krecha.append(Linie(szary, 325, y, 325, y + 25))
    for x in range(25, 125, 25):
        krecha.append(Linie(szary, x, 25, x + 25, 25))
        krecha.append(Linie(szary, x, 450, x + 25, 450))
    for x in range(225, 325, 25):
        krecha.append(Linie(szary, x, 25, x + 25, 25))
        krecha.append(Linie(szary, x, 450, x + 25, 450))


def wygranan():
    wynik = font.render(("wygrana niebieskich"), True, (0, 0, 255))
    ekran.fill((0, 0, 0))
    ekran.blit(wynik, (50, 175))


def wygranag():
    wynik = font.render(("wygrana zielonych"), True, (0, 255, 0))
    ekran.fill((0, 0, 0))
    ekran.blit(wynik, (50, 175))


def bramki():
    pygame.draw.rect(ekran, zielony, (125, 0, 100, 25))
    pygame.draw.rect(ekran, niebieski, (125, 450, 100, 25))


def powatarzanie():
    global i
    if i >= 2:
        for x in range(1, i):
            if krecha[0].xx == krecha[x].x and krecha[x].xx == krecha[0].x:
                if krecha[0].yy == krecha[x].y and krecha[x].yy == krecha[0].y:
                    krecha.remove(krecha[0])
                    i -= 1
        for x in range(1, i):
            if krecha[0].xx == krecha[x].xx and krecha[x].x == krecha[0].x:
                if krecha[0].yy == krecha[x].yy and krecha[x].y == krecha[0].y:
                    krecha.remove(krecha[0])
                    i -= 1


def odbijanie():
    global i, kolej, kolo
    ile = 0
    for x in range(1, i):
        if krecha[0].xx == krecha[x].x and krecha[0].yy == krecha[x].y:
            ile += 1
        elif krecha[0].xx == krecha[x].xx and krecha[0].yy == krecha[x].yy:
            ile += 1
    if ile == 7:
        krecha.remove(krecha[0])
        i -= 1
    if ile == 0:
        zmiana()
        kolej += 1
        kolorek()
        krecha[0].kolor = kolo


def kolorek():
    global kolo
    if kolej % 2 == 0:
        kolo = zielony
    else:
        kolo = niebieski


def redraw():
    global wygrana
    ekran.fill((0, 0, 0))
    bramki()
    liczenie()
    for x in range(i):
        Linie.rysowanie(krecha[x])
    mapa()
    pygame.draw.circle(ekran, (255, 0, 0), (krecha[0].xx, krecha[0].yy), 2)

    if wygrana == 1:
        wygranan()
        wygrana = 0
        krecha.clear()
        krecha.append(Linie(szary, 175, 250, 175, 250))
        sciany()
        pygame.display.update()
        time.sleep(3)

    elif wygrana == 2:
        wygranag()
        wygrana = 0
        krecha.clear()
        krecha.append(Linie(szary, 175, 250, 175, 250))
        sciany()
        pygame.display.update()
        time.sleep(3)
    pygame.display.update()


sciany()


def ruch(mx, my):
    global wygrana
    wherex = mx - krecha[0].xx
    wherey = my - krecha[0].yy
    kolorek()
    if 125 < mx < 225 and -33 < wherex < 33:
        if 0 < my < 25 and -33 < wherey < 33:
            wygrana += 1
        elif 450 < my < 475 and -33 < wherey < 33:
            wygrana += 2
    if 17 < mx < 333 and 17 < my < 458:
        if -8 < wherex < 8 and 17 < wherey < 33:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx, krecha[0].yy + 25))

        elif -8 < wherex < 8 and -33 < wherey < -17:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx, krecha[0].yy - 25))

        elif 17 < wherex < 33 and 17 < wherey < 33:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx + 25, krecha[0].yy + 25))

        elif -33 < wherex < -17 and -33 < wherey < -17:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx - 25, krecha[0].yy - 25))

        elif 17 < wherex < 33 and -33 < wherey < -17:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx + 25, krecha[0].yy - 25))

        elif -33 < wherex < -17 and 17 < wherey < 33:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx - 25, krecha[0].yy + 25))

        elif 17 < wherex < 33 and -8 < wherey < 8:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx + 25, krecha[0].yy))

        elif -33 < wherex < -17 and -8 < wherey < 8:
            krecha.insert(0, Linie(kolo, krecha[0].xx, krecha[0].yy, krecha[0].xx - 25, krecha[0].yy))
        powatarzanie()
        odbijanie()
        pygame.display.update()


def mapa():
    for x in range(25, 350, 25):
        for y in range(25, 475, 25):
            pygame.draw.circle(ekran, (255, 255, 255), (x, y), 2)


krecha.insert(0, Linie(szary, 175, 250, 175, 250))
while run:
    clock.tick(60)
    # liczenie()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            ruch(mx, my)

    redraw()
