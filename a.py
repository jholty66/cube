import re

class M:
    def __init__(self,m):
        if re.search(r'X|Y|Z',m):m.T=='rotation';m.depth=None
        elif m[0] in '1234567890':self.depth=int(m[0]);self.T='face' if 'w' in m else 'slice'
        else:self.T='face';self.depth=1
        self.p=True if "'" in m else False
        self.n=re.sub(r'[0-9]|w|\'','',m)
        self.c=int(m[-1]) if m[-1] in '1234567890' else 1
    
    def __str__(self):
        depth=str(self.depth) if self.depth > 1 else ''
        T='w' if self.T =='w' else ''
        c=str(self.c) if self.c > 1 else ''
        p="'" if self.p else ''
        return depth + self.n + T + c + p
   
    def inverse(self):self.p=not self.p
   
    def mirror(self):
        if 'L' in self.n:self.n=self.n.replace('L','R')
        elif 'R' in self.n:self.n=self.n.replace('R','L')
        self.p=not self.p

def expand(alg):
    expand=[];split=re.split(r'(\(.*\)[0-9]?)', alg)#Split on brackets.
    for x in split:
        if re.search(r'\(|\)',x):
            if x[-1] in '1234567890':x=(x[:-1]+' ')*int(x[-1])
            x=re.sub(r'\(|\)','',x)
        expand.append(x)
    return re.sub(r'\s+',' ',(' ').join(expand).strip())

class A:
    def __init__(self,a):self.m=[M(m) for m in re.split(r'\s+'.expand(a))]
    def __str__(self):return ' '.join(m.__str__() for m in s.m)
    def reverse(self):self.m.reverse()
    def inverse(self):(m.reverse() for m in self.m)
    def mirror(self):(m.mirror for m in self.m)
   
    def length(self,T):
        sum=0
        for m in Alg(alg):
            if m.n in 'MSE':sum+=1 if T=='STM' else 2 if T=='HTM' else 2*m.c
            else:sum+=1 if T!='QTM' else m.c
        return sum

def reverse(a):return A(a).reverse().__str__()
def inverse(a):return A(a).inverse().__str__()
def mirror(a):return A(a).mirror().__str__()
