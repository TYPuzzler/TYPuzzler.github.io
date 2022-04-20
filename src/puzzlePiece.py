from PIL import Image

# This class is an abstract representation of a piece of puzzle
# taken out of a certain puzzle.
class PuzzlePiece:
    def __init__(self, coords, imgSource):
        self.coords = coords
        self.img = imgSource

    def showPiece(self):
        # TODO
        pass