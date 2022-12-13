import pygame as pg
import random
import sys

def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    bg_rct.center = 800, 450

    clock = pg.time.Clock()

    pg_x = 900; pg_y = 400
    bm_x = random.randint(0, 1600)
    bm_y = random.randint(0, 900)
    

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        clock.tick(1000)
        pg_sfc = pg.image.load("fig/9.png")
        pg_sfc = pg.transform.rotozoom(pg_sfc, 0, 2.0)
        pg_rct = pg_sfc.get_rect()
        pg_rct.center = pg_x, pg_y
        scrn_sfc.blit(pg_sfc, pg_rct)

        vx = 1; vy =1
        draw_sfc = pg.Surface((20, 20))
        draw_sfc.set_colorkey((0,0,0))
        pg.draw.circle(draw_sfc, (255, 0, 0), (10, 10), 10)
        scrn_sfc.blit(draw_sfc, (bm_x, bm_y))

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            pg_y -= 1
        elif key_lst[pg.K_DOWN]:
            pg_y += 1
        elif key_lst[pg.K_LEFT]:
            pg_x -= 1
        elif key_lst[pg.K_RIGHT]:
            pg_x += 1

        pg.display.update()




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

