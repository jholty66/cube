from functools import reduce
readMove=lambda m:eval(m[0]+('1' if not len(m)-1 else '3' if m[1]=="'" else m[1]))
compose=lambda *m:lambda *x:reduce(lambda f,g:g(*f),m,x)
readAlg=lambda a:compose(*map(readMove,a.split()))
