exec(open('a.py').read());exec(open('d.py').read())

faces='ULFBRD'
for f in RL(ff):
 for n in R(1,fl):
  vm=[[[k:=fv[f][fv[f].index(i)-n],vf[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(vf)]
  em=[[[k:=fe[f][fe[f].index(i)-n],ef[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(ef)]
  exec(f"{faces[f]}{n}=lambda c,e:([[c[i][j] for i,j in r] for r in {vm}],[[e[i][j] for i,j in r] for r in {em}])")
