#!/usr/bin/env python3.9

'''
TODO:
Test the turn function to see that it works on all puzzles.

Function to check weather a face is solved.  Do this by looking at
(for example) all stickers with value 0 and check that they all share
the same colour.  Then extend this to check all faces to know weather
the puzzle is solved.

Function to scramble cube.  Later make scrambles WCA legal.

(Maybe) function to display cube as plaintext. Faster to check
functions that change state of cube.

Search for 3D graphics librarty to display shapes.

RESEARCH:
Look at the rubiks cube solver that is written in CPP.
 '''

import random
import re
from typing import *

class Sticker:
    def __init__(self, pos: int, depth: int):
        self.colour = pos # self.colour is immutable
        self.pos = pos
        self.depth = depth

class Piece:
    def __init__(self, *stickers: Sticker):
        self.stickers = list(stickers)

    def colour(self) -> List[int]:
        return [sticker.colour for sticker in self.stickers]

    def pos(self) -> List[int]:
        return [sticker.pos for sticker in self.stickers]

    def depth(self) -> List[int]:
        return [sticker.depth for sticker in self.stickers]

    def show(self):
        print(self.colour(), self.pos(), self.depth())

class Center(Piece):
    def __init__(self, s1):
        super().__init__(s1)

class Edge(Piece):
    def __init__(self, s1, s2):
        super().__init__(s1, s2)

class Corner(Piece):
    def __init__(self, s1, s2, s3):
        super().__init__(s1, s2, s3)

class Move:
    def __init__(self, depth: str, face: str):
        self.depth = depth
        self.face = face

    def show(self):
        print(self.depth, self.face)

