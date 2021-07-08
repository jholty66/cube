from d import *

for f in RL(ff):
 for n in R(1,fl):
  vm=[[[k:=fv[f][fv[f].index(i)-n],vf[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(vf)]
  exec(f"{'ULFBRD'[f]}{n}=lambda c:[[c[i][j] for i,j in r] for r in {vm}]")
