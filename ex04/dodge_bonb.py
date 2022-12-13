import pygame as pg
import random
import sys

def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((1600,900))

    #背景の設定
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    bg_rct.center = 800, 450

    #Clockオブジェクトの作成
    clock = pg.time.Clock()

    #各値の初期設定
    pg_x = 900; pg_y = 400          #こうかとんの初期位置
    bm_x = random.randint(0, 1600)  #爆弾のx座標
    bm_y = random.randint(0, 900)   #爆弾のy座標
    bm_mv = [-1, 1]                 #爆弾の進行方向
    vx = bm_mv[random.randint(0,1)]
    vy = bm_mv[random.randint(0,1)]

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:   #ウィンドウの✕を押したとき
                return                  #終了する
        clock.tick(1000)                #1000ミリ秒(1秒)遅延させる

        #経過時間を表示
        sec = pg.time.get_ticks()
        fonto = pg.font.Font(None, 80)
        txt = fonto.render(f"{sec/1000:.2f}", True, "BLACK")
        scrn_sfc.blit(txt, (800, 30))

        #時間経過で爆弾の速度上昇
        if sec % 100 == 0:
            if vx > 0:
                vx += 0.1
            else:
                vx -= 0.1
            if vy > 0:
                vy += 0.1
            else:
                vy -= 0.1

        #こうかとんを表示
        pg_sfc = pg.image.load("fig/9.png")
        pg_sfc = pg.transform.rotozoom(pg_sfc, 0, 2.0)
        pg_rct = pg_sfc.get_rect()
        pg_rct.center = pg_x, pg_y
        scrn_sfc.blit(pg_sfc, pg_rct)

        #爆弾を表示
        draw_sfc = pg.Surface((20, 20))
        draw_sfc.set_colorkey((0,0,0))
        pg.draw.circle(draw_sfc, (255, 0, 0), (10, 10), 10)
        ball_rct = draw_sfc.get_rect()
        ball_rct.center = bm_x, bm_y
        scrn_sfc.blit(draw_sfc, ball_rct)
        bm_x += vx; bm_y += vy

        #爆弾が画面外に出ないようにする
        if (bm_x-10 <= 0) or (bm_x+10 >= 1600):
            vx *= -1
        if (bm_y-10 <= 0) or (bm_y+10 >= 900):
            vy *= -1

        #こうかとんの移動
        key_lst = pg.key.get_pressed()
        bf_x = pg_x; bf_y = pg_y
        if key_lst[pg.K_UP]:
            pg_y -= 1
        elif key_lst[pg.K_DOWN]:
            pg_y += 1
        elif key_lst[pg.K_LEFT]:
            pg_x -= 1
        elif key_lst[pg.K_RIGHT]:
            pg_x += 1

        #こうかとんが画面外に出ないようにする
        if (pg_x-45 <= 0) or (pg_x+45 >= 1600):
            pg_x = bf_x
        if (pg_y-65 <= 0) or (pg_y+65 >= 900):
            pg_y = bf_y
        
        #こうかとんとボールが重なった時
        if pg_rct.colliderect(ball_rct):
            #「ゲームオーバー」の表示
            fonto = pg.font.Font(None, 120)
            txt = fonto.render("Game Over", True, "RED")
            scrn_sfc.blit(txt, (600, 300))

            pg.display.update()
            #2秒の遅延後、終了する
            clock.tick(0.5)
            return

        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

