import re;from c import *
def expand_bracket(alg):
    expand=[];split=re.split(r'(\(.*\)[0-9])', alg)#Split on brackets.
    for x in split:
        if re.match(r'\(|\)',x):
            if x[-1] in '1234567890':x=(x[:-1]+' ')*int(x[-1])
            x=re.sub(r'\(|\)','',x)
        expand.append(x)
    return re.sub(r'\s+',' ',(' ').join(expand).strip())
def format_move(move):
    if move[0] in '1234567890':depth=int(move[0]);type='wide' if 'w' in move else 'slice'
    else:type='face';depth=1
    prime=True if "'" in move else False
    name=re.sub(r'[0-9]|w|\'','',move)
    count=int(move[-1]) if move[-1] in '1234567890' else 1
    return Move(depth,name,type,count,prime)
def format_alg(alg):return [format_move(move) for move in re.split(r'\s+',alg)]
