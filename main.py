import alg;from solid import *; import solver
s=Cube(3)
def diff(s1,s2):return ''.join(c for c in s1 if c not in s2)
M=[random.choice('URFBDL')+random.choice(['','2'])+random.choice("' ")]
for i in range(49):M.append(random.choice(diff('URFBDL',M[i-1][0]))+random.choice(['','2'])+random.choice("' "))
A=' '.join(M);print(A)
print(s.solved())
