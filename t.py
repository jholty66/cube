exec(open('a.py').read());exec(open('d.py').read())

faces='ULFBRD'
moves={}
for f in RL(ff):
 for n in R(1,fl):
  vm=[[[k:=fv[f][fv[f].index(i)-n],vf[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(vf)]
  em=[[[k:=fe[f][fe[f].index(i)-n],ef[k].index(s if s==f else ff[f][ff[f].index(s)-n])] if f in c else [i,j] for j,s in E(c)] for i,c in E(ef)]
  exec(f"{faces[f]}{n}=lambda c,e:([[c[i][j] for i,j in r] for r in {vm}],[[e[i][j] for i,j in r] for r in {em}])")
  move=f"{faces[f]}{n}";moves[eval(move)]=move

# cube only
o=[[faces.index(f) for f in x] for x in 'UD LR FB FB LR UD'.split()]
G1=lambda VF,EF:all(EF[i][j] in ((0,2,3,5) if ef[i][j] in (0,5) else (2,3,4,1) if ef[i][j] in (1,4) else (0,1,2,3,4,5)) for i in RL(EF) for j in R(2))
G2=lambda VF,EF:all(VF[i][j] in o[vf[i][j]] for i in RL(vf) for j in R(3) if vf[i][j] in (0,5)) 
G3=lambda VF,EF:all(VF[i][j] in o[vf[i][j]] for i in RL(vf) for j in R(3)) and all(EF[i][j] in o[ef[i][j]] for i in RL(ef) for j in R(2))
