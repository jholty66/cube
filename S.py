import math

δ=0.01
φ=(1+math.sqrt(5))/2

Dv=[[0,φ,1/φ],[0,φ,-1/φ],[0,-φ,1/φ],[0,-φ,-1/φ],[1/φ,0,φ],[1/φ,0,-φ],[-1/φ,0,φ],[-1/φ,0,-φ],[φ,1/φ,0],[φ,-1/φ,0],[-φ,1/φ,0],
    [-φ,-1/φ,0],[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]

def El(v,V):return math.sqrt(sum((c-C)**2 for c,C in zip(v,V)))

r=El(Dv[-2],Dv[-1])
for i,v in enumerate(Dv[:-3]):
    for V in Dv[i+1:]:
        R=El(v,V)
        if R<r:r=R

De=[(i,j) for i,v in enumerate(Dv) for j,V in enumerate(Dv) if El(v,V)<r+δ and i!=j]

Df=[]
def DFS(f):
    for e in De:
        if f[-1]==e[0]:
            if len(f)==5:
                if e[1]==f[0] and all(any(v not in F for v in f) for F in Df):Df.append(f)
            elif f[-2] not in e:DFS(f+[e[1]])
for e in De:DFS(list(e))

DM=[[Df.index(F) for i in range(len(f)) for F in Df if F!=f and f[i-1] in F and f[i] in F] for f in Df]
R=range(5);S=set()
for i,f in enumerate(DM):
    for j in R:
        for I,F in enumerate(DM):
            if I>i:
                s=set()
                if (f[j-1],f[j]) in [(F[J-1],F[J]) for J in R]:
                    if I in S:
                        f.reverse();print('r')
                        for I in s:DM[I].reverse()
                    else:F.reverse();s.add(I)
                S|=s
