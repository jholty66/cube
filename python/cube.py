#!/usr/bin/python3

class Shape:
    def __init__(self,faces,sides):
        self.faces = faces
        self.sides = sides
        self.faceList = list(range(faces))

def makeNet():
    # List of lists.
    # The parent list has an arbitrary amount of sublists.
    # Each sublist represents a point where at least two faces
    # meet.
    # The items in the sublist are the faces that meet at that
    # point.
    # Each face is denoted by a number.
    # The length of each list is has to be either 2 or 3.

    # Net can start with two faces, all points of each face have to be
    # labelled.  Only two points will share two faces initially.


    # Test for a cube:
    net = [
        [0,1],                  # 0
        [0,1,2],                # 1
        [0,2],                  # 2
        [0],                    # 3
        [1],                    # 4
        [1],                    # 5
        [2],                    # 6
        [2],                    # 7
    ]
    faces = 6

tetrahedron = Shape(4,3)
cube = Shape(6,4)
octahedron = Shape(8,3)
dodecahedron = Shape(12,5)
icosahedron = Shape(20,3)

# shapeFaces = {
#     # 'name': number of faces
#     't': 4,
#     'c': 6,
#     'o': 8,
#     'd': 12,
# }

# shapeAdjFaces = {
#     # 'name': number of adjacent faces for any given face
#     't': 3,
#     'c': 4,
#     'o': 3,
#     'd': 5,
# }

# For a cube:
# IDENTITY [0 1 2 3 4]
# [1,2,4,5] # 0
# [0,2,3,5] # 1
# [0,1,3,4] # 2
# [1,2,4,5] # 3
# [0,2,3,5] # 4
# [0,1,3,4] # 5

# For a dodecahedron
# IDENTITY [0 1 2 3 4 5]
# 0 [1 2 3 4  5]
# 1 [0 2 5 9  10]
# 2 [0 1 3 10 11]
# 3 [0 2 4 7  11]
# 4 [0 3 5 7  8]
# 5 [0 1 4 8  9]
# 6 [7 8 9 10 11]
# 7 [3 4 6 8 11]

# def createFaces(s):
#     faces = []
#     for i in range(shapeFaces[s]):
#         faces.append([])
#     identity = list(range(1,shapeAdjFaces[s]+1))
#     faces[0].append(identity)
#     for i in range(1,int(shapeFaces[s]/2)):
#         adjFaces = []
#         for j in identity:
#             adjFaces = [identity[i-1]] + [identity[i+1]] +

#     return faces

# print(createFaces('c'))
# print(createFaces('d'))
