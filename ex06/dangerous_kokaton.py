import pygame as pg
import random
import sys


# スクリーンの設定
class Screen:
    def __init__(self, title, wh, file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
    
class BackGround:
    def __init__(self, file, xy):
        self.sfc = pg.image.load(file)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    def blit(self, scn):
        scn.sfc.blit(self.sfc, self.rct)

# 操作キャラの設定
class Bird:

    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],}

    def __init__(self, fig, rate, xy):
        self.rate = rate
        self.sfc = pg.image.load(fig)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, self.rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scn):
        scn.sfc.blit(self.sfc, self.rct)

    # 入力キーによって移動 
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
    
    # 画像の変更
    def change_image(self, fig):
        self.sfc = pg.image.load(fig)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, self.rate)


# 爆弾の設定
class Bomb:
    def __init__(self, col, r, sp, scr):
        self.sfc = pg.Surface((r*2, r*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, col, (r, r), r)
        self.rct = self.sfc.get_rect()

        pos = random.randint(0, 3)  #爆弾の飛んでくる方向(左,上,右,下)
        rad_x = random.randint(0, scr.rct.width)
        rad_y = random.randint(scr.rct.height-500, scr.rct.height)
        bombx = [10, rad_x, scr.rct.width-10, rad_x]    #飛んでくる方向によって
        bomby = [rad_y, 410, rad_y, scr.rct.height-10]  #爆弾の進む向き、初期位置を設定
        vx = [1, sp[0], -1, sp[0]]
        vy = [sp[1], 1, sp[1], -1]
        self.rct.centerx = bombx[pos]
        self.rct.centery = bomby[pos]
        self.vx = vx[pos]
        self.vy = vy[pos]
    
    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr, bmlist):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        if (yoko == -1) or (tate == -1):
            self.restart(scr)
        self.blit(scr)

    #新しく爆弾を出現させる
    def restart(self, scr):
        pos = random.randint(0, 3)
        x = random.choice([-1, 1])
        y = random.choice([-1, 1])
        rad_x = random.randint(0, scr.rct.width)
        rad_y = random.randint(scr.rct.height-500, scr.rct.height)
        bombx = [10, rad_x, scr.rct.width-10, rad_x]
        bomby = [rad_y, 410, rad_y, scr.rct.height-10]
        vx = [1, x, -1, x]
        vy = [y, 1, y, -1]
        self.rct.centerx = bombx[pos]
        self.rct.centery = bomby[pos]
        self.vx = vx[pos]
        self.vy = vy[pos]


# 画面端にぶつかったか検知
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.bottom - 500 or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


class Protecter:

    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],}

    def __init__(self, rate, bird):
        self.rate = rate
        self.sfc = pg.image.load("fig/barrior.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, self.rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird.rct.centerx, bird.rct.centery
        self.count = 3
    
    def blit(self, scn):
        scn.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        if self.count <= 0:
            self.delete(scr)
        key_dct = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)
    
    def delete(self, scr):
        self.rct.centerx = 2000
        self.rct.centery = 2000


def main():
    clock = pg.time.Clock()
    # スクリーンの表示
    SR = Screen("戦え！こうかとん", (600, 900), "fig/bg.png")
    GD = BackGround("fig/gd.png", (SR.rct.right/2, SR.rct.bottom-250))

    # 操作キャラ
    tori = Bird("fig/6.png", 1.0, (200, 600))
    tori.update(SR)

    prot = Protecter(1.0, tori)
    prot.update(SR)

    #爆弾設定
    bombs = []
    num = 15
    for i in range(num):
        vx = random.choice([-1, 1])
        vy = random.choice([-1, 1])
        bombs.append(Bomb("blue", 5, (vx, vy), SR))
        bombs[i].update(SR, bombs)

    while True:
        SR.blit()
        GD.blit(SR)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        # 操作キャラの位置更新
        tori.update(SR)
        prot.update(SR)

        # ゲームオーバーの設定
    
        for bomb in bombs:
            bomb.update(SR, bombs)
            if prot.rct.colliderect(bomb.rct):
                bomb.restart(SR)
                prot.count -= 1
            if tori.rct.colliderect(bomb.rct):
                SR.blit()
                GD.blit(SR)
                tori.change_image("fig/10.png")
                tori.update(SR)
                pg.display.update()

                clock.tick(0.5)
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()