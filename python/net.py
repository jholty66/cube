#!/usr/bin/python3

net = [
    [0,1,2,3],
    [0,1,4,5],
    [1,2,6,7],
    [2,3,8,9]
]

# TODO: crate funtion that places all items of a 2D arryin into a new 1D
# arrary.

def makeNet(faces: int, sides: int) -> list[list[int]]:
    '''New faces that are added to net can't have points or share pairs
of points that are in the previous two lists.  Adjacent points in the
list are adjacent on the face.

When adding a new face, look for two adjacend points are not in
fullPairs.  Add points n+1 and n+2 to the face and poitns where n is the
nth point in points.  Repeat until all faces have been created.

    '''
    net = [list(range(sides))]
    points = list(range(sides)) # List of points that are used by any of the faces.
    fullPoints = []             # List of all points that are used by 3 faces.
    pairs = []                  # List of sets of 2 points used by 2 faces.
    # freeFaces = []  # List of faces that don't have another face attatched to each of its sides.

    def findFullPoints(net: list[list[int]]) -> list[int]:
        points = [point for shape in net for point in shape]
        return set(point for point in points if points.count(point) == 3)

    while len(net) < faces:
        # print(0)
        for face in net:
            # print(1)
            for i in range(len(face)):
                # print(2)
                p1 = face[i-1]
                p2 = face[i]
                if {p1, p2} not in pairs and p1 not in fullPoints and p2 not in fullPoints:
                    # print(3)
                    # Found valid pair of points.
                    face = [p1,p2]
                    pairs.append(set(face))
                    for j in range(sides-2):
                        # Two time for a cube.
                        points.append(points[-1]+1)
                        face.append(points[-1])
                    net.append(face)
                    fullPoints = findFullPoints(net)
        print(len(net),faces)

    return net

# Cube:
print(makeNet(6,4))
