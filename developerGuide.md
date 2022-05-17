# Developer Guidelines

## How to obtain the source code

On your computer’s command prompt, run the following:
```
git clone https://github.com/TYPuzzler/TYPuzzler.github.io.git
```

## Layout of directories
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

## How to build
In root directory of the projcet, run the following in a terminal to start:
```
npm install
npm start
```

To deploy on Github Pages:

```
npm run deploy
```

## How to test
### JavaScript
Run commands in a terminal from project root directory.
1. Add test files to `~/test`
2. Install MochaJS:
```
npm install mocha
```
3. Run the tests:
```
npm test
```
4. For CI testing:
   1. Add test files to ~/test
   2. Commit with tag `ci-js`
### Python
Run commands in a terminal from project root directory.
1. Add test files to `~/tests`
2. Install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Install Python:
```
brew install python
```
4. Install Pillow
```
python -m pip install --upgrade Pillow
```
5. Install Pipenv
```
python -m pip install --upgrade pipenv
```
6. Install Pytest
```
python -m pip install pytest
```
7. Run tests with pytest
```
pipenv run test -v
```
8. For CI testing:
   1. Add test files to ~/tests
   2. Commit with tag `ci-py`
## Project CI Testing
1. Add JavaScript test files to ~/test and add Python test files to ~/tests
2. Commit with tag `ci-build`

## How to add new tests

- For frontend react JS tests:  
Add new js files to `~/test`. (Should change the directory name to testFrontend)

- For backend python tests:  
Add new python files to `~/tests`. (testBackend)

## How to build a release
