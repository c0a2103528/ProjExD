import pygame as pg
import random
import sys

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    #Clockオブジェクトの作成
    clock = pg.time.Clock()

    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    #背景の設定
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #こうかとんを表示
    pg_sfc = pg.image.load("fig/9.png")
    pg_sfc = pg.transform.rotozoom(pg_sfc, 0, 2.0)
    pg_rct = pg_sfc.get_rect()
    pg_rct.center = 900, 400
    scrn_sfc.blit(pg_sfc, pg_rct)

    #爆弾を表示
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    #爆弾の進行方向の初期設定
    bm_mv = [-1, 1]
    vx = bm_mv[random.randint(0,1)]
    vy = bm_mv[random.randint(0,1)]

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:   #ウィンドウの✕を押したとき
                return                  #終了する

        #経過時間を表示
        sec = pg.time.get_ticks()
        fonto = pg.font.Font(None, 80)
        txt = fonto.render(f"{sec/1000:.2f}", True, "BLACK")
        scrn_sfc.blit(txt, (800, 30))

        #こうかとんの移動
        key_lst = pg.key.get_pressed()
        bf_x = pg_rct.centerx
        bf_y = pg_rct.centery
         
        if key_lst[pg.K_UP]:
            pg_rct.centery -= 1
        elif key_lst[pg.K_DOWN]:
            pg_rct.centery += 1
        elif key_lst[pg.K_LEFT]:
            pg_rct.centerx -= 1
        elif key_lst[pg.K_RIGHT]:
            pg_rct.centerx += 1
        #こうかとんが画面外に出ないようにする
        if (pg_rct.left <= scrn_rct.left) or (pg_rct.right >= scrn_rct.right):
            pg_rct.centerx = bf_x
        if (pg_rct.top <= scrn_rct.top) or (pg_rct.bottom >= scrn_rct.bottom):
            pg_rct.centery = bf_y
        scrn_sfc.blit(pg_sfc, pg_rct)

        #爆弾の移動
        bomb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko; vy *= tate
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        #こうかとんとボールが重なった時
        if pg_rct.colliderect(bomb_rct):
            #「ゲームオーバー」の表示
            fonto = pg.font.Font(None, 120)
            txt = fonto.render("Game Over", True, "RED")
            scrn_sfc.blit(txt, (600, 300))

            pg.display.update()
            #2秒の遅延後、終了する
            clock.tick(0.5)
            return

        pg.display.update()
        clock.tick(1000)                #1000ミリ秒(1秒)遅延させる

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

