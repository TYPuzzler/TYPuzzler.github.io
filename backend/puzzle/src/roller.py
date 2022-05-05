import random


def roll(nameOfPuzzle):
    meta = open('../../../images/' + nameOfPuzzle + '/metadata.txt', 'r')
    ml = meta.readlines()
    meta.close()
    with open('../../../images/' + nameOfPuzzle + '/obtained.txt', 'r') as obt:
        ols = []
        ols = obt.readlines()
    if len(ols) == int(ml[2]):
        return 'No piece left'

    ol = [int(n) for n in ols]
    n = random.randint(1, int(ml[2]))
    while n in ol:
        n = random.randint(1, int(ml[2]))
    with open('../../../images/' + nameOfPuzzle + '/obtained.txt', 'a') as obt:
        obt.write(str(n)+'\n')
    url = 'https://github.com/TYPuzzler/TYPuzzler.github.io/blob/main/images/'\
        + nameOfPuzzle + '/' + nameOfPuzzle + '_piece_' + str(n)\
        + '.png?raw=true'
    return url
