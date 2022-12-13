import pygame as pg
import random
import sys

#画面外に出たか判定
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()

    #背景設定
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    #こうかとんの設定
    tori_sfc = pg.image.load("fig/9.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) 

    #爆弾の設定
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    count = 0           #跳ね返った回数

    #爆弾の初期移動方向の設定
    move_bomb = [-1, 1]
    vx = move_bomb[random.randint(0, 1)]
    vy = move_bomb[random.randint(0, 1)]

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #経過時間を表示
        sec = pg.time.get_ticks()
        fonto = pg.font.Font(None, 80)
        txt = fonto.render(f"{sec/1000:.2f}", True, "BLACK")
        scrn_sfc.blit(txt, (800, 30))

        #こうかとんの移動
        key_dct = pg.key.get_pressed()
        bf_x = tori_rct.centerx
        bf_y = tori_rct.centery
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            tori_rct.centerx = bf_x
            tori_rct.centery = bf_y          
        scrn_sfc.blit(tori_sfc, tori_rct) 

        #爆弾の移動
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        #時間経過による爆弾の速度変化
        change_speed = 0.001
        if vx > 0:
            vx += change_speed
        else:
            vx -= change_speed
        if vy > 0:
            vy += change_speed
        else:
            vy -= change_speed

        #こうかとんとボールが重なった時
        if tori_rct.colliderect(bomb_rct):
            #「ゲームオーバー」の表示
            fonto = pg.font.Font(None, 120)
            txt1 = fonto.render("Game Over", True, "RED")
            txt2 = fonto.render(f"Your Score: {sec/1000:.1f} s", True, "BLACK")
            scrn_sfc.blit(txt1, (600, 300))
            scrn_sfc.blit(txt2, (500, 400))

            pg.display.update()
            #2秒の遅延後、終了する
            clock.tick(0.5)
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()