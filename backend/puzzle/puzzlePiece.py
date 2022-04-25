from PIL import Image

# This class is an abstract representation of a piece of puzzle
# taken out of a certain puzzle.
#
# coords: coordinates of the top-left and bottom-right corner.
# imgSource: the relative path to the original image of which
#   the puzzle piece is taken out.
# name: the name of the puzzle, not the piece. Pieces don't
#   have names.
class PuzzlePiece:
    def __init__(self, coords, imgSource, name, num):
        self.coords = coords
        self.src = imgSource
        self.name = name
        self.num = num
        self.rarity = None

    # Shows this piece in a new window
    def show(self):
        Image.open(self.src).crop(self.coords).show()

    # Saves this puzzle piece as a PNG in the given directory.
    # path: must be an existing directory, if not given,
    #   default will be the same directory as the image.
    def save(self, path=None):
        if path is None:
            path = ''
            index = self.src.rfind('/')
            if index != -1:
                path += self.src[:index+1]
        path += 'puzzle_' + self.name + '_piece_' + str(self.num) + '.png'
        Image.open(self.src).crop(self.coords).save(path)

    def _setRarity(self, rarity):
        self.rarity = rarity

    def getRarity(self):
        return self.rarity