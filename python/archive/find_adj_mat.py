# Convert an adjacency matrix of vericies to an adjacency matrix of
# faces.

tetrahedron = [[0,1,1,1],
               [1,0,1,1],
               [1,1,0,1],
               [1,1,1,0]]

cube = [[0,1,1,0,1,0,0,0],
        [1,0,0,1,0,1,0,0],
        [1,0,0,1,0,0,1,0],
        [0,1,1,0,0,0,0,1],
        [1,0,0,0,0,1,1,0],
        [0,1,0,0,1,0,0,1],
        [0,0,1,0,1,0,0,1],
        [0,0,0,1,0,1,1,0]]

ocathedron = [[0,1,1,1,1,0],
              [1,0,1,1,0,1],
              [1,1,0,0,1,1],
              [1,1,0,0,1,1],
              [1,0,1,1,0,1],
              [0,1,1,1,1,0]]

dodecahedron =[[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
               [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
               [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
               [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
               [0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
               [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
               [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
               [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
               [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
               [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0],
               [0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0]];

icosahedron = [[0,1,0,0,1,0,1,1,0,0,1,0],
               [1,0,0,0,1,1,0,1,0,1,0,0],
               [0,0,0,1,0,0,1,0,1,0,1,1],
               [0,0,1,0,0,0,1,1,0,1,0,1],
               [1,1,0,0,0,1,0,0,1,0,1,0],
               [0,1,0,0,1,0,0,0,1,1,0,1],
               [1,0,1,1,0,0,0,1,0,0,1,0],
               [1,1,0,1,0,0,1,0,0,1,0,0],
               [0,0,1,0,1,1,0,0,0,0,1,1],
               [0,1,0,1,0,1,0,1,0,0,0,1],
               [1,0,1,0,1,0,1,0,1,0,0,0],
               [0,0,1,1,0,1,0,0,1,1,0,0]]

def findAdjVertices(vertice, G):
    return [i for i, v in enumerate(G[vertice]) if v == 1]

def find3Net(G):
    faces = []
    for v in range(len(G)):
        for a in findAdjVertices(v, G):
            for b in findAdjVertices(a, G):
                for c in findAdjVertices(b, G):
                    new_face = [a, b, c]
                    if c == v and set(new_face) not in [set(face) for face in faces]:
                        faces.append(new_face)
    return faces

def find4Net(G):
    faces = []
    for v in range(len(G)):
        for a in findAdjVertices(v, G):
            for b in findAdjVertices(a, G):
                for c in findAdjVertices(b, G):
                    for d in findAdjVertices(c, G):
                        new_face = [a, b, c, d]
                        if d == v and set(new_face) not in [set(face) for face in faces]:
                            faces.append(new_face)
    return faces

def find5Net(G):
    faces = []
    for v in range(len(G)):
        for a in findAdjVertices(v, G):
            for b in findAdjVertices(a, G):
                for c in findAdjVertices(b, G):
                    for d in findAdjVertices(c, G):
                        for e in findAdjVertices(d, G):
                            new_face = [a, b, c, d, e]
                            if e == v and set(new_face) not in [set(face) for face in faces]:
                                faces.append(new_face)
    return faces

t = find3Net(tetrahedron)
c = find4Net(cube)
o = find3Net(ocathedron)
d = find5Net(dodecahedron)
i = find3Net(icosahedron)


def findAdjFace(net):
    adjMat = [[] for _ in range(len(net))]
    graph = [[set([face[i - 1], face[i]]) for i in range(len(face))] for face in net]
    for row in graph:
        print(row)
    print()
    for i in range(len(graph)):
        for edge in graph[i]:
            for j in range(len(graph)):
                if edge in graph[j] and j != i:
                    adjMat[i].append(j)
    for row in adjMat:
        print(row)
    return(adjMat)

findAdjFace(d)
