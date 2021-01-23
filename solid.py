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
        def makeFaces(self):
            # Create list of faces that contain list of points.
            # Every point appears in 3 faces.
            # Pairs of adjacent points appear in 2 faces.
            numPoints = self.numSides; fullPoints = set(); fullPairs = []
            faces = [list(range(numPoints))] + [None] * (self.numFaces - 1)

            def findPair():
                # Pick two adjacent points on an adjacent face.
                for adjface, j in enumerate(faces):
                    if j in self.adjmat[i] and adjface != None:
                        for p, _ in enumerate(adjface):
                            pair = [adjface[p], adjface[p - 1]] 
                            if all(point not in fullPoints for point in pair) and set(pair) not in fullPairs:
                                fullPoints = set(point for point in [point for face in faces for point in face] if points.count(point) == 3)
                                fullPairs.append(set(pair))
                                return pair
                print('Error count not find any pairs'); quit()

            def findPoint(dir):
                while True:
                    for adjface, j in enumerate(faces):
                        if j in self.adjmat[i] and adjface != None:
                            for k, point in enumerate(adjface):
                                if point == face[-1]:
                                    if set(point, face[face.index(point) - dir % len(self.numSides)]) == set(adjface[p], adjface[(p + dir) % len(self.numSides)]):
                                        fullPoints = set(point for point in [point for face in faces for point in face] if points.count(point) == 3)
                                        fullPairs.append(set(pair))
                                        faces.insert(0 if dir == 1 else -1, point)

            for i in range(self.numFaces - 1):
                face = findPair() # Use function to return out of double for loop.
                # Add adjacent points before the first point in the pair that lie on adjacent faces.
                findPoint(1)
                # Add adjacent points after the second point in the pair that lie on adjacent faces.
                findPoint(-1)
                # If there are no adjacent faces and the face does not have all its points, create new points on the face.
                if len(face) < self.numSides:
                    newPoints = range(1 + numPoints, 1 + (self.numSides - len(face))) 
                    face += newPoints; numPoints += len(newPoints)
            assert len(faces) == self.numFaces; print(numPoints); return faces

    def __init__(self, size, order, points, adjmat, moveFace):
        self.size = size
        self.order = order # Order is the number of faces that meet at a point.
        self.points = points
        self.adjmat = adjmat
        self.moveFace = moveFace # Describes what face a move should turn, varies between solids.
        self.numFaces = len(adjmat)
        self.numSides = len(adjmat[0])

        centers = [Piece(Sticker(i, int((self.size + 1) / 2))) for i in range(self.numFaces)] if self.size % 2 == 1 else []

        edges = []

        if self.size % 2 == 1:
            for i in range(len(self.adjmat)):
                for j in range(len(self.adjmat[i])):
                    for d1 in range(1, int((self.size + 1) / 2)):
                        for d2 in range(1, int((self.size + 1) / 2)):
                            for d3 in range(1, int((self.size + 1) / 2)):
                                if 1 in (d1, d2):
                                    edge = Piece(Sticker(i, d1), Sticker(self.adjmat[i][j], d2))
                                    if [edge.pos(), edge.depth()] not in [[set(EDGE.pos()), EDGE.depth()] for EDGE in edges]:
                                        edges.append(edge)
        
        corners = []
        for i in range(len(self.adjmat)):
            for j in range(len(self.adjmat[i])):
                for d1 in range(1, int(self.size / 2) + 1):
                    for d2 in range(1, int(self.size / 2) + 1):
                        for d3 in range(1, int(self.size / 2) + 1):
                            if 1 in (d1, d2, d3):
                                corner = Piece(Sticker(i, d1), Sticker(self.adjmat[i][j - 1], d2), Sticker(self.adjmat[i][j], d3))
                                if [corner.pos(), corner.depth()] not in [[set(CORNER.pos()), CORNER.depth()] for CORNER in corners]:
                                    corners.append(corner)

