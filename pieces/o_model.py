from pieces.base_model import BaseModel

class OModel(BaseModel):
    def draw_piece(self):
        rect = self.rotation_coordinates()
        self.main.pg.draw.rect(self.main.surface, (255, 255, 0), rect)

    def rotation_coordinates(self):
        return self.main.pg.Rect(self.start_piece_at(),
                        -2*self.main.tiles_side_size + self.main.grid_y_axis_offset,
                        self.main.tiles_side_size*2,
                        self.main.tiles_side_size*2)