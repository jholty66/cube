import alg; import math

phi=(1+math.sqrt(5))/2

class Sticker:
    def __init__(self, pos, depth):
        self.colour = pos # self.colour is immutable
        self.pos = pos
        self.depth = depth

class Piece:
    def __init__(self, *stickers): self.stickers = list(stickers)
    def colour(self): return [sticker.colour for sticker in self.stickers]
    def pos(self): return [sticker.pos for sticker in self.stickers]
    def depth(self): return [sticker.depth for sticker in self.stickers]
    def __str__(self): return f'{self.colour()}\t{self.pos()}\t{self.depth()}'

class Solid:
    def spawn_centers(self):
        return [Piece(Sticker(i, int((self.size + 1) / 2))) for i in range(self.numFaces)] if self.size % 2 == 1 else []

    def spawn_edges(self):
        edges = []
        if self.size % 2 == 1:
            for i in range(len(self.adj_mat)):
                for j in range(len(self.adj_mat[i])):
                    for d1 in range(1, int((self.size + 1) / 2)):
                        for d2 in range(1, int((self.size + 1) / 2)):
                            for d3 in range(1, int((self.size + 1) / 2)):
                                if 1 in (d1, d2):
                                    edge = Piece(Sticker(i, d1), Sticker(self.adj_mat[i][j], d2))
                                    if [edge.pos(), edge.depth()] not in [[set(EDGE.pos()), EDGE.depth()] for EDGE in edges]:
                                        edges.append(edge)
        return edges

    def spawn_corners(self):
        corners = []
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat[i])):
                for d1 in range(1, int(self.size / 2) + 1):
                    for d2 in range(1, int(self.size / 2) + 1):
                        for d3 in range(1, int(self.size / 2) + 1):
                            if 1 in (d1, d2, d3):
                                corner = Piece(Sticker(i, d1), Sticker(self.adj_mat[i][j - 1], d2), Sticker(self.adj_mat[i][j], d3))
                                if [corner.pos(), corner.depth()] not in [[set(CORNER.pos()), CORNER.depth()] for CORNER in corners]:
                                    corners.append(corner)

        return corners

    def spawn_faces(self):
        # Create list of faces that contain list of points.
        # Every point appears in 3 faces.
        # Pairs of adjacent points appear in 2 faces.
        points = self.num_sides
        faces = [list(range(points))] + [None] * (self.numFaces - 1)
        def findPair():
            # Pick two adjacent points on an adjacent face.
            for adjface, j in enumerate(faces):
                if j in self.adj_mat[i] and adjface != None:
                    for p, _ in enumerate(adjface):
                        pair = [adjface[p], adjface[p - 1]] 
                        if all(point not in fullPoints for point in pair) and set(pair) not in fullPairs:
                            fullPairs.append(set(pair)); return pair
            print('Error count not find any pairs'); quit()

        def findPoint(dir):
            while True:
                for adjface, j in enumerate(faces):
                    if j in self.adj_mat[i] and adjface != None:
                        for k, point in enumerate(adjface):
                            if point == face[-1]:
                                if set(point, face[face.index(point) - dir % len(self.num_sides)]) == set(adjface[p], adjface[(p + dir) % len(self.num_sides)]):
                                    faces.insert(0 if dir == 1 else -1, point)

        for i in range(self.numFaces - 1):
            face = findPair() # Use function to return out of double for loop.
            # Add adjacent points before the first point in the pair that lie on adjacent faces.
            findPoint(1)
            # Add adjacent points after the second point in the pair that lie on adjacent faces.
            findPoint(-1)
            # If there are no adjacent faces and the face does not have all its points, create new points on the face.
            if len(face) < self.num_sides:
                newPoints = range(1 + points, 1 + (self.num_sides - len(face))) 
                face += newPoints; points += len(newPoints)
        assert len(faces) == self.numFaces
        print(points); return faces

    def __init__(self, size, order, points, adj_mat, move_face):
        self.size = size
        self.order = order # Order is the number of faces that meet at a point.
        self.points = points
        self.adj_mat = adj_mat
        self.move_face = move_face # Describes what face a move should turn, varies between solids.
        self.num_faces = len(adj_mat)
        self.num_sides = len(adj_mat[0])
        self.faces = spawn_faces()
        self.centers = self.spawn_centers()
        self.edges = self.spawn_edges()
        self.corners = self.spawn_corners()

    def face_turn(self, move):
        dir = 1 if move.prime == True else -1;dir*=move.count
        # Centers can be ignored as they do not change position when
        # turning a face.
        for piece in self.corners + self.edges:
            # Find pieces that are on the face that is being turned.
            # Change the positions of the stickers on the piece.
            if any(sticker.pos == self.move_face[move.name] for sticker in piece.stickers):
                for sticker in piece.stickers:
                    if sticker.pos != self.move_face[move.name]:
                        sticker.pos = self.adj_mat[self.move_face[move.name]][(self.adj_mat[self.move_face[move.name]].index(sticker.pos) + dir) % self.num_sides]


    def slice_turn(self, move): pass

    # To be defined in child classes.
    def x(self): pass
    def x_prime(self): pass
    def y(self): pass
    def y_prime(self): pass
    def z(self): pass
    def z_prime(self): pass

    # {(move.name move.prime): rotate_fn}
    rotate = {('x', False): x,
              ('x', True): x_prime,
              ('y', False): y,
              ('y', True): y_prime,
              ('z', False): z,
              ('z', True): z_prime}

    def exec_alg(self, alg_str):
        for move in alg.create(alg_str):
            if move.type=='face': self.face_turn(move)
            elif move.type=='rotation': self.rotate[(move.name, move.prime)]()
            elif move.type=='slice': slice_turn(move)
            else: raise ValueError

    def solved(self):
        # Return false if there is one more colour of sticker on a face,
        # else return true.
        face_colour = [None] * self.numFaces
        for piece in self.centers + self.edges + self.corners:
            for colour, pos in zip(piece.colour(), piece.pos()):
                if face_colour[pos] == None: face_colour[pos] = colour
                elif face_colour[pos] != colour: return False
        return True

    def __str__(self):
        def show(pieces):
            s=''
            for piece in pieces: s += piece.__str__() + '\n'
            return s

        return f'''Centers:
colour | pos | depth
{show(self.centers)}
Edges:
colour | pos | depth
{show(self.edges)}
Corners:
colour | pos | depth
{show(self.corners)}
Centers: {len(self.centers)}
Edges: {len(self.edges)}
Corners: {len(self.corners)}

Movable: {len(self.edges)+len(self.corners)}
Total: {len(self.centers)+len(self.edges)+len(self.corners)}'''

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
    def __init__(self, size):
        super().__init__(size = size, order= 3,
                         points = ((1,1,1),
                                   (1,-1,-1),
                                   (-1,1,-1),
                                   (-1,-1,1)),
                         adj_mat = ((1,2,3),  # 0
                                    (0,3,2),  # 1
                                    (0,1,3),  # 2
                                    (0,2,1)), # 3
                         move_face = {'U':0,
                                      'R':1,
                                      'B':2,
                                      'L':3})

