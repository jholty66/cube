#!/usr/bin/env python3

import re

def format_alg(alg: str, type: str) -> list[str]:
    '''Converts an algorithm string with moves seperated by spaces in
either WCA, SigN or prefix format and return a list of moves as strings
in prefix format.'''
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
        return new_alg
    elif type == 'SiGN':
        return list(map(lambda move: move.upper(), alg))
    elif type == 'prefix':
        return alg
    else:
        assert False, 'Not a valid format.'

class Shape():
    sides = 5
    def read_alg(self, alg: list[str]) -> list[tuple[str, int]]:
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
                new_alg.append((dir[0:c], int(move[0])))
        return new_alg
