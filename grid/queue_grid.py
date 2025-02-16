import grid.helper_grid as helper_grid

class QGrid:
    def __init__(self, main):
        self.main = main

    def grid(self):
        rect = self.main.pg.Rect(helper_grid.place_grid_at(self.main, 10),
                    self.main.grid_y_axis_offset,
                    150,
                    391)
        self.main.pg.draw.rect(self.main.surface, (200, 200, 200), rect, 1)
