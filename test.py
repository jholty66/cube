from solid import *
p = Dodecahedron(3)
alg = "R U R' F' R U R' U' R' F R2 U' R' ";print(alg);print(p.solved())
for _ in range(3):p.exec_alg(alg);print(p.solved())