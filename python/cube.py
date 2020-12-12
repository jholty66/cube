#!/usr/bin/python3

print('----------------------------------------------------------------')

class Shape:
    def __init__(self,faces,sides,facesAtPoint):
        self.faces = faces
        self.sides = sides
        self.facesAtPoint = facesAtPoint
        self.faceList = list(range(faces))
        self.colourScheme: list[str]

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
    face = list(range(shape.sides))
    net = [face]                                   # Net initially contains the first face.
    points = list(range(shape.sides))
    pairs = [{face[i], face[i - 1]} for i in face] # Pairs of vertices joined by an edge.
    fullPairs = []                                 # Pairs of vertices shared by two shapes.
    fullPoints = []                                # Vetices that are connected to FACESATPOINT other points or faces.

    def findFullPoints(net: list[list[int]]) -> list[int]:
        '''Take the points in each face in the net. Return a set of all of those
points.'''
        points = [point for shape in net for point in shape]
        connections = [point for pair in pairs for point in pairs]
        return set(point for point in points if points.count(point) == shape.facesAtPoint or connections.count(point) == shape.facesAtPoint)

    for face in net:
        if len(net) == shape.faces:
            print(pairs)
            print()
            return net #, pairs
        else:
            for i in range(shape.sides):
                p1 = face[i - 1]
                p2 = face[i]
                if {p1, p2} not in fullPairs and p1 not in fullPoints and p2 not in fullPoints:
                    fullPairs.append({p1, p2})
                    newPoints = [len(points) + j for j in range(shape.sides - 2)]
                    points += newPoints
                    newFace = [p1, p2] + newPoints
                    for j in range(len(newFace)):
                        pair = {newFace[j - 1], newFace[j]}
                        if pair not in pairs:
                            pairs.append(pair)
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

print(makeNet(dodecahedron))
