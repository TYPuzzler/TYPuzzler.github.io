# TYPuzzler

TYPuzzler is a typing practice application developed by Chris Choi, Margaret Li, Bowen Tian and Eric Yoon. Practice typing while collecting pieces to solve a puzzle. We hope this makes learning to type enjoyable and exciting!

## Product Description
Our product is a web browser app to practice typing. It will allow users to complete typing exercises, and earn pieces of a puzzle as they go. Users will be able to view and download the whole picture when they finish a puzzle. It is publicly accessible at https://typuzzler.github.io/.

See [userManual.md](/userManual.md) for instructions on how to use TYPuzzler. If you would like to contribute to the project, please read the instructions in [developerGuide.md](/developerGuide.md).

## App Goals/Functionalities

* Allow the user to practice typing exercises of text snippets in real time

* Track and report user’s typing accuracy and speed at the end of a typing exercise

* During a typing exercise, only advance if the user enters the right current character

* (Work in progress) Reward the user with a puzzle piece when an exercise is finished

* (Work in progress) Show the completed puzzle when all pieces have been obtained, then allow the user to download the full image

* (Work in progress) Provide multiple puzzles for the user to solve

## Repository Layout
### \~/src/puzzle
Contains the code related to the backend puzzle processing mechanism

### \~/src/utils
Contains the backend for text sample generation

### \~/public
Contains the public webpage files

### \~/images
Contains all the puzzle images

### \~/src
Contains code related to the front end website

### \~/test
Tests related to frontend and JS.
Update with test directories if necessary.

### \~/tests
Tests related to backend Python code.
Update with test directories if necessary.

## Setup

See **How to build** in [developerGuide.md](/developerGuide.md) for information on the setup.

See **How to test** in [developerGuide.md](/developerGuide.md) for information on testing.
