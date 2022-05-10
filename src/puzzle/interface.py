import random
import urllib.request
import json


# Given the name of a puzzle, returns the URL to a undiscovered piece of that puzzle
# or a message that says "No piece left". Uses a text log to keep track of which
# pieces are obtained.
def roll(nameOfPuzzle, TEST=False):
    meta = open('images/' + nameOfPuzzle + '/metadata.txt', 'r')
    ml = meta.readlines()
    meta.close()
    with open('images/' + nameOfPuzzle + '/obtained.txt', 'r') as obt:
        ols = []
        ols = obt.readlines()
    if len(ols) == int(ml[2]):
        return 'No piece left'

    ol = [int(n) for n in ols]
    n = random.randint(1, int(ml[2]))
    while n in ol:
        n = random.randint(1, int(ml[2]))
    with open('images/' + nameOfPuzzle + '/obtained.txt', 'a') as obt:
        obt.write(str(n)+'\n')
    url = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/'\
        + nameOfPuzzle + '/' + nameOfPuzzle + '_piece_' + str(n)\
        + '.png?raw=true'
    return url

def demo_roll(nameOfPuzzle):
    metaURL = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/' + nameOfPuzzle + '/metadata.txt?raw=true'
    meta = urllib.request.urlopen(metaURL)
    
    ml = meta.readlines()

    n = random.randint(1, int(ml[2]))
    
    url = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/'\
        + nameOfPuzzle + '/' + nameOfPuzzle + '_piece_' + str(n)\
        + '.png?raw=true'
    with open('url.json', 'w', encoding='utf-8') as f:
        json.dump(url, f, ensure_ascii=False, indent=4)

    return json.dumps(url)

demo_roll('JS_logo')
