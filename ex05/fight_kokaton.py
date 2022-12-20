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

    def stop(self, scr):
        self.vx = 0
        self.vy = 0
        self.rct.centerx = scr.rct.width + 50
        self.rct.centery = scr.rct.height + 50
        self.blit(scr)


# 剣の設定
class Sword:

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


# テキストの設定
class Text:
    def __init__(self, txt, col, scr, xy):
        self.fonto = pg.font.Font(None, 120)
        self.text = self.fonto.render(txt, True, col)
        scr.sfc.blit(self.text, xy)


# 跳ね返りの確認
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1*1.15
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1*1.15
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # スクリーンの表示
    SR = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 操作キャラ、剣の表示
    tori = Bird("fig/6.png", 2.0, (900, 500))
    tori.update(SR)
    sw = Sword("fig/ken1.png", 0.2, (855, 500))
    sw.update(SR)

    #爆弾の色設定、進行方向の設定、表示
    colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
    bombs = []
    for i in range(5):
        vx = random.choice([-1, 1])
        vy = random.choice([-1, 1])
        color = colors[i % 5]
        bombs.append(Bomb(color, 20, (vx, vy), SR))
        bombs[i].update(SR)

    while True:
        SR.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        # 操作キャラ・剣の位置更新
        tori.update(SR)
        sw.update(SR)

        # 陸上・空中によって画像変更
        if (tori.rct.centery < 450):
            tori.change_image("fig/3.png")
        elif (tori.rct.centery >= 450):
            tori.change_image("fig/5.png")

        # 爆弾と剣がぶつかった時、爆弾が消える
        for bomb in bombs:
            if sw.rct.colliderect(bomb.rct):
                bomb.stop(SR)

        # ゲームオーバーの設定
        for bomb in bombs:
            bomb.update(SR)
            if tori.rct.colliderect(bomb.rct):
                SR.blit()
                tori.change_image("fig/10.png")
                tori.update(SR)

                # ゲームオーバーテキストの表示
                go_txt = Text("Game Over!", "Red", SR, (600, 300))
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