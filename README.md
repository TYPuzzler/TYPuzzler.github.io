# TYPuzzler

Go to https://typuzzler.github.io/ to play now!

TYPuzzler is a typing game developed by Chris Choi, Margaret Li, Bowen Tian and Eric Yoon. Practice typing while collecting pieces to solve a puzzle. We hope this makes learning to type enjoyable and exciting!

## Product Description
Our product is a web browser app to practice typing. It allows users to complete typing exercises, and earn pieces of a puzzle as they go. Users can view and download the whole picture when they finish a puzzle. It is publicly accessible at https://typuzzler.github.io/.

See the [user manual](https://github.com/TYPuzzler/TYPuzzler.github.io/wiki/User-Manual) for instructions on how to use TYPuzzler. If you would like to contribute to the project, please read the instructions in the [developer guide](https://github.com/TYPuzzler/TYPuzzler.github.io/wiki/Developer-Guide).

## App Goals/Functionalities

* Allow the user to practice typing exercises of text snippets in real time

* Track and report user’s typing accuracy and speed at the end of a typing exercise

* During a typing exercise, only advance if the user enters the right current character. Indicate when the wrong character is entered by turning the current character highlight red

* Reward the user with a puzzle piece when an exercise is finished

* Show the completed puzzle when all pieces have been obtained, then allow the user to download the full image

* Provide three puzzles for the user to solve, of increasing challenge in the length of the typing exercises and the number of puzzle pieces to complete a puzzle

* Allow the user to come back to their progress on the puzzles, and to clear their progress

## Repository Layout
### \~/src/puzzle
Contains the code related to the backend puzzle processing mechanism

### \~/src/utils
Contains the backend for text sample generation

### \~/src
Contains code related to the front end website

### \~/public
Contains the public webpage files

### \~/images
Contains all the puzzle images

### \~/test
Tests related to the application

## Setup

See [**How to build**](https://github.com/TYPuzzler/TYPuzzler.github.io/wiki/Developer-Guide#how-to-build) in the developer guide for information on the setup.

See [**How to test**](https://github.com/TYPuzzler/TYPuzzler.github.io/wiki/Developer-Guide#how-to-test) in the developer guide for information on testing.