class Solid:
    def spawn_centers(self) -> List[Center]:
        return [Center(Sticker(i, int((self.order + 1) / 2))) for i in range(self.faces)] if self.order % 2 == 1 else []

    def spawn_edges(self) -> List[Edge]:
        edges: List[Edge] = []
        if self.order % 2 == 1:
            for i in range(len(self.adjMat)):
                for j in range(len(self.adjMat[i])):
                    for d1 in range(1, int((self.order + 1) / 2)):
                        for d2 in range(1, int((self.order + 1) / 2)):
                            for d3 in range(1, int((self.order + 1) / 2)):
                                if 1 in (d1, d2):
                                    edge = Edge(Sticker(i, d1), Sticker(self.adjMat[i][j], d2))
                                    if [set(edge.pos()), edge.depth()] not in [[EDGE.pos, EDGE.depth] for EDGE in edges]:
                                        edges.append(edge)
        return edges

    def spawn_corners(self) -> List[Corner]:
        corners: List[Corner] = []
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat[i])):
                for d1 in range(1, int(self.order / 2) + 1):
                    for d2 in range(1, int(self.order / 2) + 1):
                        for d3 in range(1, int(self.order / 2) + 1):
                            if 1 in (d1, d2, d3):
                                corner = Corner(Sticker(i, d1), Sticker(self.adjMat[i][j - 1], d2), Sticker(self.adjMat[i][j], d3))
                                if [set(corner.pos()), corner.depth()] not in [[CORNER.pos, CORNER.depth] for CORNER in corners]:
                                    corners.append(corner)

        return corners

    def find_opp_faces(self):
        opp_faces = dict()
        for i in range(self.faces):
            adj_faces = [i]
            for j in ff:
                for k in self.adjMat[j]:
                    if k not in adj_faces:
                        adj_faces.append(k)
                if len(ff) == len(self.adjMat) - 1:
                    op[i] = [face for face in range(self.faces) if face not in adj_faces][0]
                    break
        return opp_faces
    
    def __init__(self, order: int, adjMat: List[List[int]]):
        self.order = order
        self.adjMat = adjMat
        self.faces = len(adjMat)
        self.sides = len(adjMat[0])
        self.oppDict = self.find_opp_faces()
        self.centers = self.spawn_centers()
        self.edges = self.spawn_edges()
        self.corners = self.spawn_corners()
        self.pieces = self.centers

    def alg_format(self, alg: str, style: str) -> List[Move]:
        '''Converts an algorithm string with moves seperated by spaces in
either WCA, SigN or prefix format and return a list of moves as strings
in modified prefix format.

In the modified format, there are no brackets, wide moves and all moves
state how many ayers they turn, not just wide moves, even for small
puzzles like 3x3x3.'''
        # If brackers have a number at the end, expand the brackets, and
        # remove them. Eg "(R U R' U')2" expands to "R U R' U' R U R' U'"
        # Split the alg into strings with backs and strings with brackets.
        # Expand the brackets on items with brackets.  Join the strings.
        print(alg, ': alg')
        split_alg = re.split(r'(\(.*\)[0-9])', alg)
        print(split_alg, ': split_alg')
        for i in range(len(split_alg)):
            if re.match(r'\(|\)', split_alg[i]):
                # Brackets only need to be expanded if the last character is a
                # number.
                if split_alg[i][-1] in '1234567890':
                    count = int(split_alg[i][-1])
                    # Replace number with space
                    split_alg[i] = split_alg[i][:-1] + ' '
                    split_alg[i] = split_alg[i] * count
                # Remove brackets.
                split_alg[i] = re.sub(r'\(|\)', '', split_alg[i])
        alg = (' ').join(split_alg).strip()
        # List of moves.
        list_alg = re.split('\s+', alg)
        print(list_alg, ': list_alg')
        assert style in ('WCA', 'SiGN', 'prefix')
        # Following functions foramt list_alg to prefix format,
        def WCA(list_alg: List[str]) -> List[str]:
            format_alg = []
            for move in list_alg:
                # Wide move turing 3 or layesrs.
                if move[0] in '1234567890':
                    move = move.replace('w', '')
                # Wide move turining one layer.
                elif 'w' in move:
                    move = '2' + move.replace('w', '')
                format_alg.append(move)
            return format_alg

        def SiGN(list_alg: List[str]) -> List[str]:
            return [move.upper() for move in list_alg]

        def prefix(list_alg: List[str]) -> List[str]:
            return list_alg

        prefix_alg = eval(style)(list_alg)
        # Prepend '1' to the beginnig of moves.
        for i in range(len(prefix_alg)):
            if prefix_alg[i] not in '1234567890':
                prefix_alg[i] = '1' + prefix_alg[i]
        print(prefix_alg, ': prefix_alg')
        # Change double moves and prime moves to single moves. 
        # For a dodecahedron: U2' -> U U U.
        format_alg = []
        for move in prefix_alg:
            # Prime move.
            if move[-1] == "'":
                # Prime move and double turn.
                if re.search(r'[0-9]', move[-1]):
                    r = range(self.sides - int(move[-2]))
                    move = move[:-2]
                # Single prime move.
                elif re.search(r'[a-zA-Z]', move[-2]):
                    r = range(self.sides - 1)
                    move = move[:-1]
                else:
                    raise ValueError(move + ' unknown move.')
            # Double turn and not primve.
            elif move[-1] in '1234567890':
                r = range(int(move[-1]))
                move = move[:-1]
            # Single turn.
            elif re.search(r'[a-zA-Z]+', move[1:]):
                r = range(1)
            else:
                raise ValueError(move + ' unknown move.')
            for _ in r:
                format_alg.append(Move(move[0], move[1:]))
        print([move.show() for move in format_alg], ': format_alg')
        return format_alg

        def alg_show(self, alg: List[str], type: Callable[[List[str]], str]) -> str:
            '''Show internal representation of alg in type format.'''
            pass
    
        def alg_exec(self, alg: List[Tuple[str, int]]):
            # U 0
            # F 1
            # R 2
            # B 3
            # L 4
            # D 5
            # ...
            for MOVE in alg:
                # move: (move, depth)
                move, depth = MOVE
                # Face turn.
                if move in 'FBUDLR':
                    pass
                # Rotation.
                elif move in 'xyz':
                    pass
                # Error.
                else:
                    raise AssertionError(move + 'is not a valid move.')


    def solved_p(self) -> bool:
        # Return true if for each face, all the colours of the stickers
        # of that lies on the face are the same for all pieces of the
        # puzzle, otherwise return false.

        # Mypy bug fix:
        edges: List[Any] = self.edges
        corners: List[Aly] = self.corners
        pieces = edges + corners
        return all(len(set(colour for piece in pieces for colour, pos in zip(piece.colour(), piece.pos()) if pos == face)) == 1 for face in range(self.faces))
        # # Does not work mypy doesn't (currently) allow + on lists with
        # # different types of items.
        # return all(len(set(colour for piece in self.edges + self.corners for colour, pos in zip(piece.colour(), piece.pos()) if pos == face)) == 1 for face in range(self.faces))

    def scramble(self):
        moves = 'RBUDLR'
        r = range(shape.sides - 1)
        for _ in range(len(shape.pieces)):
            exec_move((random.choice(r), random.choice(moves), random.choice(r)))

    def __show_pieces(self, pieces):
        print([piece.show for piece in pieces])

    def show_centers(self):
        __show_pieces(self.centers)

    def show_edges(self):
        __show_pieces(self.edges)

    def show_corners(self):
        __show_pieces(self.corners)

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
            adjMat = [[1,2,3], # 0
                      [0,3,2], # 1
                      [0,1,3], # 2
                      [0,2,1]] # 3
        )

    def rotate(self):
        # Tetrahedron is the only solid that does not have opposite
        # faces that are parallel, the rotatate procudure will not work.
        pass

class Cube(Solid):
    def __init__(self, order: int):
        super().__init__(
            order = order,
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

alg = "R U' R' R (R U R' U')2"
p = Cube(3)
print(p.solved_p())
