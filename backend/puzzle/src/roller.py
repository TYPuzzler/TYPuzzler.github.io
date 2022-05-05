import random

def roll(name):
    obt = open('../../../images/'+name+'/obtained.txt', 'ra')
    meta = open('../../../images/'+name+'/metadata.txt', 'r')

    ml = meta.readlines()
    ol = obt.readlines()
