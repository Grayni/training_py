import pygame as pg

size = (600, 800)
pg.display.set_mode(size)
pg.display.set_caption('caption of window')
img = pg.image.load('../pictures/android.png')
pg.display.set_icon(img)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()