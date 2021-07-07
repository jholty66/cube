Tree:
alias.py      function aliases
alg.py        algorithm library
definition.py puzzle data
index.py      index implementation
vector.py     vector implementation

Notes:
- cube as vector data structure, each element as sticker
- moves are vectors of indices stating how to reorder the stickers
- each face turn will rotate the stickers on a given slice and then reorder the
  stickers adjacent to that face
- rotation will be calculated by code so that they satisfy equations
  (X U = F X) 
- this can then be generalized to any regular polyedron of any size, minor
  changes for cuboids
- vector data structure and moves will then be translated to a list of cubies,
  where each cubie is a tuple of the faces that lie on it as this is more
  useful for pattern databases 

Current features:

Future features:
Turnable Rubik's cube
Implementation of Thistlewaite's algorithm
Vector implementation of puzzles, (list of stickers) 
Implementation of Kociemba's algorithm
Implementation of korf's algorithm
Support larger cubes
Support higher dimension cubes
Support regular polydra
Support n-polytopes
Support cuboids
OpenGL puzzle visualization
