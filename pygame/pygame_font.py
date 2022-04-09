import pygame as pg

pg.init()
size = (600, 800)
screen = pg.display.set_mode(size)
pg.display.set_caption('caption of window')
img = pg.image.load('../pictures/android.png')
pg.display.set_icon(img)

font = pg.font.SysFont('ebrima', 36)

follow = font.render('Hello pygame', True, '#999999')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.blit(follow, (5, 5))
    pg.display.update()
