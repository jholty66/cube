import c;from c import *
alg = "R U' R' R (R U R' U')2"
p = Cube(3)
m=Move(1,'R',False)
p.alg_face_turn(m)