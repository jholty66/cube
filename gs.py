import math

δ=0.01
φ=(1+math.sqrt(5))/2

class T:v=((-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1));s=3
class H:v=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1));s=4
class O:v=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1));s=3
class D:v=((0,φ,1/φ),(0,φ,-1/φ),(0,-φ,1/φ),(0,-φ,-1/φ),(1/φ,0,φ),(1/φ,0,-φ),(-1/φ,0,φ),(-1/φ,0,-φ),(φ,1/φ,0),(φ,-1/φ,0),(-φ,1/φ,0),
           (-φ,-1/φ,0),(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1));s=5
class I:v=((0,1,φ),(0,1,-φ),(0,-1,φ),(0,-1,-φ),(1,φ,0),(1,-φ,0),(-1,φ,0),(-1,-φ,0),(φ,0,1),(φ,0,-1),(-φ,0,1),(-φ,0,-1));s=3

def d(v,V):return math.sqrt(sum((c-C)**2 for c,C in zip(v,V)))

def DFS(f):
    for e in s.ev:
        if f[-1]==e[0]:
            if len(f)==s.s:
                if e[1]==f[0] and all(any(v not in F for v in f) for F in s.fv):s.fv.append(f)
            elif f[-2] not in e:DFS(f+[e[1]])

for S in [T,H,O,D,I]:
    s=S();print(s)

    r=d(s.v[-2],s.v[-1])
    for i,v in enumerate(s.v[:-3]):
        for V in s.v[i+1:]:
            R=d(v,V)
            if R<r:r=R

    s.ev=[(i,j) for i,v in enumerate(s.v) for j,V in enumerate(s.v) if d(v,V)<r+δ and i!=j] # edges undirected

    s.fv=[]
    for e in s.ev:DFS(list(e))

    s.fe=[[(f[i-1],f[i]) for i in range(len(f))] for f in s.fv]

    s.vf=[[i for i,f in enumerate(s.fv) if v in f] for v in range(len(s.v))]

    s.ed=[(i,j) for i,v in enumerate(s.v) for j,V in enumerate(s.v) if d(v,V)<r+δ and i<j] # edges directed
    s.ef=[[i for i,f in enumerate(s.fe) if set(e) in [set(E) for E in f]] for e in s.ed]

    s.m=[[s.fv.index(F) for i in range(len(f)) for F in s.fv if F!=f and f[i-1] in F and f[i] in F] for f in s.fv]
    R=range(s.s);sf=set()
    for i,f in enumerate(s.m):
        for j in R:
            for I,F in enumerate(s.m):
                if I>i:
                    ss=set()
                    if (f[j-1],f[j]) in [(F[J-1],F[J]) for J in R]:
                        if I in sf:
                            f.reverse()
                            for I in ss:s.m[I].reverse()
                        else:F.reverse();ss.add(I)
                    sf|=ss

    for f in s.fv:print(f)
    print()
    for f in s.fe:print(f)
    print()
    for v in s.vf:print(v)
    print()
    for e in s.ef:print(e)
    print(len(s.ef));print()
    for f in s.m:print(f)
    print()
