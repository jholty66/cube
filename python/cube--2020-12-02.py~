#!/usr/bin/python3

solidFaces = {
    # 'name': number of faces
    't': 4,
    'c': 6,
    'o': 8,
    'd': 12,
}

solidAdjFaces = {
    # 'name': number of adjacent faces for any given face
    't': 3,
    'c': 4,
    'o': 3,
    'd': 5,
}

def printm(matrix):
    print()
    for i in range(len(matrix)):
        print(i,matrix[i])

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

def createFaces(s):
    faces = []
    for i in range(solidFaces[s]):
        faces.append([])
    identity = list(range(1,solidAdjFaces[s]+1))
    faces[0].append(identity)
    for i in range(1,int(solidFaces[s]/2)):
        adjFaces = []
        for j in identity:
            adjFaces = [identity[i-1]] + [identity[i+1]] +

    return faces

print(createFaces('c'))
print(createFaces('d'))
