# Team Report
## 1. Last Week's Plans / Goals
- Continue implementing goals of our project, especially the puzzle reward use case
- Provide comprehensive documentation
## 2. What We Did 
- Added user and developer documentation to the repository
## 3. Plans / Goals
- Keep working on implementing the puzzle reward use case and puzzle progress use case, investigating different options
## 4. Meeting Agenda
- Discuss how to work on implementing the main features that haven't been completed (puzzle rewards, puzzle progress, multiple puzzles available)
# Contributions  
## 1. Last Week's Plans / Goals
### Margaret
- Investigate and try options for communicating data between Python and React.
- Add more UI elements and interfaces for the user to interact with, and functionalities in the typing interface.
### Bowen
- Set up database/python server for front/back end data transfer.
### Chris
- Make the puzzle progress position adapt to screen size
- Do more research on the Web Storage API
### Eric
- Help frontend team with Python to React connection
## 2. What We Did  
### Margaret
- Did research on Heroku and began trying it out as an option for establishing data storage and communication between frontend and backend
### Bowen
- Automatically generating data files for front end for piece selection.
- Database server is working on local network.
### Chris
- Made the puzzle progress position adapt to screen size
    - It seems that there is a cutoff to horizontal screen size where the puzzle progress position is no longer centered. This should not be a problem since the intended user is one who has a standard computer screen.
- I did research on the Web Storage API and have a general plan for tracking the user's progress
    - I plan on using it as a map from puzzle name to a list of pieces that they've acquired for that puzzle, updating it whenever they earn a new one.
    - I can use JSON strings to store the list as a string and convert it back when I need to access the contents.
### Eric
## 3. Plans / Goals  
### Margaret
- Keep investigating and setting up Heroku as a way to help with implementing the puzzle rewards and puzzle progress
- Add more functionalities to the user interface and feedback to the user in the typing interface
### Bowen
- Make database more accessable(if we still want to use one)
- Look into python integration
### Chris
- Implement the user progress storage using the Web Storage API with the user earning pieces in a specific order.
- Start working on randomizing the order of puzzle pieces earned
### Eric
