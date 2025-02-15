from grid.main_grid import MainGrid
from grid.queue_grid import QGrid
import pygame as pg

class Main:
    window_width = 1000
    window_height = 600

    def __init__(self):
        pg.init()
        self.surface = pg.display.set_mode((self.window_width, self.window_height))
        self.surface.fill((0, 0, 0))
        self.grid = MainGrid(self)
        self.queue_grid = QGrid(self)

    def main(self):
        while self.grid.running:
            self.grid.grid_loop()
        pg.quit()

if __name__ == "__main__":
    mygame = Main()
    mygame.main()