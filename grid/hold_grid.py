import resources.helper_grid as helper_grid

class HoldGrid:
    def __init__(self, main):
        self.main = main

    def grid(self):
        rect = self.main.pg.Rect(helper_grid.place_grid_at(self.main, -5), 
                    self.main.grid_y_axis_offset,
                    150, 
                    151)
        self.main.pg.draw.rect(self.main.surface, (200, 200, 200), rect, 1)