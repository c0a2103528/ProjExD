import pygame as pg
import random
import sys

class Screen:
    def __init__(self, title, wh, file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],}

    def __init__(self, fig, rate, xy):
        self.sfc = pg.image.load("fig/6.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scn):
        scn.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr):
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self, col, r, sp, scr):
        self.sfc = pg.Surface((20, 20))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, col, (10, 10), r)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx = sp[0]
        self.vy = sp[1]
    
    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    SR = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    
    tori = Bird("fig/0.png", 2.0, (900, 400))

    colors = ["Red", "Blue", "Green", "White", "Yellow"]
    bombs = []
    for i in range(5):
        color = colors[i]
        vx = random.choice([-1, 1])
        vy = random.choice([-1, 1])
        bombs.append(Bomb(color, 10, (vx, vy), SR))

    while True:
        SR.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tori.update(SR)

        for bomb in bombs:
            bomb.update(SR)
            if tori.rct.colliderect(bomb.rct):
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()