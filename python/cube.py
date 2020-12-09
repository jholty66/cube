#!/usr/bin/python3

class Piece:
    faces: set[int]

    def __init__(*positions: tuple[int, int]):
        pass

    def getFaces():
        pass

class Center(Piece):
    pass

class Edge(Piece):
    pass

class Corner(Piece):
    pass

class Shape:
    def __init__(self,faces,sides,facesAtPoint):
        self.faces = faces
        self.sides = sides
        self.facesAtPoint = facesAtPoint
        self.faceList = list(range(faces))

tetrahedron  = Shape(4,3,3)
cube         = Shape(6,4,3)
octahedron   = Shape(8,3,4)
dodecahedron = Shape(12,5,3)
icosahedron  = Shape(20,3,5)

# Pretty sure that this code workds, will test it later.
def makeNet(shape: Shape) -> tuple[list[list[int]], list[set[int]]]:
    '''New faces that are added to net can't have points or share pairs of
points that are in the previous two lists.  Adjacent points in the list
are adjacent on the face.  Return the net and it pairs of of points that
share two faces .

When adding a new face, look for two adjacend points are not in
fullPairs.  Add points n+1 and n+2 to the face and poitns where n is the
nth point in points.  Repeat until all faces have been created.'''
    net = [list(range(shape.sides))]  # The net is initially points that surround that first face.
    points = list(range(shape.sides)) # List of points that are used by any of the faces.
    fullPoints = []                   # List of all points that are used by 3 faces.
    pairs = []                        # List of sets of 2 points used by 2 faces.

    def findFullPoints(net: list[list[int]]) -> list[int]:
        '''Take the points in each face in the net. Return a set of all of those
points.'''
        points = [point for shape in net for point in shape]
        return set(point for point in points if points.count(point) == shape.facesAtPoint)

    for face in net:
        if len(net) == shape.faces:
            return net, pairs
        else:
            for i in range(shape.sides):
                p1 = face[i - 1]
                p2 = face[i]
                if {p1, p2} not in pairs and p1 not in fullPoints and p2 not in fullPoints:
                    newFace = [p1, p2]
                    pairs.append(set(newFace))
                    # Create remaining points around newFAce.
                    for j in range(shape.sides - 2):
                        newPoint = len(points)
                        points.append(newPoint)
                        newFace.append(newPoint)
                    net.append(newFace)
                    fullPoints = findFullPoints(net)

# Assuming that makeNet works:
def formatNet(net: list[list[int]]) -> list[set[int, int]]:
    '''Take net as input, return a list contining adjacent faces.'''
    pass

def findAdjFaces(pars: list[set[int, int]]) -> list[list[int]]:
    '''Take a list of faces that are adjacent to each other, the same face
can appear more than once in the list.  Return a new list of lists where
its index is a face and the contents are the faces that are adjacent to
the face.'''
    pass

print('tetrahedron', makeNet(tetrahedron))
print()
print('cube', makeNet(cube))
print()
print('octahedron', makeNet(octahedron))
print()
