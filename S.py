import math as math

δ = 0.01
φ = (1+math.sqrt(5))/2

Dv=[[0,φ,1/φ],[0,φ,-1/φ],[0,-φ,1/φ],[0,-φ,-1/φ],[1/φ,0,φ],[1/φ,0,-φ],[-1/φ,0,φ],[-1/φ,0,-φ],[φ,1/φ,0],[φ,-1/φ,0],[-φ,1/φ,0],
    [-φ,-1/φ,0],[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]

def El(v,V):return math.sqrt(sum((c-C)**2 for c,C in zip(v,V)))
def Es(e,E): return true if (e[0]==E[0] and e[1]==E[1]) or (e[0]==E[1] and e[1]==E[0]) else False

r=l(Dv[-2],Dv[-1])
for i,v in enumerate(Dv[:-3]):
    for V in Dv[i+1:]:
        R=El(v,V)
        if R<r:r=R

De=[]
for i,v in enumerate(Dv[:-3]):
    for V in Dv[i+1:]:
        e=El(v,V)
        if e<r+δ:De.append((v,V))

Dfe=[];ce=()
while len(Dfe)<12:
    ie=[e for e in De if e not in ce]
    e=ie.pop();v=e[0];f=[e]
    while len(f)<5:
        for E in ie:
            print(e);print(E)
            if Es(e,E)==False and v in E:
                f.append(E);e=E;ie.remove(E)
                v=E[0] if E[0] != v else E[1]
                break
    es=[e for f in Dfe for e in f]
    ce = set(e for e in es if es.count(e)==2)
