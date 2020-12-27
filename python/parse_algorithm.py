#!/usr/bin/env python3

import re

def format_alg(alg: str, type: str) -> list[str]:
    '''Converts an algorithm string with moves seperated by spaces in
either WCA, SigN or prefix format and return a list of moves as strings
in modified prefix format.

The the difference between the modified format and the normal format is
that moves turn outer layers start with a "1".'''
    alg = alg.replace('(','')
    alg = alg.replace(')','')   
    alg = alg.split(' ')
    if type == 'WCA':
        new_alg = []
        for move in alg:
            if move[0] in '1234567890':
                move = move.replace('w', '')
            elif 'w' in move:
                move = '2' + move.replace('w', '')
            new_alg.append(move)
    elif type == 'SiGN':
        new_alg = list(map(lambda move: move.upper(), alg))
    elif type == 'prefix':
        new_alg = alg
    else:
        assert False, 'Not a valid format.'
    print(new_alg)
    return new_alg

def convert_alg(alg: list[str], type: str) -> list[str]:
    '''Convertes program readable alg to human readable alg.'''
    pass

class Shape():
    sides = 4
    def read_alg(self, alg: list[str]) -> list[str]:
        '''Takes algorithm in suffix format (each move is a string),
returns a list readable by the solver.'''
        new_alg = []
        for i in range(len(alg)):
            if alg[i][0] not in '1234567890':
                alg[i] = '1' + alg[i]
        for move in alg:
            print(move)
        print()
        for move in alg:
            dir = move[1:]
            # Only letters.
            if len(dir) == 1:
                r = [0]
            elif re.fullmatch('[a-zA-z]', dir[-1]):
                r = [0]
            # Prime dir.
            elif dir[-1] == "'":
                # No number.
                if re.fullmatch('[a-zA-z]', dir[-2]):
                    r = range(self.sides - 1)
                # Number.
                elif dir[-2] in '1234567890':
                    r = range(self.sides - int(dir[-2]))
            # Letter + number.
            elif dir[-1] in '1234567890':
                r = range(int(dir[-1]))
            if len(dir) == 1:
                c = 2
            elif dir[1] in '1234567890':
                c = 1
            else:
                c = 2
            for _ in r:
                # new_alg.append((dir[0:c], int(move[0])))
                new_alg.append(move[0] + dir[0:c])
        print(new_alg)
        return new_alg

xx = Shape()
alg = "x R' U R' D2 R U' R' D2 R2"
print(alg)
yy = format_alg(alg, 'WCA')
xx.read_alg(yy)
