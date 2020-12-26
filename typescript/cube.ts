class Solid {
    order: number;
    faces: number;
    sides: number;
    degree: number;
    adjMat: number[][];

    // centers: number[][];
    // edges: number[][];
    // corners: number[][];

    //    makeAdjFaceMat = (sides: number, adjMat: number[][]) => {
    //        // create list of all cycles that contain sides edges, this
    //        // should be equal to the number of faces
    //        //
    //        // look at a cycle, push to adjFacemat all other cycles that
    //        // share two consecutive vertices
    //        let facesP: number[][] = adjMat[0].filter(v => v == 1);

    //    };

    findFace = (G: number[][], i: number, maxDepth: number) => {
/*      start at node 0
        create a list of the indexes of the nodes that are adjacent to it
        (the nodes that are 1 and not 0)


*/
	let helper = (j: number, depth: number) => {
            	visited: number[] = [];
	}
    }

    constructor(order: number, faces: number, sides: number, degree: number, adjMat: number[][]) {
        // degree is the number of faces that meet at a point.
        // order is the number of layers. EG: 3 for a 3x3x3 cube.
        this.order = order;
        this.faces = faces;
        this.sides = sides;
        this.degree = degree;
        this.adjMat = adjMat;

        // this.adjFaceMat = makeAdjFaceMat(adjMat);

        /*this.centers = (() => {
          let centers: number[] = [];
          for (var i = 0; i < faces; i++) { centers.push(i) }
          return centers;
          })

          this.edges = () => {
          let edges: number[] = [];
          for (let i = 0; i < adjFaceMat.length; i++) {
          let edge: number[] = [i, adjFaceMat[i]];m
          if (!edges.includes(edge)) { edges.append(edge) }
          }
          return edges;
          };

          this.corners = (adjFaceMat => {
          let corners: number[][] = [];
          for (let i = 0; i < adjFaceMat.length; i++) {
          let corner: number[] = [i, adjFaceMat[i], adjFaceMat[(i + 1) % sides]];
          if (!corners.includes(corner)) { corners.append(corner) }
          }
          return corners;
          });
        */    };
}

class Shape extends Solid {
    findAdjVertices = (v: number): number[] => {
        vertices: number[] = []
        for (let i = 0; i < Solid.adjMat.length; i++) {
            if (Shape.adjMat[i]) {
                vertices.push(i)
            }
        }
        return verticies
    }
}

class Triangle extends Shape {
    findFaces = G => {
        for (var v = 0; v < Solid.adjMat.length; v++) {
            for (let a in Shape.findAdjVertices(v)) {
                for (let b in Shape.findAdjVertices(a)) {
                    for (let c in Shape.findAdjVertices(b)) {
                        let newFace: number[] = [a,b,c];
                        if (c == v && newFace.sort()) {

                        }
                    }
                }
            }
        }
    }
}

class Square extends Shape {

}

class Pentagon extends Shape {

}

class Tetrahedron extends Solid {
    constructor(order: number) {
        super(
            order, 4, 3, 3,
            [[1,2,3], // 0
             [0,3,2], // 1
             [0,1,2], // 2
             [0,2,1]] // 3
        );
    }
}

class Cube extends Solid {
    constructor(order: number) {
        super(
            order, 6, 4, 3,
            [[1,2,3,4], // 0
             [0,4,5,2], // 1
             [0,1,5,3], // 2
             [0,2,5,4], // 3
             [0,3,5,1], // 4
             [1,2,3,4]] // 5

        );
    }

    // Colour scheme:
    // 0: White
    // 1: Green
    // 2: Red
    // 3: Blue
    // 4: Orange
    // 5: Yellow
}

class Octahedron extends Solid {
    constructor(order :number) {
        super(order, 8, 3, 4,
              [[]]);
    }
}

class Dodecahedron extends Solid {
    constructor(order: number) {
        super(
            order, 12, 5, 3,
            [[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
             [0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0]]

        );
    }
}

class Icosehedron extends Solid {
    constructor(order: number) {
        super(order, 20, 3, 5,
              [[0,1,0,0,1,0,1,1,0,0,1,0],
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
             );
    }
}

const d2 = new Dodecahedron(2);
console.log(d2.adjList)
console.log(d2.order)

// const xx = new Solid(3,4,3,3);
// console.log(xx.order)
