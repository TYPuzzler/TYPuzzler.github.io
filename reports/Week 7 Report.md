# Team Report
## 1. Last Week's Plans / Goals
- Continue implementing goals of our project, especially the puzzle reward use case
- Provide comprehensive documentation
## 2. What We Did 
## 3. Plans / Goals
## 4. Meeting Agenda
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
### Bowen
### Chris
- Made the puzzle progress position adapt to screen size
    - It seems that there is a cutoff to horizontal screen size where the puzzle progress position is no longer centered. This should not be a problem since the intended user is one who has a standard computer screen.
- I did research on the Web Storage API and have a general plan for tracking the user's progress
    - I plan on using it as a map from puzzle name to a list of pieces that they've acquired for that puzzle, updating it whenever they earn a new one.
    - I can use JSON strings to store the list as a string and convert it back when I need to access the contents.
### Eric
## 3. Plans / Goals  
### Margaret
### Bowen
### Chris
- Implement the user progress storage using the Web Storage API with the user earning pieces in a specific order.
- Start working on randomizing the order of puzzle pieces earned
### Eric