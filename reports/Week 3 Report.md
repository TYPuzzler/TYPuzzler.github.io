# Team Report
## 1. Last Week's Plans / Goals
- Finish setting up Git repo  
- Start investigating our technology stack  
- Create small prototypes and foundational code for the web app  
## 2. What We Did  
- Finalized Git repo set upCancel changes
- Implemented puzzle generating mechanics
- Random text generation
- Basic frontend pages
## 3. Meeting Agenda
- Start investigating options for our technology stack, try out ideas for small prototypes and foundational code
# Contributions  
## 1. Last Week's Plans / Goals
### Margaret  
- Start setting up a basic web application frontend  
### Chris  
- Start setting up the random text sample generation  
### Bowen  
- Setting up GitHub Repo and start working/experimenting on different ways of cutting images into pieces  
### Eric  
- Started on basic react app frontend
- Frontend is set up to start on next week typing UI
## 2. What We Did  
### Margaret
- Researched technologies and tools for making the frontend and UI of the app.
- Found React tools that can hopefully work nicely for creating the client interface and capturing input, but will need to narrow it down for what will work best with the backend's functions.
### Eric  
- Started on basic react app frontend
- Debugged node js build failures
- Frontend is set up to start on next week typing UI
### Bowen
- Set up GitHub Repo with teammates.
- Implemented puzzle generating mechanism(`puzzleCreator.py`, `puzzlePiece.py`, `util.py`).
- Planned to use NumPy for seam carving but turned out Pillow is more than enough for the current stage and is much easier to implement.
- Storage method of puzzles and pieces was a hard choice to make: either store each puzzle and piece as an individual image object which is faster to retrieve but takes up more memory, or use coordinates as a reference and do the calculation/cutting on the fly which saves space but runs slightly slower. Went with the second method because the puzzles won't be accessed that often so space efficiency is favored.
### Chris
- Tested a few APIs for text generation.
- Implemented a simple random text generator using one of the tested APIs (`words.js`).
## 3. Plans / Goals  
### Margaret
- Research more about APIs and frameworks for capturing user input and information, connecting to backend systems.
- Implement more ideas for trying to create a basic frontend.
### Bowen
- Find a way to assign different chances to each of the puzzle pieces for the rewarding system
- Maybe find a way to make the puzzle pieces more like actual puzzle pieces instead of squares
### Chris
- Research more APIs for text sample generation since the one currently in use often provides samples with punctuation errors.
- Add parameters to the random text generator to allow for different types of typing samples.
- Start implementing accuracy checking functionality
### Eric  
- Work on refining the navigation UI
- Start on typing UI