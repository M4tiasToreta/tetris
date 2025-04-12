
class BaseModel:
    def __init__(self, main):
        self.main = main
    
    def start_piece_at(self):
        return (self.main.window_width/2)-((self.main.tiles_horizontal/2)*self.main.tiles_side_size)+4*self.main.tiles_side_size
    
    def draw_piece(self):
        raise NotImplementedError

    def rotation_coordinates(self):
        raise NotImplementedError
