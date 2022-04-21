import math
from PIL import Image
from puzzlePiece import PuzzlePiece
from util import *
import os

# This class is an abstract representation of a puzzle.
# A Puzzle is cropped out of the center of the image that
# can fit in the most number of pieces of the specified
# piece size.
#
# imgSource: the relative path to the image file
# size: desired size of a single piece
# name: name of the puzzle should be a string without file
# extensions.
#
# E.g.: p = Puzzle('path-to-image', 20, 'example') will
# create a puzzle named example; if image has size 110 by
# 84 pixels, the puzzle will be 100 by 80 pixels which
# means 5 by 4 pieces.
class Puzzle:
    def __init__(self, imgSource, size, name):
        self.src = imgSource
        self.img = Image.open(imgSource)
        self.name = name
        self.pieceSize = size
        self.puzzleVertices = self._coords()
        self.pieces = self._toPieces()
        self.rarityChart = [None] * len(self.pieces)
        self.rarity = None

    # Helper function that calculates and returns a tuple
    # of the coordinates of the top-left and bottom-right
    # vertices of the puzzle in form of (x1, y1, x2, y2).
    def _coords(self):
        width, height = self.img.size
        cWidth = math.floor(width / self.pieceSize)
        cHeight = math.floor(height / self.pieceSize)
        newWidth = cWidth * self.pieceSize
        newHeight = cHeight * self.pieceSize
        coord1 = math.floor((width - newWidth) / 2)
        coord2 = math.floor((height - newHeight) / 2)
        coord3 = coord1 + newWidth
        coord4 = coord2 + newHeight
        return (coord1, coord2, coord3, coord4)

    # Helper function that calculates and returns a tuple
    # of the coordinates of the vertices of the puzzle.
    def _toPieces(self):
        pieceBlocks = []
        x1, y1, x2, y2 = self.puzzleVertices
        count = 1
        for i in range(y1, y2, self.pieceSize):
            for j in range(x1, x2, self.pieceSize):
                vert = (j, i, j + self.pieceSize, i + self.pieceSize)
                if not self._isTransparentPiece(self.img.crop(vert)):
                    pieceBlocks.append( PuzzlePiece(vert, self.src, self.name, count))
                    count += 1

        return tuple(pieceBlocks)

    def _isTransparentPiece(self, img):
        return False

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

    # Returns None if rarity is not set.
    # Returns a tuple of probabilities of all the rarity
    # classes(N, R, SR, SSR)
    def getRarity(self):
        return self.rarity

    # Sets the rarities of all the pieces, default probs are:
    #   P(N) = 0.55, P(R) = 0,25, P(SR) = 0.15, P(SSR) = 0.05
    # chances: A tuple in the order (P(N), P(R), P(SR), P(SSR))
    def setRarityChart(self, chances=(0.55, 0.25, 0.15, 0.05)):
        size = len(self.pieces)
        if size < 4:
            for i in range(size):
                self.rarityChart[i] = 'R'
        elif size < 20:
            self.rarityChart[0] = 'SSR'
            self.rarityChart[1] = 'SR'
            self.rarityChart[2] = 'R'
            for i in range(3, size):
                self.rarityChart[i] = 'N'
        count = [math.floor(coeff * size) for coeff in chances]
        n_class, r_class, sr_class, ssr_class = count
        if sum(count) < size:
            diff = size - sum(count)
            for i in range(diff):
                # TODO
                pass



# Some function calls that you can try out:
p30 = Puzzle('../../images/Python_(programming_language).png', 30, 'test')
p30.getFullPuzzle().show()
# print(p30.getFullPuzzle().size)
print('Is ' + str(len(p30.pieces)) + ' = ' + str((p30.getFullPuzzle().size[0] / 30) * (p30.getFullPuzzle().size[1] / 30)) + ' true?')
# p30.showPieces(92,200,1)
# p30.savePieces()
p30.saveFullPuzzle()