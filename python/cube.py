#!/usr/bin/python3

platonicSolids = {
    # 'name': number of faces
    'tetrahedron': 4,
    'cube': 6,
    'octahedron': 8,
    'dodecahedron': 12,
    'icosahedron': 20,
}

# For a cube:
# [1,2,4,5] # 0
# [0,2,3,5] # 1
# [0,1,3,4] # 2
# [1,2,4,5] # 3
# [0,2,3,5] # 4
# [0,1,3,4] # 5

def createFaces(n):
    faces = []
    for i in range(n):
        for j in range(n):
            adjFaces = []
            print(i,j,i+j,3%(3+i+j))
            if (i+j) % 3 == 0:
                adjFaces.append((i+j) % 6)
        faces.append(adjFaces)
    return faces
