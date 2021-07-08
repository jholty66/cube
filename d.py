from functools import reduce
from math import sqrt
E=enumerate;L=len;R=range;RL=lambda x:range(len(x))

def bfs(n,g):
 d=[0]+[n]*(n-1);p=[-1]*n;q=[0]
 while q:
  x=q.pop(0)
  for c in am[x]:
   if d[c]==n:d[c]=1+d[x];p[c]=x;q.append(c)
   elif p[x]!=c and p[c]!=x:return d[x]+d[c]+1

def dfs(p,l,g):
 for v in g[p[-1]]:
  if len(p)==l and v==p[0] and set(p) not in map(set,fv):fv.append(p)
  elif v not in p: dfs(p+[v],l,g) 

def converge(x,f):
    y=f(x)
    return y if x==y else converge(y,f)

vv=[(x,y,z) for x in (1,-1) for y in (1,-1) for z in (1,-1)];n=len(vv)
dm=[[sqrt(sum((c-C)**2 for c,C in zip(v,V))) for v in vv] for V in vv]
el=min(d for r in dm for d in r if d)
am=[[i for i,c in E(r) if el==c] for r in dm]
ev=[{i,v} for i in R(n) for v in am[i] if i<v]
fl=bfs(n,am)
fv=[];[dfs([i],fl,am) for i in R(n)] # undirected
fv=converge(fv,lambda fv:[v[::-1] if any((v[i-1],v[i])==(V[j-1],V[j]) for V in fv[:k] for i in R(fl) for j in R(fl)) else v for k,v in E(fv)])
fe=[[ev.index({f[i-1],f[i]}) for i in R(fl)] for f in fv]
vf=[[i for i,f in E(fv) if v in f] for v in R(n)]
ef=[[i for i,f in E(fv) for j in R(fl) if {f[j-1],f[j]}==e] for e in ev]
ff=[[fe.index(F) for e in f for F in fe for E in F if f!=F and e==E] for f in fe]
