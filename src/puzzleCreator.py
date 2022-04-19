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
# E.g.: p = Puzzle('path-to-image', 20) will create a
# puzzle that's cut to a square with each piece being 20
# by 20 pixels.
class Puzzle:
    def __init__(self, imgSource, size):
        self.img = Image.open(imgSource)
        self.pieceSize = size
        self.puzzleVertices = self._coords()
        self.pieces = self._toPieces()

    # Private function that calculates and returns a tuple
    # of the coordinates of the top-left and bottom-right
    # vertices of the puzzle in form of (x1, y1, x2, y2).
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

    # Private function that calculates and returns a tuple
    # of the coordinates of the vertices of the puzzle.
    def _toPieces(self):
        pieceBlocks = []
        x1, y1, x2, y2 = self.puzzleVertices
        
        for i in range(y1, y2, self.pieceSize):
            for j in range(x1, x2, self.pieceSize):
                pieceBlocks.append((j, i, j + self.pieceSize, i + self.pieceSize))

        return tuple(pieceBlocks)

    def getFullPuzzle(self):
        return self.img.crop(self.puzzleVertices)

    def getFullImg(self):
        return self.img

    def getPieces(self):
        pass

    def showFullPuzzle(self):
        self.getFullPuzzle.show()

    def showFullImg(self):
        self.img.show()

    def showPieces(self):
        pass
# Some function calls that you can try out:
# p30 = Puzzle('../images/python.png', 30)
# p30.getFullPuzzle().show()
# print(p30.getFullPuzzle().size)
# print('Is ' + str(len(p30.pieces)) + ' = ' + str((p30.getFullPuzzle().size[0] / 30) ** 2) + ' true?')