import pygame as pg

class MainGrid:

    title = "Grid"
    tiles_horizontal = 10
    tiles_vertical = 20
    tiles_size = 20
    tiles_side_size = 30

    def __init__(self, main):
        self.clock = pg.time.Clock()
        self.running = True
        self.main = main

    def grid_loop(self):
        for row in range(self.tiles_vertical):
            for col in range(self.tiles_horizontal):
                rect = pg.Rect(self._place_grid_at_middle(col), 
                               row*self.tiles_side_size,
                               self.tiles_side_size, 
                               self.tiles_side_size)
                pg.draw.rect(self.main.surface, (40, 40, 40), rect, 1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
        pg.display.update()

    def _place_grid_at_middle(self, col):
        return (self.main.window_width/2)-((self.tiles_horizontal/2)*self.tiles_side_size)+col*self.tiles_side_size