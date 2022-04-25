# TYPuzzler Development Log --- Bowen Tian

## 04/21/22

#### `puzzleCreator.py`
- Updated cropping mechanism from center square to center max pan.
	- e.g. If an image of 110 by 84 pixels is passed in and puzzle size is 20, old algorithm would create a puzzle of size 80 by 80 pixels, new algorithm would be 100 by 80. Both in the center.
#### `puzzleRoll.py`
- Created for a random roll of a puzzle piece.
#### TODOs
- ~~Get rid of transparent pieces(no solid color at all)~~
- ~~Need getter functions to get coordinates for puzzle pieces~~
- Inventory System
- ~~Set Rarity~~
- Finish `puzzleRoll.py`

## 04/25/22
#### `puzzleCreator.py`
- Set & get rarity implemented. Pieces created first then assigned with rarity.
- Fully transparent pieces now won't be included thanks to `_isTransparentPiece`.
- `savePieces` function updated to accept user argument including starting piece, ending piece and pace just like `showPieces`.
#### `puzzlePiece.py`
- Set & get rarity implemented, getter functions implemented.
#### `main.py`
- Created to isolate small tests (`.gitignore`)
#### `spec_doc.md`
- Created for documenting classes and functions for client(frontend)
#### `util.py`
- New `PuzzleException` added. Exception hierarchy updated: `PuzzleException` is the parent.
#### TODOs
- Fill `spec_doc.md`