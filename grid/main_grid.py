import pygame as pg
import grid.helper_grid as helper_grid

class MainGrid:

    def __init__(self, main):
        self.main = main

    def grid(self):
        self.draw_background_lines_grid()
        self.draw_grid_white_outline()
        self.draw_open_top_line()
        pg.display.update()

    def draw_background_lines_grid(self):
        for row in range(self.main.tiles_vertical):
            for col in range(self.main.tiles_horizontal):
                rect = pg.Rect(helper_grid.place_grid_at(self.main, col), 
                               row*self.main.tiles_side_size + self.main.grid_y_axis_offset,
                               self.main.tiles_side_size, 
                               self.main.tiles_side_size)
                pg.draw.rect(self.main.surface, (40, 40, 40), rect, 1)

    def draw_grid_white_outline(self):
        rect = pg.Rect(helper_grid.place_grid_at(self.main, 0), 
                               self.main.grid_y_axis_offset,
                               self.main.tiles_horizontal*self.main.tiles_side_size, 
                               self.main.tiles_vertical*self.main.tiles_side_size)
        pg.draw.rect(self.main.surface, (200, 200, 200), rect, 1)

    def draw_open_top_line(self):
        start_pos = (helper_grid.place_grid_at(self.main, 0), self.main.grid_y_axis_offset)
        end_pos = (helper_grid.place_grid_at(self.main, 10), self.main.grid_y_axis_offset)
        pg.draw.line(self.main.surface, (40, 40, 40), start_pos, end_pos)
