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

# DM=[[0 for _ in range(len(Dv))] for _ in range(len(Dv))]
# for e in De:DM[e[0]][e[1]]=1;DM[e[1]][e[0]]=1
# 
# def nf(f):
#     for x,v in enumerate(DM[f[-1]]):
#         if v:
#             if len(f)==5:
#                 if x==f[0] and set(f) not in [set(F) for F in Df]:Df.append(f)
#             elif x not in f: nf(f+[x])
# for y in range(len(Dv)):nf([y])

Df=[]
def DFS(f):
    for e in De:
        if len(f)==5:
            if f[-1] in e and f[0] in e and set(f) not in [set(F) for F in Df]:Df.append(f)
        elif f[-1] in e and f[-2] not in e:DFS(f+[e[0]] if e[0]!=f[-1] else f+[e[1]])
for e in De:DFS(list(e))

for f in Df:print(f)
