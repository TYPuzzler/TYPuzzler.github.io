import math
from PIL import Image

class PuzzlePiece:
    def __init__(self, coords, imgSource):
        self.coords = coords
        self.img = img

    def getPiece(self):
        pass

# This class is an abstract representation of a puzzle.
# Given the relative path to the image file and a desired
# size of a single piece, a Puzzle is created using a
# square center crop of the image that can fit in the
# most number of pieces of the specified piece size.
class Puzzle:
    def __init__(self, imgSource, size):
        self.img = Image.open(imgSource)
        self.pieceSize = size
        self.puzzleVertices = self._coords()
        self.pieces = self._toPieces()

    def _coords(self):
        width, height = self.img.size
        shorter = min(width, height)
        longer = max(width, height)
        count = math.floor(shorter / self.pieceSize)
        length = count * self.pieceSize
        coord1 = math.floor((longer - length) / 2)
        coord2 = math.floor((shorter - length) / 2)
        coord3 = coord1 + length
        coord4 = coord2 + length
        if width >= height:
            return (coord1, coord2, coord3, coord4)
        else:
            return (coord2, coord1, coord4, coord3)

    def _toPieces(self):
        

    def getFullPuzzle(self):
        return self.img.crop(self.vertices)

    def getFullImg(self):
        return self.img

    def asPieces(self, numOfPieces):
        pass

# p30 = Puzzle('../images/python.png', 30)
# p10 = Puzzle('../images/python.png', 10)
# p300 = Puzzle('../images/python.png', 300)
# p30.getFullPuzzle().show()
# p10.getFullPuzzle().show()
# p300.getFullPuzzle().show()
