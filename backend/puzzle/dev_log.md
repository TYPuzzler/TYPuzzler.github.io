# 04/21/22

- `puzzleCreator.py` Updated cropping mechanism from center square to center max pan
	- e.g. If an image of 110 by 84 pixels is passed in and puzzle size is 20, old algorithm would create a puzzle of size 80 by 80 pixels, new algorithm would be 100 by 80. Both in the center.
- TODO: Get rid of transparent pieces(no solid color at all)
- TODO: Need getter functions to get coordinates for puzzle pieces
- TODO: Inventory System
- ~~TODO: Set Rarity~~

# 04/25/22
- `puzzleCreator.py` Set rarity implemented
- `puzzlePiece.py` Set & get rarity implemented
- `main.py` Created to isolate small tests (`.gitignore`)