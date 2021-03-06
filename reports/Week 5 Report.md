# Team Report
## 1. Last Week's Plans / Goals
- Investigate adding tests to our project
## 2. What We Did  
- Integrated GitHub Actions as our CI service
- Wrote some simple tests
## 3. Plans / Goals
- Create beta version of our project
## 4. Meeting Agenda
- Discuss which major components of our product need to be ready for the beta release and how to demonstrate them.
# Contributions  
## 1. Last Week's Plans / Goals
### Margaret
- Catch up on last week's goals.
- Implement frontend elements to try to connect to the backend elements.
### Bowen
- Filter on new pieces.
- Start on the document for puzzle.
- Save gallary data.
### Chris
- Complete a working version of text generation and accuracy checking functionality.
- Discuss with team to determine whether or not the text generator should be parameterized to allow for different text lengths.
### Eric  
- Health permitting, work on catching up from last week's goals
- Ideally have UI that is ready to interact with the puzzle backend

## 2. What We Did  
### Margaret
- Investigated frontend design choices and ways to implement elements to interact with processing and backend functions.
### Eric  
- Added basic css for page formatting and color
### Bowen
- Implemented puzzle generation from URL.
- Configured GitHub Actions for automatic execution of Python tests using Pytest.
- Created a simple test.
- Started implementing filters for puzzle pieces.
### Chris
- I got the text generator to work with strings and am able to print them to console from the frontend.
    - The way that I was previously implementing it was based on an implementation I did using React classes, which does not work on this project since we are using hooks instead.
    - Currently working on displaying the text sample on the page. Since we can't do top-level awaits for async functions, I'm experimenting with the React useEffect hook for this.
- Configured GitHub Actions for automatic execution of JavaScript tests using MochaJS.

## 3. Plans / Goals  
### Margaret
- Have major components of the frontend (typing interface, puzzle interface) ready for beta release. 
### Bowen
- Finish filtering.
- Simplify puzzle generation proces and get rid of unnecessary funtions.
- Figure out a way to store user progress,
### Chris
- Finish displaying the generated text on the typing page.
- Finish the accuracy functionality of input
### Eric  
- Display hardcoded puzzle in time for the beta release
