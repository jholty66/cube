import math
import pygame;from pygame.locals import *
from OpenGL.GL import *;from OpenGL.GLU import *

δ=0.01
φ=(1+math.sqrt(5))/2

class T:v=((-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1));s=3
class H:v=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1));s=4
class O:v=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1));s=3
class D:v=((0,φ,1/φ),(0,φ,-1/φ),(0,-φ,1/φ),(0,-φ,-1/φ),(1/φ,0,φ),(1/φ,0,-φ),(-1/φ,0,φ),(-1/φ,0,-φ),(φ,1/φ,0),(φ,-1/φ,0),(-φ,1/φ,0),
           (-φ,-1/φ,0),(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1));s=5
class I:v=((0,1,φ),(0,1,-φ),(0,-1,φ),(0,-1,-φ),(1,φ,0),(1,-φ,0),(-1,φ,0),(-1,-φ,0),(φ,0,1),(φ,0,-1),(-φ,0,1),(-φ,0,-1));s=3
s=I()

def d(v,V):return math.sqrt(sum((c-C)**2 for c,C in zip(v,V)))

r=d(s.v[-2],s.v[-1])
for i,v in enumerate(s.v[:-3]):
    for V in s.v[i+1:]:
        R=d(v,V)
        if R<r:r=R

s.e=[(i,j) for i,v in enumerate(s.v) for j,V in enumerate(s.v) if d(v,V)<r+δ and i!=j]

s.f=[]
def DFS(f):
    for e in s.e:
        if f[-1]==e[0]:
            if len(f)==s.s:
                if e[1]==f[0] and all(any(v not in F for v in f) for F in s.f):s.f.append(f)
            elif f[-2] not in e:DFS(f+[e[1]])
for e in s.e:DFS(list(e))

s.M=[[s.f.index(F) for i in range(len(f)) for F in s.f if F!=f and f[i-1] in F and f[i] in F] for f in s.f]
R=range(s.s);sf=set()
for i,f in enumerate(s.M):
    for j in R:
        for I,F in enumerate(s.M):
            if I>i:
                ss=set()
                if (f[j-1],f[j]) in [(F[J-1],F[J]) for J in R]:
                    if I in sf:
                        f.reverse()
                        for I in ss:s.M[I].reverse()
                    else:F.reverse();ss.add(I)
                sf|=ss

if __name__=='__main__':
    for r in s.f:print(r)
    print()
    for r in s.M:print(r)
    pygame.init();display=(800,600);pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(30,display[0]/display[1],0.1,50.0);glTranslatef(0.0,0.0,-10);glRotatef(0,0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:pygame.quit();quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1,1,1,1)
        glBegin(GL_LINES)
        for e in set(s.e):
            for v in e:
                glVertex3fv(s.v[v])
        glEnd()
        pygame.display.flip();pygame.time.wait(10)
