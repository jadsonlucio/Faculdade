import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class PyGameSreen():
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.running = False

        pygame.init()
        pygame.display.set_mode(self.size, DOUBLEBUF|OPENGL)

    @property
    def size(self):
        return self.width, self.height

    def aspect_ratio(self):
        return self.width, self.height

    def run(self):
        self.running = True
        gluPerspective(45, self.aspect_ratio, 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()