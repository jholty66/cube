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

De=[(i,j) for i,v in enumerate(Dv) for j,V in enumerate(Dv) if El(v,V)<r+δ and i<j]

Dfe=[]
def DFS(f):
    for e in De:
        if any(v in f[-1] for v in e): # check if new edge share verticie with previous edge
            if len(f)==5:
                if e==f[0] and set(f) not in [set(F) for F in Dfe]:Dfe.append(f)
            elif e not in f:DFS(f+[e])
for e in De:DFS([e])
print(Dfe);print()

Dfv=[[f[i][0] if f[i][0]!=f[i-1][0] else f[i][1] for i,_ in enumerate(f)] for f in Dfe]
for f in Dfv:print(f)
print()

DM=[[Dfe.index(F) for e in f for F in Dfe if e in F and F!=f] for f in Dfe]
for r in DM:print(r)
print()
