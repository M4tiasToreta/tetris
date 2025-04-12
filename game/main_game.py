from pieces.o_model import OModel

class MainGame:
    def __init__(self, main):
        self.main = main
        self.o = OModel(self.main)

    def play(self):
        self.o.draw_piece()