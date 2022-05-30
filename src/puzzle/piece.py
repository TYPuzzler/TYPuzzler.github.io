from PIL import Image
import io
import urllib.request

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
        with urllib.request.urlopen(self.src) as url:
            f = io.BytesIO(url.read())
        Image.open(f).crop(self.coords).show()

    # Saves this puzzle piece as a PNG in the given directory.
    # path: must be an existing directory, if not given,
    #   default will be the same directory as the image.
    def save(self, path=None):
        if path is None:
            path = ''
            index = self.src.rfind('/')
            if index != -1:
                path += self.src[:index+1]
            else:
                path += '/'
        path += self.name + '_piece_' + str(self.num) + '.png'
        with urllib.request.urlopen(self.src) as url:
            f = io.BytesIO(url.read())
        Image.open(f).crop(self.coords).save(path)

    # Private function called when puzzle is created with default
    # or when rarity is reassigned.
    def _setRarity(self, rarity):
        self.rarity = rarity

    # Returns the rarity level of this specific piece(N, R, SR or SSR)
    def getRarity(self):
        return self.rarity

    # Returns the top-left and bottom-right corners' coordinates
    # in the image(not puzzle) as a tuple.
    def getPos(self):
        return self.coords

    # Returns the number of this piece in the puzzle.
    def getNum(self):
        return self.num

    def gray(self):
        with urllib.request.urlopen(self.src) as url:
            f = io.BytesIO(url.read())
        return Image.open(f).crop(self.coords).convert('LA')

    def trans(self):
        with urllib.request.urlopen(self.src) as url:
            f = io.BytesIO(url.read())
        return Image.open(f).crop(self.coords).putalpha(128)
