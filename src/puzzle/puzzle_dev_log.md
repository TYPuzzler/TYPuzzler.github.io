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
- ~~Inventory System~~ *Passed*
- ~~Set Rarity~~
- ~~Finish `puzzleRoll.py`~~ *Passed*

## 04/25/22
#### `puzzleCreator.py`
- Set & get rarity implemented. Pieces created first then assigned with rarity.
- Fully transparent pieces now won't be included thanks to `_isTransparentPiece`.
- `savePieces` function updated to accept user argument including starting piece, ending piece and pace just like `showPieces`.
- Rarity assignment updated. Instead of assigning in order(e.g. N,N,N,N,N,R,R,R,SR,SR,SSR), now is assigning randomly(e.g. SR,N,R,N,N,SSR,R,SR,R,N,N,R)
#### `puzzlePiece.py`
- Set & get rarity implemented, getter functions implemented.
#### `main.py`
- Created to isolate small tests (`.gitignore`)
#### `spec_doc.md`
- Created for documenting classes and functions for client(frontend)
#### `util.py`
- New `PuzzleException` added. Exception hierarchy updated: `PuzzleException` is the parent.
#### `puzzleInventory.py`
- Created.
#### TODOs
- ~~Fill `spec_doc.md`~~ *Passed*
- ~~**Inherited**: Inventory System~~ *No longer need*
- ~~**Inherited**: Finish `puzzleRoll.py`~~ *Passed*

## 04/26/22
#### TODOs
- ~~**Inherited**: Fill `spec_doc.md`~~ *Passed*
- ~~Filter on new piece.~~ *Passed*

## 05/03/22
#### Test & CI
- Initial set up for PyTest.
- Github Actions set up for pytest.
#### TODOs
- ~~**Inherited**: Finish `puzzleRoll.py`~~
- ~~**Inherited**: Fill `spec_doc.md`~~*Passed*
- ~~**Inherited**: Filter on new piece.~~*Passed*
- ~~Write a simple test.~~

## 05/04/22
#### `puzzle.py`
- `imageSource` now is URL to image instead of relative path.
#### `roller.py`
- Implemented roller. Given a puzzle name returns URL of a piece of new puzzle.
- Test added
#### Styel
- File name changed to adhere to PEP8
#### TODOs
- **Inherited**: Fill `spec_doc.md`
- **Inherited**: Filter on new piece.

## 05/09/22
#### `roller.py` --> `interface.py`
- Renamed to `interface.py`.
- `demo_roll` implemented for beta release.
- URL packaged to JSON
