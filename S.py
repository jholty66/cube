import math
from functools import reduce

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

De=set((i,j) for i,v in enumerate(Dv[:-3]) for j,V in enumerate(Dv[i+1:]) if El(v,V)<r+δ)

Dfe=[]
def ff(f=[]):
    for e in De:
        if not f:
            f=[e]
        else:
            if any(v in f[-1] for v in e):
                if len(f)==5:
                    if f[0]==e and all(len(set(f)&F)<=1 for F in Dfe) and all([ee for F in Dfe for ee in F].count(E) <= 2 for E in f):
                        Dfe.append(set(f));f=[]
                elif e not in f:
                    ff(f+[e])
ff()
print(Dfe)
#Dfv=[set(v for e in f for v in e[1]) for v in Dfe];print(Dfv)
#DM=[[Dfe.index(F) for e in f for F in Dfe if e in F and F!=f] for f in Dfe]
