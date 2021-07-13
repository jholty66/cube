from math import sqrt
E=enumerate;L=len;R=range;RL=lambda x:range(len(x))
φ=(1+sqrt(5))/2;δ=0.01

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
def converge(x,f):y=f(x);return y if x==y else converge(y,f)
def _p(*x):return ' '.join(''.join('ULFBRD'[s] for s in c) for p in x for c in p)
def p(*x):print(_p(*x))

vv=[(x,y,z) for x in (1,-1) for y in (1,-1) for z in (1,-1)];n=len(vv)
dm=[[sqrt(sum((c-C)**2 for c,C in zip(v,V))) for v in vv] for V in vv]
el=min(d for r in dm for d in r if d)
am=[[i for i,x in E(y) if abs(x-el)<δ] for y in dm]
ev=[{i,v} for i in R(n) for v in am[i] if i<v]
fl=bfs(n,am)
fv=[];[dfs([i],fl,am) for i in R(n)] # undirected
fv=converge(fv[:-1]+[fv[-1][::-1]],lambda fv:[f[::-1] if any((f[i-1],f[i])==(F[j-1],F[j]) for i in R(fl) for F in fv[k+1:] for j in R(fl)) else f for k,f in E(fv)]) # hack, passing fv does not work for dodecahedron and icosededron
fe=[[ev.index({f[i-1],f[i]}) for i in R(fl)] for f in fv]
ff=[[fe.index(F) for e in f for F in fe for E in F if f!=F and e==E] for f in fe]
vf=[[i,ff[i][j],ff[i][j-1]] for v in R(n) for i in RL(fv) for j in R(fl) if all(v in fv[k] for k in [i,ff[i][j-1],ff[i][j]])][::3]
ef=[[i for i,f in E(fv) for j in R(fl) if {f[j-1],f[j]}==e] for e in ev]