class Cube(Square):
    def __init__(self, size):
        super().__init__(size = size, order = 3,
                         points = ((1,1,1),
                                   (1,1,-1),
                                   (1,-1,1),
                                   (1,-1,-1),
                                   (-1,1,1),
                                   (-1,1,-1),
                                   (-1,-1,1),
                                   (-1,-1,-1)), 
                         adj_mat = ((1,2,3,4),   # 0
                                    (2,0,4,5),   # 1
                                    (3,0,1,5),   # 2
                                    (4,0,2,5),   # 3
                                    (1,0,3,5),   # 4
                                    (1,4,3,2)),  # 5
                         move_face = {'U':0,
                                      'F':1,
                                      'R':2,
                                      'B':3,
                                      'L':4,
                                      'D':5})

class Octahedron(Triangle):
    def __init__(self, size):
        super().__init__(size = size, order = 4,
                         points=((1,0,0),
                                 (-1,0,0),
                                 (0,1,0),
                                 (0,-1,0),
                                 (0,0,1),
                                 (0,0,-1)),
                         adj_mat = ((1,2,3),  # 0
                                    (0,4,6),  # 1
                                    (0,6,5),  # 2
                                    (0,5,4),  # 3
                                    (3,7,1),  # 4
                                    (3,2,7),  # 5
                                    (2,1,7),  # 6
                                    (4,5,6)), # 7
                         move_face = {})

class Dodecahedron(Pentagon):
    def __init__(self, size):
        super().__init__(size = size, order = 3,
                         points=((0,phi,1/phi),
                                 (0,phi,-1/phi),
                                 (0,-phi,1/phi),
                                 (0,-phi,-1/phi),
                                 (1/phi,0,phi),
                                 (1/phi,0,-phi),
                                 (-1/phi,0,phi),
                                 (-1/phi,0,-phi),
                                 (phi,1/phi,0),
                                 (phi,-1/phi,0),
                                 (-phi,1/phi,0),
                                 (-phi,-1/phi,0),
                                 (1,1,1),
                                 (1,1,-1),
                                 (1,-1,1),
                                 (1,-1,-1),
                                 (-1,1,1),
                                 (-1,1,-1),
                                 (-1,-1,1),
                                 (-1,-1,-1)),
                         adj_mat = ((1,2,3,4,5),   # 0
                                    (0,5,6,7,2),   # 1
                                    (0,1,7,8,3),   # 2
                                    (0,2,8,9,4),   # 3
                                    (0,3,9,10,5),  # 4
                                    (0,4,10,6,1),  # 5
                                    (1,5,10,11,7), # 6
                                    (1,6,11,8,2),  # 7
                                    (2,7,11,9,3),  # 8
                                    (3,8,11,10,4), # 9
                                    (4,9,11,6,5),  # 10
                                    (10,9,8,7,6)), # 11
                         move_face = {'U':0,
                                      'F':1,
                                      'R':2,
                                      'BR':3,
                                      'BL':4,
                                      'L':5,
                                      'DR':7,
                                      'DL':6})

class Icosahedron(Triangle):
    def __init__(self, size):
        super().__init__(size = size, order = 5,
                         points=((0,1/phi,1),
                                 (0,1/phi,-1),
                                 (0,-1/phi,1),
                                 (0,-1/phi,-1),
                                 (1,0,1/phi),
                                 (1,0,-1/phi),
                                 (-1,0,1/phi),
                                 (-1,0,-1/phi),
                                 (1/phi,1,0),
                                 (1/phi,-1,0),
                                 (-1/phi,1,0),
                                 (-1/phi,-1,0)),
                         adj_mat = ((1,3,18),   # 0
                                    (5,0,17),   # 1
                                    (3,6,19),   # 2
                                    (0,4,2),    # 3
                                    (5,7,3),    # 4
                                    (8,4,1),    # 5
                                    (7,10,2),   # 6
                                    (4,9,6),    # 7
                                    (5,12,9),   # 8
                                    (8,11,7),   # 9
                                    (11,15,6),  # 10
                                    (13,10,9),  # 11
                                    (8,17,13),  # 12
                                    (12,14,11), # 13
                                    (13,16,15), # 14
                                    (14,19,10), # 15
                                    (17,18,14), # 16
                                    (16,12,1),  # 17
                                    (19,16,0),  # 18
                                    (15,18,2)), # 19
                         move_face = {})
