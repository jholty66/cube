#!/usr/bin/env python3.9

class Solid:
    def __init__(self, order: int, faces: int, adjMat: list[list[int]]):
        self.order = order
        self.faces = faces
        self.sides = sides
        self.adjMat = adjMat

class Shape(Solid):
    def __init__(self, sides: int):
        self.sides = sides

    def findAdjVertices(self, vertice: int) -> list[int]:
        return [i for i, v in enumerate(Solid.adjMat[vertice]) if v == 1]

class Triangle(Shape):
    def __init__(self):
        Shape.__init__(sides = 3)

    def findFaces(self, adjMat: list[list[int]]) -> list[list[int]]:
        faces: list[list[int]] = []
        for v0 in range(len(adjMat)):
            for v1 in Shape.findAdjVertices(v0):
                for v2 in Shape.findAdjVertices(v1):
                    for v3 in Shape.findAdjVertices(v2):
                        newFace = [v1, v2, v3]
                        if v0 == v3 and set(newFace) not in [set(face) for face in faces]:
                            faces.append(newFace)
        return faces

class Square(Shape):
    def __init__(self):
        Shape.__init__(sides = 4)

    def findFaces(self, adjMat: list[list[int]]) -> list[list[int]]:
        faces: list[list[int]] = []
        for v0 in range(len(adjMat)):
            for v1 in Shape.findAdjVertices(v0):
                for v2 in Shape.findAdjVertices(v1):
                    for v3 in Shape.findAdjVertices(v2):
                        for v4 in Shape.findAdjVertices(v3):
                            newFace = [v1, v2, v3, v4]
                            if v4 == v0 and set(newFace) not in [set(face) for face in faces]:
                                faces.append(newFace)
        return faces

class Dodecahedron(Shape):
    def __init__(self):
        Shape.__init__(sides = 5)

    def findFaces(self, adjMat: list[list[int]]) -> list[list[int]]:
        faces: list[list[int]] = []
        for v0 in range(len(adjMat)):
            for v1 in Shape.findAdjVertices(v0):
                for v2 in Shape.findAdjVertices(v1):
                    for v3 in Shape.findAdjVertices(v2):
                        for v4 in Shape.findAdjVertices(v3):
                            for v5 in Shape.findAdjVertices(v4):
                                newFace = [v1, v2, v3, v4, v5]
                                if v5 == v0 and set(newFace) not in [set(face) for face in faces]:
                                    faces.append(newFace)
        return faces

class Tetrahedron(Solid, Triangle):
    def __init__(self, order: int):
        Solid.__init__(order = order,
                       faces = 4,
                       adjMat = [[]])
        Triangle.__init__()

class Cube(Solid, Square):
    def __init__(self, order: int):
        Solid.__init__(order = order,
                       faces = 6,
                       adjmat = [[]])
        Square.__init__()

class Octahedron(Solid, Triangle):
    def __init__(self, order: int):
        Solid.__init__(order = order,
                       faces = 8,
                       adjMat = [[]])
        Triangle.__init__()

class Dodecahedron(Solid, Dodecahedron):
    def __init__(self, order: int):
        Solid.__init__(order = order,
                       faces = 12,
                       adjMat= [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
        Dodecahedron.__init__()

class Tetrahedron(Solid, Triangle):
    def __init__(self, order: int):
        Solid.__init__(order = order,
                                          faces = 4,
                                          adjMat = [[0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
                                                    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
                                                    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
                                                    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                                                    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                                                    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
                                                    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                                                    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                                                    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                                                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                                                    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                                                    [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0]])
        Triangle.__init__()

d3 = Dodecahedron(3)
