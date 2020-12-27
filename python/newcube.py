#!/usr/bin/env python3.9

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
        if self.order % 2 == 1:
            edges: List[List[Sticker]] = []
            for i in range(len(self.adjMat)):
                for j in range(len(self.adjMat[i])):
                    for depth1 in range(1, int((self.order + 1) / 2)):
                        for depth2 in range(1, int((self.order + 1) / 2)):
                            if 1 == (depth1 or depth2):
                                edge = [Sticker(i,depth1), Sticker(self.adjMat[i][j], depth2)]
                                if set(s.pos for s in edge) not in [set(S.pos for S in e) for e in edges]:
                                    edges.append(edge)
            return edges
        else:
            return []

    def spawn_corners(self) -> List[List[Sticker]]:
        corners: List[List[Sticker]] = []
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat[i])):
                for depth1 in range(1 , int(self.order / 2) + 1):
                    for depth2 in range(1 , int(self.order / 2) + 1):
                        for depth3 in range(1 , int(self.order / 2) + 1):
                            if 1 == (depth1 or depth2 or depth3) :
                                corner = [Sticker(i,depth1), Sticker(self.adjMat[i][j - 1], depth2), Sticker(self.adjMat[i][j], depth3)]
                                if set(s.pos for s in corner) not in [set(S.pos for S in c) for c in corners]:
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
        self.pieces = self.centers + self.edges + self.corners
        self.mobile_pieces= self.edges + self.corners

    # def move(self, move: Tuple[str, int]):
    #     depth = move[0]
    #     move = move[1:]
    #     # Face turns.
    #     # Slice moves.
    #     # Rotations.
    #     # Rotations are a combinatino of two face turns and oen slice
    #     # move.
    #     if move = 'X':
    #         pass
    #     elif move = 'Y':
    #         pass
    #     elif move = 'Z':
    #         pass
    #     return pieces

    def scramble(self):
        pass

    def show_centers(self):
        print([center.pos for center in self.centers])

    def show_edges(self):
        print([edge.pos for edge in self.edges])

    def show_corners(self):
        print([corner.pos for corner in self.corners])

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

pzl = Cube(7)
[print([s.pos for s in center]) for center in pzl.centers]
print()
[print([s.pos for s in edge]) for edge in pzl.edges]
print()
[print([s.pos for s in corner]) for corner in pzl.corners]
print()
print(len(pzl.centers), len(pzl.edges), len(pzl.corners))
print()
