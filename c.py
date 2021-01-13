from a import *
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
    def __str__(self): return str(self.colour(), self.pos(), self.depth()

class Center(Piece):
    def __init__(self, s1): super().__init__(s1)
class Edge(Piece):
    def __init__(self, s1, s2):super().__init__(s1, s2)
class Corner(Piece):
    def __init__(self, s1, s2, s3):super().__init__(s1, s2, s3)

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

    def face_turn(self, move):
        dir = 1 if move.prime == True else -1
        # Centers can be ignored as they do not change position when
        # turning a face.
        for piece in self.corners + self.edges:
            # Find pieces that are on the face that is being turned.
            # Change the positions of the stickers on the piece.
            if any(sticker.pos == self.move_face[move.name] for sticker in piece.stickers):
                for sticker in piece.stickers:
                    if sticker.pos != self.move_face[move.name]:
                        sticker.pos = self.adj_mat[self.move_face[move.name]][(self.adj_mat[self.move_face[move.name]].index(sticker.pos) + dir) % self.sides]

    def solved(self):
        # Return false if there is one more colour of sticker on a face,
        # else return true.
        face_colour = [None] * self.faces
        for piece in self.centers + self.edges + self.corners:
            for colour, pos in zip(piece.colour(), piece.pos()):
                if face_colour[pos] == None:
                    face_colour[pos] = colour
                elif face_colour[pos] != colour:
                    return False
        return True

    def __str__(self):
        return f'Centers:\n{[center.__str__() for center in self.centers)]}\n\nEdges:\n{[edges.__str__() for edge in self.edges]}\n\nCorners:\n{[corner.__str__() for corner in self.corners]}\n\nCenters: {len(self.centers)}\nEdges: {len(self.edges)}\nCorners: {len(self.corners)}\n\nTotal {len(self.centers)+len(self.edges)+len(self.corners)}'

class Triangle(Solid):
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