#!/usr/bin/env python3.9

import random
from typing import *

class Sticker:
    def __init__(self, pos: int, depth: int):
        self.colour = pos # self.colour is immutable
        self.pos = pos
        self.depth = depth

class Solid:
    def spawn_centers(self) -> List[List[Sticker]]:
        return [[Sticker(i, 1)] for i in range(len(self.adjMat))] if self.order % 2 == 1 else []

    def spawn_edges(self) -> List[List[Sticker]]:
        edges: List[List[Sticker]] = []
        r = range(1, int((self.order + 1) / 2))
        if self.order % 2 == 1:
            for i in range(len(self.adjMat)):
                for j in range(len(self.adjMat[i])):
                    for depth1 in r:
                        for depth2 in r:
                            if 1 in (depth1, depth2):
                                edge = [Sticker(i, depth1), Sticker(self.adjMat[i][j], depth2)]
                                if [set(s.pos for s in edge), [s.depth for s in edge]] not in [[set(S.pos for S in e), [S.depth for S in e]] for e in edges]:
                                    edges.append(edge)
        return edges

    def spawn_corners(self) -> List[List[Sticker]]:
        corners: List[List[Sticker]] = []
        r = range(1 , int(self.order / 2) + 1)
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat[i])):
                for depth1 in r:
                    for depth2 in r:
                        for depth3 in r:
                            if 1 in (depth1, depth2, depth3):
                                corner = [Sticker(i, depth1), Sticker(self.adjMat[i][j - 1], depth2), Sticker(self.adjMat[i][j], depth3)]
                                if [set(s.pos for s in corner), [s.depth for s in corner]] not in [[set(S.pos for S in c), [S.depth for S in c]] for c in corners]:
                                    corners.append(corner)
        return corners

    def __init__(self, order: int, sides: int, faces: int, adjMat: List[List[int]]):
        self.order = order
        self.faces = faces
        self.sides = sides
        self.adjMat = adjMat
        self.centers = self.spawn_centers()
        self.edges = self.spawn_edges()
        self.corners = self.spawn_corners()
        # Lists are mutable in python, modifiying the eges list also odifies the pieces list.
        self.pieces = self.edges + self.corners

    def exec_move(self, move: Tuple[int, str, int]):
        global self.centers, self.edegs, self.corners
        # move: (count, move, depth)
        count, move, depth = move
        for _ in range(count):
            # Fuce turn.
            if move == 'F':
                for piece in self.pieces:
                    if:
            elif move == 'B':
                pass
            elif move == 'U':
                pass
            elif move == 'D':
                pass
            elif move == 'L':
                pass
            elif move == 'R':
                pass
            # Slice.
            elif move == 'M':
                pass
            elif move == 'E':
                pass
            elif move == 'S':
                pass
            # Error.
            else:
                raise AssertionError(move + 'is not a valid move.')

    def exec_alg(self, alg: List[str])):
        for move in alg:
            exec_move(move)

    def scramble(self):
        moves = 'RBUDLR'
        r = range(shape.sides - 1)
        for _ in range(len(shape.pieces)):
            exec_move((random.choice(r), random.choice(moves), random.choice(r)))

    def show_centers(self):
        for center in self.centers:
            print([s.colour for s in center], [s.pos for s in center], [s.depth for s in center])

    def show_edges(self):
        for edge in self.edges:
            print([s.colour for s in edge], [s.pos for s in edge], [s.depth for s in edge])

    def show_corners(self):
        for corner in self.corners:
            print([s.colour for s in corner], [s.pos for s in corner], [s.depth for s in corner])

    def show_all(self):
        self.show_centers()
        print()
        self.show_edges()
        print()
        self.show_corners()
        print()
        print(len(self.centers), len(self.edges), len(self.corners))
        print(len(self.centers) + len(self.edges) + len(self.corners))

class Tetrahedron(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
            sides = 3,
            faces = 4,
            adjMat = [[1,2,3], # 0
                      [0,3,2], # 1
                      [0,1,3], # 2
                      [0,2,1]] # 3
        )

class Cube(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
            sides = 4,
            faces = 6,
            adjMat = [[1,2,3,4], # 0
                      [2,0,4,5], # 1
                      [3,0,1,5], # 2
                      [4,0,2,5], # 3
                      [1,0,3,5], # 4
                      [1,4,3,2]] # 5
        )

    scheme = {
       0: 'FFFFFF',
       1: '008000',
       2: 'FF0000',
       3: '0000FF',
       4: 'FFA500',
       5: 'FFFF00:'
    }

    def show_cube(self):
        '''
    uuu
    uuu
    uuu

lll fff rrr bbb
lll fff rrr bbb
lll fff rrr bbb

    ddd
    ddd
    ddd
        '''
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')
        print('    ','    ')

class Octahedron(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
            sides = 3,
            faces = 8,
            adjMat = [[1,2,3], # 0
                      [0,4,6], # 1
                      [0,6,5], # 2
                      [0,5,4], # 3
                      [3,7,1], # 4
                      [3,2,7], # 5
                      [2,1,7], # 6
                      [4,5,6]] # 7
        )

class Dodecahedron(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
            sides = 5,
            faces = 12,
            adjMat = [[1,2,3,4,5],   # 0
                      [0,5,6,7,2],   # 1
                      [0,1,7,8,3],   # 2
                      [0,2,8,9,4],   # 3
                      [0,3,9,10,5],  # 4
                      [0,4,10,6,1],  # 5
                      [1,5,10,11,7], # 6
                      [1,6,11,8,2],  # 7
                      [2,7,11,9,3],  # 8
                      [3,8,11,10,4], # 9
                      [4,9,11,6,5],  # 10
                      [10,9,8,7,6]]  # 11
        )

class Icosahedron(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
            sides = 3,
            faces = 20,
            adjMat = [[1,3,18],   # 0
                      [5,0,17],   # 1
                      [3,6,19],   # 2
                      [0,4,2],    # 3
                      [5,7,3],    # 4
                      [8,4,1],    # 5
                      [7,10,2],   # 6
                      [4,9,6],    # 7
                      [5,12,9],   # 8
                      [8,11,7],   # 9
                      [11,15,6],  # 10
                      [13,10,9],  # 11
                      [8,17,13],  # 12
                      [12,14,11], # 13
                      [13,16,15], # 14
                      [14,19,10], # 15
                      [17,18,14], # 16
                      [16,12,1],  # 17
                      [19,16,0],  # 18
                      [15,18,2]]  # 19
        )

print(Tetrahedron(4).show_all())
