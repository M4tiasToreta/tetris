import pygame as pg

TITLE = "Grid"
TILES_HORIZONTAL = 10
TILES_VERTICAL = 20
TILE_SIZE = 20

class QGrid:
    def __init__(self, main):
        self.clock = pg.time.Clock()
        self.loop = True
        self.main = main

    def grid_loop(self):
        for row in range(TILES_VERTICAL):
            for col in range(TILES_HORIZONTAL):
                rect = pg.Rect(col*40, row*40, 40, 40)
                pg.draw.rect(self.surface, (40, 40, 40), rect, 1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
        pg.display.update()
