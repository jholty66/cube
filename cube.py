#!/usr/bin/env python3.9

# Prime moves were origionally ignored (number sides - 1 normal moves
# were used instead) they are now added to improve performance.
#
# Rewrite solved function to only work on a given face.

import random, re

class Sticker:
    def __init__(self, pos, depth):
        self.colour = pos # self.colour is immutable
        self.pos = pos
        self.depth = depth

class Piece:
    def __init__(self, *stickers):self.stickers = list(stickers)
    def colour(self): return [sticker.colour for sticker in self.stickers]
    def pos(self): return [sticker.pos for sticker in self.stickers]
    def depth(self):return [sticker.depth for sticker in self.stickers]
    def show(self): print(self.colour(), self.pos(), self.depth())

class Center(Piece):
    def __init__(self, s1): super().__init__(s1)
class Edge(Piece):
    def __init__(self, s1, s2):super().__init__(s1, s2)
class Corner(Piece):
    def __init__(self, s1, s2, s3):super().__init__(s1, s2, s3)

class Move:
    def __init__(self, depth, name, prime):
        self.depth = depth
        self.name = name
        self.prime = prime
    def show(self): print(self.depth, self.name)

class Solid:
    def spawn_centers(self):
        return [Center(Sticker(i, int((self.order + 1) / 2))) for i in range(self.faces)] if self.order % 2 == 1 else []

    def spawn_edges(self):
        edges = []
        if self.order % 2 == 1:
            for i in range(len(self.adj_mat)):
                for j in range(len(self.adj_mat[i])):
                    for d1 in range(1, int((self.order + 1) / 2)):
                        for d2 in range(1, int((self.order + 1) / 2)):
                            for d3 in range(1, int((self.order + 1) / 2)):
                                if 1 in (d1, d2):
                                    edge = Edge(Sticker(i, d1), Sticker(self.adj_mat[i][j], d2))
                                    if [set(edge.pos()), edge.depth()] not in [[EDGE.pos, EDGE.depth] for EDGE in edges]:
                                        edges.append(edge)
        return edges

    def spawn_corners(self):
        corners = []
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat[i])):
                for d1 in range(1, int(self.order / 2) + 1):
                    for d2 in range(1, int(self.order / 2) + 1):
                        for d3 in range(1, int(self.order / 2) + 1):
                            if 1 in (d1, d2, d3):
                                corner = Corner(Sticker(i, d1), Sticker(self.adj_mat[i][j - 1], d2), Sticker(self.adj_mat[i][j], d3))
                                if [set(corner.pos()), corner.depth()] not in [[CORNER.pos, CORNER.depth] for CORNER in corners]:
                                    corners.append(corner)

        return corners

    def __init__(self, order, adj_mat, move_face):
        self.order = order
        self.adj_mat = adj_mat
        self.move_face = move_face # Describes what face a move should turn, varies between solids.
        self.faces = len(adj_mat)
        self.sides = len(adj_mat[0])
        self.centers = self.spawn_centers()
        self.edges = self.spawn_edges()
        self.corners = self.spawn_corners()

    class Alg(): # More of a namespace than a class.
        def face_turn(move):
            dir = 1 if move.prime == True else -1
            # Centers can be ignored as they do not change position when
            # turning a face.
            for piece in self.corners + self.edges:
                # Find pieces that are on the face that is being turned.
                # Change the positions of the stickers on the piece.
                if any(sticker.pos == move_face[move.face] for sticker in piece.stickers) and len(self.piece) > 1:
                    for sticker in piece.stickers:
                        if sticker.pos != move_face[move.face]:
                            print(self.adj_mat[move_face[move.face]], sticker.pos)
                            sticker.pos = self.adj_mat[move_face[move.face]][self.adj_mat[move_face].index(sticker.pos) + dir]
                            print(self.adj_mat[move_face[move.face]], sticker.pos)
            self.show_all()

    def solved(self):
        # Go over all pices, add the colour of the stickers to a set for each
        # face.  If the length of the sets are 1, then return true.
        face_colour = [None] * self.faces
        for piece in self.centers + self.edges + self.corners:
            for colour, pos in zip(piece.colour(), piece.pos()):
                if face_colour[pos] == None:
                    face_colour[pos] = colour
                elif face_colour[pos] != colour:
                    return False
        return True

    def show_pieces(self, pieces): print([piece.show() for piece in pieces])
    def show_centers(self): self.show_pieces(self.centers)
    def show_edges(self): self.show_pieces(self.edges)
    def show_corners(self): self.show_pieces(self.corners)

    def show_all(self):
        self.show_centers();print()
        self.show_edges();print()
        self.show_corners();print()
        print(len(self.centers), len(self.edges), len(self.corners))
        print(len(self.centers) + len(self.edges) + len(self.corners))

