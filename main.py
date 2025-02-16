from grid.main_grid import MainGrid
from grid.queue_grid import QGrid
from grid.hold_grid import HoldGrid
import pygame as pg

class Main:
    tiles_horizontal = 10
    tiles_vertical = 20
    window_width = 1500
    window_height = 900
    tiles_side_size = 30
    tiles_size = 20
    grid_y_axis_offset = 100
    pg=pg

    def __init__(self):
        self.pg.init()
        self.surface = self.pg.display.set_mode((self.window_width, self.window_height))
        self.surface.fill((0, 0, 0))
        self.grid = MainGrid(self)
        self.queue_grid = QGrid(self)
        self.hold_grid = HoldGrid(self)
        self.running = True

    def main(self):
        while self.running:
            self.grid.grid()
            self.queue_grid.grid()
            self.hold_grid.grid()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        pg.quit()

if __name__ == "__main__":
    mygame = Main()
    mygame.main()
