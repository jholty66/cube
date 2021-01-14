import re
class Move:
    def __init__(self, move):
        print('move',move)
        if re.search(r'X|Y|Z',move):move.type=='rotation';move.depth=None
        elif move[0] in '1234567890':self.depth=int(move[0]);self.type='face' if 'w' in move else 'slice'
        else:self.type='face';self.depth=1
        self.prime=True if "'" in move else False
        self.name=re.sub(r'[0-9]|w|\'','',move)
        self.count=int(move[-1]) if move[-1] in '1234567890' else 1

    def __str__(self):
        depth=str(self.depth) if self.depth > 1 else ''
        type='w' if self.type =='w' else ''
        count=str(self.count) if self.count > 1 else ''
        prime="'" if self.prime else ''
        return depth + self.name + type + count + prime

    def inverse(self):self.prime=not self.prime

    def mirror(self):
        if 'L' in self.name:self.name=self.name.replace('L','R')
        elif 'R' in self.name:self.name=self.name.replace('R','L')
        self.prime=not self.prime

def expand(alg):
    expand=[];split=re.split(r'(\(.*\)[0-9]?)', alg)#Split on brackets.
    for x in split:
        if re.search(r'\(|\)',x):
            if x[-1] in '1234567890':x=(x[:-1]+' ')*int(x[-1])
            x=re.sub(r'\(|\)','',x)
        expand.append(x)
    return re.sub(r'\s+',' ',(' ').join(expand).strip())

def create(alg): return [Move(move) for move in re.split(r'\s+',expand(alg))]

def inverse(alg): return (' ').join(move.inverse().__str__() for move in create(alg))

def reverse(alg): return (' ').join(expand(alg).split(' ').reverse())

def mirror(alg): return (' ').join(move.mirror.__str__ for move in create(alg))

def count_moves(alg):
    assert type in ['QTM','HTM','STM']
    sum=0
    for move in Alg(alg):
        if move.name in 'MSE':sum+=1 if type=='STM' else 2 if type=='HTM' else 2*move.count
        else:sum+=1 if type!='QTM' else move.count
    return sum