import math
from PIL import Image
from puzzlePiece import PuzzlePiece
from util import *
import os

# This class is an abstract representation of a puzzle.
# A Puzzle is created using a square center crop of the
# image that can fit in the most number of pieces of
# the specified piece size.
#
# imgSource: the relative path to the image file
# size: desired size of a single piece
# name: name of the puzzle should be a string without file
# extensions.
#
# E.g.: p = Puzzle('path-to-image', 20, 'example') will
# create a puzzle named example that's cut to a square
# with each piece being 20 by 20 pixels.
class Puzzle:
    def __init__(self, imgSource, size, name):
        self.src = imgSource
        self.img = Image.open(imgSource)
        self.name = name
        self.pieceSize = size
        self.puzzleVertices = self._coords()
        self.pieces = self._toPieces()

    # Helper function that calculates and returns a tuple
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

    # Helper function that calculates and returns a tuple
    # of the coordinates of the vertices of the puzzle.
    def _toPieces(self):
        pieceBlocks = []
        x1, y1, x2, y2 = self.puzzleVertices
        count = 1
        for i in range(y1, y2, self.pieceSize):
            for j in range(x1, x2, self.pieceSize):
                pieceBlocks.append(\
                    PuzzlePiece((j, i, j + self.pieceSize,\
                                 i + self.pieceSize),\
                                 self.src, self.name, count))
                count += 1

        return tuple(pieceBlocks)

    # Returns an Image object of the puzzle.
    def getFullPuzzle(self):
        return self.img.crop(self.puzzleVertices)

    # Returns an Image object of the original image.
    def getFullImg(self):
        return self.img

    # Returns a tuple of PuzzlePiece objects that represents
    # all the pieces in this puzzle
    def getPieces(self):
        return self.pieces

    # Shows the full puzzle.
    def showFullPuzzle(self):
        self.getFullPuzzle.show()

    # Shows the full original image.
    def showFullImg(self):
        self.img.show()

    # Shows the pieces in the given range. If no range given, shows all.
    def showPieces(self, start=1, end=None, step=1):
        if start < 1:
            msg = 'Starting point is puzzle piece #1.'
            raise NoSuchPieceException(msg)
        if end > len(self.pieces):
            msg = 'The last piece is #' + str(len(self.pieces)) + \
                  ', there\'s no piece #' + str(end) + '.'
            raise NoSuchPieceException(msg)
        if end is None:
            end = len(self.pieces)
        for i in range(start - 1, end, step):
            self.pieces[i].show()

    # Saves the puzzle as a PNG in the given path.
    # path: must be an existing directory, if not given,
    #   default will be the same directory as the image.
    def saveFullPuzzle(self, path=None):
        if path is None:
            path = ''
            index = self.src.rfind('/')
            if index != -1:
                path += self.src[:index+1]
            path += 'full_puzzle_' + self.name + '.png'
        self.getFullPuzzle().save(path)

    # Saves the puzzle pieces as PNGs in the given directory.
    # path: must be an existing directory, if not given,
    #   default will be the same directory as the image.
    def savePieces(self, path=None):
        if path is None:
            path = ''
            index = self.src.rfind('/')
            if index != -1:
                path += self.src[:index+1]
        for piece in self.pieces:
            piece.save(path)

# Some function calls that you can try out:
# p30 = Puzzle('../images/python.png', 30, 'test')
# p30.getFullPuzzle().show()
# print(p30.getFullPuzzle().size)
# print('Is ' + str(len(p30.pieces)) + ' = ' +\
#       str((p30.getFullPuzzle().size[0] / 30) ** 2) + ' true?')
# p30.showPieces(92,200,1)
# p30.savePieces()