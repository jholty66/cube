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

vv=[(x,y,z) for x in (1,-1) for y in (1,-1) for z in (1,-1)];n=len(vv)
dm=[[sqrt(sum((c-C)**2 for c,C in zip(v,V))) for v in vv] for V in vv]
el=min(d for r in dm for d in r if d)
am=[[i for i,c in E(r) if el==c] for r in dm]
ev=[{i,v} for i in R(n) for v in am[i] if i<v]
fl=bfs(n,am)
fv=[];[dfs([i],fl,am) for i in R(n)] # undirected
vf=[[i for i,f in E(fv) if v in f] for v in R(n)]
ef=[[i for i,f in E(fv) for j in R(fl) if {f[j-1],f[j]}==e] for e in ev]
ff=[[j for i in R(fl) for j,F in E(fv) if F!=f and f[i-1] in F and f[i] in F] for f in fv] # undirected
ff=[f[::-1] if any((f[i-1],f[i])==(F[j-1],F[j]) for F in ff[:k] for i in R(fl) for j in R(fl)) else f for k,f in E(ff)] # directed
fv=[[i for j in R(fl) for i,v in E(vf) if {f[j-1],f[j],k}==set(v)] for k,f in E(ff)] # directed
fe=[[i for j in R(fl) for i,e in E(ef) if {f[j],k}==set(e)] for k,f in E(ff)] # directed

for f in RL(ff):
 for n in R(1,fl):
  vm=[[[k:=fv[f][fv[f].index(i)-n],vf[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(vf)]
  exec(f"{'URFBLD'[f]}{n}=lambda c:[[c[i][j] for i,j in r] for r in {vm}]")

readMove=lambda m:eval(m[0]+('1' if not len(m)-1 else '3' if m[1]=="'" else m[1]))
compose=lambda *m:lambda x:reduce(lambda f,g:g(f),m,x)