class Triangle(Solid):
    class Alg(Solid.Alg):
        def x(self):
            self.move_face["B"] = self.move_face["L"]
            self.move_face["L"] = self.move_face["U"]
            self.move_face["U"] = self.adj_mat[self.adj_mat.index(move_face["L"]) + 1]

        def x_prime(self):
            self.move_face["B"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["L"]
            self.move_face["L"] = self.adj_mat[self.adj_mat.index(move_face["U"]) + 1]

        def y(self):
            self.move_face["L"] = self.move_face["B"]
            self.move_face["B"] = self.move_face["R"]
            self.move_face["R"] = self.adj_mat[self.adj_mat.index(move_face["B"]) + 1]

        def y_prime(self):
            self.move_face["L"] = self.move_face["B"]
            self.move_face["B"] = self.move_face["R"]
            self.move_face["R"] = self.adj_mat[self.adj_mat.index(move_face["B"]) + 1]

        # Not sure if z rotations go the right way as there are no F on
        # tetrahedrons, assuming it rotatates in the direction of a B"
        # turn.
        def z(self):
            self.move_face["R"] = self.move_face["L"]
            self.move_face["L"] = self.move_face["U"]
            self.move_face["U"] = self.adj_mat[self.adj_mat.index(move_face["L"]) + 1]

        def z_prime(self):
            self.move_face["R"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["L"]
            self.move_face["L"] = self.adj_mat[self.adj_mat.index(move_face["U"]) + 1]

class Square(Solid):
    class Alg(Solid.Alg):
        def x(self):
            self.move_face["B"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["D"]
            self.move_face["D"] = self.adj_mat[self.adj_mat.index(move_face["F"]) + 1]

        def x_prime(self):
            self.move_face["B"] = self.move_face["D"]
            self.move_face["D"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["U"]
            self.move_face["U"] = self.adj_mat[self.adj_mat.index(move_face["F"]) + 1]

        def y(self):
            self.move_face["L"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["B"]
            self.move_face["B"] = self.adj_mat[self.adj_mat.index(move_face["R"] + 1)]

        def y_prime(self):
            self.move_face["L"] = self.move_face["B"]
            self.move_face["B"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["U"]
            self.move_face["U"] = self.adj_mat[self.adj_mat.index(move_face["R"] + 1)]

        def z(self):
            self.move_face["D"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["L"]
            self.move_face["L"] = self.adj_mat[self.adj_mat.index(move_face["U"] + 1)]

        def z_prime(self):
            self.move_face["D"] = self.move_face["L"]
            self.move_face["L"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["R"]
            self.move_face["R"] = self.adj_mat[self.adj_mat.index(move_face["U"] + 1)]

class Pentagon(Solid):
    class Alg(Solid.Alg):
        def x(self):
            self.move_face["BR"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["D"]
            self.move_face["D"] = self.adj_mat[self.adj_mat.index(move_face["F"]) + 1]

        def x_prime(self):
            self.move_face["BR"] = self.move_face["D"]
            self.move_face["D"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["U"]
            self.move_face["U"] = self.adj_mat[self.adj_mat.index(move_face["F"]) + 1]

        def y(self):
            self.move_face["L"] = self.move_face["F"]
            self.move_face["F"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["BR"]
            self.move_face["BR"] = self.move_face["BL"]
            self.move_face["BL"] = self.adj_mat[self.adj_mat.index(move_face["BR"] + 1)]

        def y_prime(self):
            self.move_face["L"] = self.move_face["BL"]
            self.move_face["BL"] = self.move_face["BR"]
            self.move_face["BR"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["F"]
            self.move_face["F"] = self.adj_mat[self.adj_mat.index(move_face["R"] + 1)]

        def z(self):
            self.move_face["DL"] = self.move_face["DR"]
            self.move_face["DR"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["L"]
            self.move_face["L"] = self.adj_mat[self.adj_mat.index(move_face["U"] + 1)]

        def z_prime(self):
            self.move_face["DL"] = self.move_face["L"]
            self.move_face["L"] = self.move_face["U"]
            self.move_face["U"] = self.move_face["R"]
            self.move_face["R"] = self.move_face["DR"]
            self.move_face["DR"] = self.adj_mat[self.adj_mat.index(move_face["R"] + 1)]

class Tetrahedron(Triangle):
    def __init__(self, order):
        super().__init__(order = order,
                         adj_mat = [[1,2,3], # 0
                                    [0,3,2], # 1
                                    [0,1,3], # 2
                                    [0,2,1]],# 3
                         move_face = {'U':0,
                                      'R':1,
                                      'B':2,
                                      'L':3})

class Cube(Square):
    def __init__(self, order):
        super().__init__(order = order,
                         adj_mat = [[1,2,3,4], # 0
                                    [2,0,4,5], # 1
                                    [3,0,1,5], # 2
                                    [4,0,2,5], # 3
                                    [1,0,3,5], # 4
                                    [1,4,3,2]],# 5
                         move_face = {'U':0,
                                      'F':1,
                                      'R':2,
                                      'B':3,
                                      'L':4,
                                      'D':5})

class Octahedron(Triangle):
    def __init__(self, order):
        super().__init__(order = order,
                         adj_mat = [[1,2,3], # 0
                                    [0,4,6], # 1
                                    [0,6,5], # 2
                                    [0,5,4], # 3
                                    [3,7,1], # 4
                                    [3,2,7], # 5
                                    [2,1,7], # 6
                                    [4,5,6]],# 7
                         move_face = {})

class Dodecahedron(Pentagon):
    def __init__(self, order):
        super().__init__(order = order,
                         adj_mat = [[1,2,3,4,5],   # 0
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
                                    [10,9,8,7,6]], # 11
                         move_face = {'U':0,
                                      'F':1,
                                      'R':2,
                                      'BR':3,
                                      'BL':4,
                                      'L':5,
                                      'DR':7,
                                      'DL':6})

class Icosahedron(Triangle):
    def __init__(self, order):
        super().__init__(order = order,
                         adj_mat = [[1,3,18],   # 0
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
                                    [15,18,2]], # 19
                         move_face = {})

alg = "R U' R' R (R U R' U')2"
p = Cube(3)
print(p.solved())
