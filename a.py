import re
class __Move:
    def __init__(self, move):
        if move[0] in '1234567890':self.depth=int(move[0]);self.type='wide' if 'w' in move else 'slice'
        else:self.type='face';self.depth=1
        self.prime=True if "'" in move else False
        self.name=re.sub(r'[0-9]|w|\'','',move)
        self.count=int(move[-1]) if move[-1] in '1234567890' else 1
    def show(self): print(self.depth,self.name,self.type,self.count,self.prime)
    def inverse(self):self.prime=not self.prime
    def __str__(self):return str(self.depth)+name+type+str(count)+"'" if self.prime else ""
class __Alg:
    def __init__(self, alg):
        self.moves = [__Move(move) for move in re.split(r'\w+',expand_bracket(alg))]
    def format(self):return [__Move.form(move) for move in re.split(r'\s+',alg)]
    def reverse(self):self.moves.reverse()
    def inverse(self):
        for move in self.moves:move.inverse()
    def to_string(self):return (' ').join(move.to_string for move in self.moves)
def expand_bracket(alg):
    expand=[];split=re.split(r'(\(.*\)[0-9]?)', alg)#Split on brackets.
    for x in split:
        if re.match(r'\(|\)',x):
            if x[-1] in '1234567890':x=(x[:-1]+' ')*int(x[-1])
            x=re.sub(r'\(|\)','',x)
        expand.append(x)
    return re.sub(r'\s+',' ',(' ').join(expand).strip())
def inverse(alg):return __Alg(alg).inverse().to_string()
def reverse(alg):return re.split(r'(\(|\)[0-9]?',alg).reverse().replace('(',')').replace(')','(')
def mirror(alg):
    def mirror_move(move):
        if move.name=='L':move.name=='R'
        elif move.name=='R'move.name=='L'
        move.prime=not move.prime
        return move.__str__()
    return (' ').join(mirror_mive(move) for move in __Alg(alg))
def count_moves(alg):
    assert type in ['QTM','HTM','STM']
    sum=0
    for move in __Alg(alg):
        if move.name in 'MSE':sum+=1 if type=='STM' else 2 if type=='HTM' else 2*move.count
        else:sum+=1 if type!='QTM' else move.count
    return sum