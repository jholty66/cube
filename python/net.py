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

def makeNet(shape: Shape):
    face1: list[int] = list(range(shape.sides))
    edges: list[set[int]] = [{face1[i - 1], face1[i + 1]} for i in range(shape.sides)]
    pass

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

# print(makeNet(dodecahedron))

NET(dodecahedron)