def faceTurn(self, move):
        dir = 1 if move.prime == True else -1;dir*=move.count
        # Centers can be ignored as they do not change position when
        # turning a face.
        for piece in self.corners + self.edges:
            # Find pieces that are on the face that is being turned.
            # Change the positions of the stickers on the piece.
            if any(sticker.pos == self.moveFace[move.name] for sticker in piece.stickers):
                for sticker in piece.stickers:
                    if sticker.pos != self.moveFace[move.name]:
                        sticker.pos = self.adjmat[self.moveFace[move.name]][(self.adjmat[self.moveFace[move.name]].index(sticker.pos) + dir) % self.numSides]


    def sliceTurn(self, move): pass

    # To be defined in child classes.
    def x(self): pass
    def xPrime(self): pass
    def y(self): pass
    def yPrime(self): pass
    def z(self): pass
    def zPrime(self): pass

    # {(move.name move.prime): rotate fn}
    rotate = {('x', False): x,
              ('x', True): xPrime,
              ('y', False): y,
              ('y', True): yPrime,
              ('z', False): z,
              ('z', True): zPrime}

    def execAlg(self, algStr):
        for move in alg.create(algStr):
            if move.type=='face': self.faceTurn(move)
            elif move.type=='rotation': self.rotate[(move.name, move.prime)]()
            elif move.type=='slice': sliceTurn(move)
            else: raise ValueError

    def solved(self):
        # Return false if there is one more colour of sticker on a face,
        # else return true.
        faceColour = [None] * self.numFaces
        for piece in self.centers + self.edges + self.corners:
            for colour, pos in zip(piece.colour(), piece.pos()):
                if faceColour[pos] == None: faceColour[pos] = colour
                elif faceColour[pos] != colour: return False
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
        self.moveFace["B"] = self.moveFace["L"]
        self.moveFace["L"] = self.moveFace["U"]
        self.moveFace["U"] = self.adjmat[self.adjmat.index(moveFace["L"]) + 1]

    def xPrime(self):
        self.moveFace["B"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["L"]
        self.moveFace["L"] = self.adjmat[self.adjmat.index(moveFace["U"]) + 1]

    def y(self):
        self.moveFace["L"] = self.moveFace["B"]
        self.moveFace["B"] = self.moveFace["R"]
        self.moveFace["R"] = self.adjmat[self.adjmat.index(moveFace["B"]) + 1]

    def yPrime(self):
        self.moveFace["L"] = self.moveFace["B"]
        self.moveFace["B"] = self.moveFace["R"]
        self.moveFace["R"] = self.adjmat[self.adjmat.index(moveFace["B"]) + 1]

    # Not sure if z rotations go the right way as there are no F on
    # tetrahedrons, assuming it rotatates in the direction of a B"
    # turn.
    def z(self):
        self.moveFace["R"] = self.moveFace["L"]
        self.moveFace["L"] = self.moveFace["U"]
        self.moveFace["U"] = self.adjmat[self.adjmat.index(moveFace["L"]) + 1]

    def zPrime(self):
        self.moveFace["R"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["L"]
        self.moveFace["L"] = self.adjmat[self.adjmat.index(moveFace["U"]) + 1]

class Square(Solid):
    def x(self):
        self.moveFace["B"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["D"]
        self.moveFace["D"] = self.adjmat[self.adjmat.index(moveFace["F"]) + 1]

    def xPrime(self):
        self.moveFace["B"] = self.moveFace["D"]
        self.moveFace["D"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["U"]
        self.moveFace["U"] = self.adjmat[self.adjmat.index(moveFace["F"]) + 1]

    def y(self):
        self.moveFace["L"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["B"]
        self.moveFace["B"] = self.adjmat[self.adjmat.index(moveFace["R"] + 1)]

    def yPrime(self):
        self.moveFace["L"] = self.moveFace["B"]
        self.moveFace["B"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["U"]
        self.moveFace["U"] = self.adjmat[self.adjmat.index(moveFace["R"] + 1)]

    def z(self):
        self.moveFace["D"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["L"]
        self.moveFace["L"] = self.adjmat[self.adjmat.index(moveFace["U"] + 1)]

    def zPrime(self):
        self.moveFace["D"] = self.moveFace["L"]
        self.moveFace["L"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["R"]
        self.moveFace["R"] = self.adjmat[self.adjmat.index(moveFace["U"] + 1)]

class Pentagon(Solid):
    def x(self):
        self.moveFace["BR"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["D"]
        self.moveFace["D"] = self.adjmat[self.adjmat.index(moveFace["F"]) + 1]

    def xPrime(self):
        self.moveFace["BR"] = self.moveFace["D"]
        self.moveFace["D"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["U"]
        self.moveFace["U"] = self.adjmat[self.adjmat.index(moveFace["F"]) + 1]

    def y(self):
        self.moveFace["L"] = self.moveFace["F"]
        self.moveFace["F"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["BR"]
        self.moveFace["BR"] = self.moveFace["BL"]
        self.moveFace["BL"] = self.adjmat[self.adjmat.index(moveFace["BR"] + 1)]

    def yPrime(self):
        self.moveFace["L"] = self.moveFace["BL"]
        self.moveFace["BL"] = self.moveFace["BR"]
        self.moveFace["BR"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["F"]
        self.moveFace["F"] = self.adjmat[self.adjmat.index(moveFace["R"] + 1)]

    def z(self):
        self.moveFace["DL"] = self.moveFace["DR"]
        self.moveFace["DR"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["L"]
        self.moveFace["L"] = self.adjmat[self.adjmat.index(moveFace["U"] + 1)]

    def zPrime(self):
        self.moveFace["DL"] = self.moveFace["L"]
        self.moveFace["L"] = self.moveFace["U"]
        self.moveFace["U"] = self.moveFace["R"]
        self.moveFace["R"] = self.moveFace["DR"]
        self.moveFace["DR"] = self.adjmat[self.adjmat.index(moveFace["R"] + 1)]

class Tetrahedron(Triangle):
    def __init__(self, size):
        super().__init__(size = size, order= 3,
                         points = ((1,1,1),
                                   (1,-1,-1),
                                   (-1,1,-1),
                                   (-1,-1,1)),
                         adjmat = ((1,2,3),  # 0
                                    (0,3,2),  # 1
                                    (0,1,3),  # 2
                                    (0,2,1)), # 3
                         moveFace = {'U':0,
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
                         adjmat = ((1,2,3,4),   # 0
                                    (2,0,4,5),   # 1
                                    (3,0,1,5),   # 2
                                    (4,0,2,5),   # 3
                                    (1,0,3,5),   # 4
                                    (1,4,3,2)),  # 5
                         moveFace = {'U':0,
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
                         adjmat = ((1,2,3),  # 0
                                    (0,4,6),  # 1
                                    (0,6,5),  # 2
                                    (0,5,4),  # 3
                                    (3,7,1),  # 4
                                    (3,2,7),  # 5
                                    (2,1,7),  # 6
                                    (4,5,6)), # 7
                         moveFace = {})

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
                         adjmat = ((1,2,3,4,5),   # 0
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
                         moveFace = {'U':0,
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
                         adjmat = ((1,3,18),   # 0
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
                         moveFace = {})
