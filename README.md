# TYPuzzler

TYPuzzler is a typing practice application developed by Chris Choi, Margaret Li, Bowen Tian and Eric Yoon. Practice typing while collecting pieces to solve a puzzle. We hope this makes learning to type enjoyable and exciting!

## Product Description
Our product is an app to practice typing. It will allow users to complete typing exercises, and earn pieces of a puzzle as they go. Users will be able to view and download the whole picture when they finish a puzzle. It will be a browser app accessible through a public URL.

## App Goals

* Allow user to practice typing exercises of text snippets in real time

* Track and report user’s typing accuracy and speed at the end of a typing exercise

* During a typing exercise, only advance if the user enters the right current character

* Reward the user with a puzzle piece (chosen by user from three hidden pieces) when an exercise is finished

* Show the completed puzzle when all pieces have been obtained, then allow the user to download the full image

* Provide multiple puzzles for the user to solve

## Repository Layout
### \~/src/
Contains the code related to the backend puzzle processing mechanism

### \~src/utils
Contains the backend for text sample generation

### \~/public
Contains the public webpage files

### \~/images
Contains all the puzzle images

### \~/src
Contains code related to the front end website

Make sure all commands to run the frontend are run in the typuzzler directory

## Setup

npm install

To run:

npm start

To deploy on Github Pages:

npm run deploy

## Local Testing

### JavaScript
1. Add test files to ~/test
2. Install MochaJS
    - `npm install mocha`
3. Run the tests
    - `npm test`

## CI testing

### JavaScript
1. Add test files to ~/test
2. Commit with tag `ci-js`
### Python
1. Add test files to ~/tests
2. Commit with tag `ci-py`
### JavaScript & Python
1. Add JavaScript test files to ~/test and add Python test files to ~/tests
2. Commit with tag `ci-build`
