import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像Surfaceを作成する
    bg_img_r = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    w_k = 0
    h_k = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            h_k = -1
        elif key_lst[pg.K_DOWN]:
            h_k = 1
        if key_lst[pg.K_LEFT]:
            w_k = -1
        if key_lst[pg.K_RIGHT]:
            w_k = 2
        kk_rct.move_ip(w_k,h_k)
        w_k = 0
        h_k = 0
    
        screen.blit(bg_img, [-x, 0]) #screen Surfaceに背景画像Surfaceを貼り付ける
        screen.blit(bg_img_r, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(bg_img_r, [-x+4800, 0])
        screen.blit(kk_img, [-x+kk_rct[0], kk_rct[1]])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()