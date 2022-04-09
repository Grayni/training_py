import pygame as pg

pg.init()
size = (200, 670)
screen = pg.display.set_mode(size)
font = pg.font.SysFont('Arial', 36)
follow = font.render(' Continue ', True, '#000000', '#121212')
width, height = follow.get_size()

x, y = 5, 105
FPS = 120
vector_x = 1
vector_y = 1

clock = pg.time.Clock()
while True:
    if y + height >= size[1] or y == 0:
        vector_y = -vector_y

    if x + width >= size[0] or x == 0:
        vector_x = -vector_x

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill('#000000')
    screen.blit(follow, (x, y))
    x += vector_x
    y += vector_y
    pg.display.update()



