import math
import pygame;from pygame.locals import *
from OpenGL.GL import *;from OpenGL.GLU import *

φ=(1+math.sqrt(5))/2

class T:
    s=3
    v=((-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1))
    e=((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    f=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
    m=((2,1,3),(3,0,2),(1,0,3),(2,0,1))

class H:
    s=4
    v=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1))
    e=((0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7))
    f=((0,1,3,2),(0,1,5,4),(0,2,6,4),(1,3,7,5),(2,3,7,6),(4,5,7,6))
    m=((2,1,3,4),(2,0,3,5),(1,0,4,5),(5,4,0,1),(5,3,0,2),(4,3,1,2))

class O:
    s=3
    v=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    e=((0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5))
    f=((0,2,4),(0,2,5),(0,3,4),(0,3,5),(1,2,4),(1,2,5),(1,3,4),(1,3,5))
    m=((2,1,4),(3,0,5),(0,3,6),(1,2,7),(6,5,0),(7,4,1),(4,7,2),(5,6,3))

class D:
    s=5
    v=((0,φ,1/φ),(0,φ,-1/φ),(0,-φ,1/φ),(0,-φ,-1/φ),(1/φ,0,φ),(1/φ,0,-φ),(-1/φ,0,φ),(-1/φ,0,-φ),(φ,1/φ,0),(φ,-1/φ,0),
       (-φ,1/φ,0),(-φ,-1/φ,0),(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1))
    e=((0,1),(0,12),(0,16),(1,13),(1,17),(2,3),(2,14),(2,18),(3,15),(3,19),(4,6),(4,12),(4,14),(5,7),(5,13),(5,15),
       (6,16),(6,18),(7,17),(7,19),(8,9),(8,12),(8,13),(9,14),(9,15),(10,11),(10,16),(10,17),(11,18),(11,19))
    f=((0,1,13,8,12),(0,1,17,10,16),(0,12,4,6,16),(1,13,5,7,17),(2,3,15,9,14),(2,3,19,11,18),(2,14,4,6,18),
       (3,15,5,7,19),(4,12,8,9,14),(5,13,8,9,15),(6,16,10,11,18),(7,17,10,11,19))
    m=((2,1,3,9,8),(10,11,3,0,2),(1,0,8,6,10),(11,7,9,0,1),(8,9,7,5,6),(6,4,7,11,10),(10,2,8,4,5),(5,4,9,3,11),
       (6,2,0,9,4),(4,8,0,3,7),(5,11,1,2,6),(7,3,1,10,5))

class I:
    s=3
    v=((0,1,φ),(0,1,-φ),(0,-1,φ),(0,-1,-φ),(1,φ,0),(1,-φ,0),(-1,φ,0),(-1,-φ,0),(φ,0,1),(φ,0,-1),(-φ,0,1),
       (-φ,0,-1))
    e=((0,2),(0,4),(0,6),(0,8),(0,10),(1,3),(1,4),(1,6),(1,9),(1,11),(2,5),(2,7),(2,8),(2,10),(3,5),(3,7),(3,9),(3,11),
       (4,6),(4,8),(4,9),(5,7),(5,8),(5,9),(6,10),(6,11),(7,10),(7,11),(8,9),(10,11))
    f=((0,2,8),(0,2,10),(0,4,6),(0,4,8),(0,6,10),(1,3,9),(1,3,11),(1,4,6),(1,4,9),(1,6,11),(2,5,7),(2,5,8),(2,7,10),
       (3,5,7),(3,5,9),(3,7,11),(4,8,9),(5,8,9),(6,10,11),(7,10,11))
    m=((3,1,11),(4,0,12),(4,3,7),(0,2,16),(1,2,18),(8,6,14),(9,5,15),(9,8,2),(5,7,16),(6,7,18),(12,11,13),(0,10,17),
       (1,10,19),(15,14,10),(5,13,17),(6,13,19),(8,3,17),(14,11,16),(9,4,19),(15,12,18))

if __name__=='__main__':
    i=0;S=[T,H,O,D,I]
    pygame.init();display=(1600,900);pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(30,display[0]/display[1],0.1,50.0);glTranslatef(0.0,0.0,-10);glRotatef(0,0,0,0)
    while True:
        s=S[i%5]()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:pygame.quit();quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:i-=1
                elif event.key==pygame.K_RIGHT:i+=1
        glRotatef(1,1,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glBegin(GL_LINES)
        for e in s.e:
            for v in e:
                glVertex3fv(s.v[v])
        glEnd()
        pygame.display.flip();pygame.time.wait(25)
