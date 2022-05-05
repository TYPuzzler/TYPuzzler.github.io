import math
from PIL import Image
from piece import *
from util import *
import os
import io
import random
import urllib.request

# This class is an abstract representation of a puzzle.
# A Puzzle is cropped out of the center of the image that
# can fit in the most number of pieces of the specified
# piece size.
#
# imgSource: the URL to the image file
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
        with urllib.request.urlopen(self.src) as url:
            f = io.BytesIO(url.read())
        self.img = Image.open(f)
        self.name = name
        self.pieceSize = size
        self.puzzleVertices = self._coords()
        self.pieces = self._toPieces()
        self.rarity = (0.55, 0.25, 0.15, 0.05)
        self.rarityList = [None] * len(self.pieces)
        self.rarityPool = {'N': [], 'R': [], 'SR': [], 'SSR': []}
        self.setRarity(self.rarity)

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
                    pieceBlocks.append(PuzzlePiece(vert, self.src,
                                                   self.name, count))
                    count += 1

        return tuple(pieceBlocks)

    def _isTransparentPiece(self, img):
        return img.convert('RGBA').getextrema()[-1] == (0, 0)

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
        if end is None:
            end = len(self.pieces)

        if start < 1:
            msg = 'Starting point is puzzle piece #1.'
            raise NoSuchPieceException(msg)
        if end > len(self.pieces):
            msg = 'The last piece is #' + str(len(self.pieces)) + \
                  ', there\'s no piece #' + str(end) + '.'
            raise NoSuchPieceException(msg)

        for i in range(start - 1, end, step):
            self.pieces[i].show()

    # Saves the puzzle pieces as PNGs in the given directory.
    # path: must be an existing directory, if not given,
    #   default will be the same directory as the image.
    def savePieces(self, path=None, start=1, end=None, step=1):
        if end is None:
            end = len(self.pieces)
        if start < 1:
            msg = 'Starting point is puzzle piece #1.'
            raise NoSuchPieceException(msg)
        if end > len(self.pieces):
            msg = 'The last piece is #' + str(len(self.pieces)) + \
                  ', there\'s no piece #' + str(end) + '.'
            raise NoSuchPieceException(msg)

        for i in range(start - 1, end, step):
            self.pieces[i].save(path)

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

    # Returns (0.55, 0.25, 0.15, 0.05) if rarity is not set.
    # Returns a tuple of probabilities of all the rarity
    # levels(N, R, SR, SSR)
    def getRarity(self):
        return self.rarity

    # Funtion that sets the rarities of all the pieces,
    # default probs are:
    #   P(N) = 0.55, P(R) = 0,25, P(SR) = 0.15, P(SSR) = 0.05
    # chances: A tuple in the order (P(N), P(R), P(SR), P(SSR))
    def setRarity(self, rarity):
        if min(rarity) < 0 or max(rarity) > 1 or sum(rarity) != 1:
            msg = 'Invalid combination of probabilities: ' + str(rarity)
            raise PuzzleException(msg)

        size = len(self.pieces)
        if size < 4:
            self.rarity = (0, 1, 0, 0)
            for i in range(size):
                self.rarityList[i] = 'R'
        elif size < 20:
            self.rarity = (1 - 3/size, 1/size, 1/size, 1/size)
            self.rarityList[0] = 'SSR'
            self.rarityList[1] = 'SR'
            self.rarityList[2] = 'R'
            for i in range(3, size):
                self.rarityList[i] = 'N'
        else:
            self.rarity = rarity
            count = [math.floor(coeff * size) for coeff in rarity]
            n_class, r_class, sr_class, ssr_class = count
            if sum(count) < size:
                diff = size - sum(count)
                for i in range(diff):
                    self.rarityList[size - 1 - i] = 'R'
            counter = 0
            while counter < sum(count):
                i = random.randint(0, sum(count) - 1)
                if counter < n_class:
                    if self.rarityList[i] is None:
                        self.rarityList[i] = 'N'
                        counter += 1
                elif counter < n_class+r_class:
                    if self.rarityList[i] is None:
                        self.rarityList[i] = 'R'
                        counter += 1
                elif counter < sum(count) - ssr_class:
                    if self.rarityList[i] is None:
                        self.rarityList[i] = 'SR'
                        counter += 1
                else:
                    if self.rarityList[i] is None:
                        self.rarityList[i] = 'SSR'
                        counter += 1
        self._updatePiecesAndPool()

    # Private function that updates the rarity of the pieces
    def _updatePiecesAndPool(self):
        for i in range(len(self.pieces)):
            r = self.rarityList[i]
            self.pieces[i]._setRarity(r)
            self.rarityPool[r].append(i)

    # Returns the rarity level of a certain piece.
    def getRarityOf(self, num):
        if num < 1 or num > len(self.pieces):
            msg = 'The last piece is #' + str(len(self.pieces)) + \
                  ', there\'s no piece #' + str(end) + '.'
            raise NoSuchPieceException(msg)

        return self.pieces[num - 1].getRarity()
