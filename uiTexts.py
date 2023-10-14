from circle import MidpointCircle
from line import MidpointLine
from digits import Digits


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


line = MidpointLine()
circle = MidpointCircle()


class UI_Text:
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0, title="Surviving gane",
                 pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.title = title
        self.pixel_size = pixel_size

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(25)
        glLoadIdentity()

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)
        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def game_over_text(self, x=0, y=0):
        self.g(adjust=0, x= 10+ x, y= 10+ y)
        self.a(adjust=150, x= 10+ x, y= 10+ y)
        self.m(adjust=300, x= 10 + x, y= 10 + y)
        self.e(adjust=450, x= 10 + x, y= 10 + y)
        self.o(adjust=750, x= 10 + x, y= 10 + y)
        self.v(adjust=900, x= 10 + x, y= 10 + y)
        self.e(adjust=1050, x= 10 + x, y= 10 + y)
        self.r(adjust=1200, x= 10 + x, y= 10 + y)

    def health_text(self, x=5, y=10):
        self.h(adjust=50,x=10 + x, y=10 + y)
        self.e(adjust=180,x=10+x, y=10+y)
        self.a(adjust=310,  x=10+x,y=10+y)
        self.l(adjust=440, x=10+x,  y=10+y)
        self.t(adjust=570, x=10+x,  y=10+y)
        self.h(adjust=700, x=10+x, y=10+y)

    def score_text(self, x=0, y=0):
        self.s(adjust=50, x= 10+ x, y= 10+ y)
        self.c(adjust=180, x= 10 + x, y= 10 + y)
        self.o(adjust=310, x= 10 + x, y= 10 + y)
        self.r(adjust=440, x= 10 + x, y= 10 + y)
        self.e(adjust=570, x= 10 + x, y= 10+ y)
    def sartaj_text(self, x=0, y=0):
        self.s_1(adjust=50, x= 10+ x, y= 10+ y)
        self.a_1(adjust=180, x= 10 + x, y= 10 + y)
        self.r_1(adjust=310, x= 10 + x, y= 10 + y)
        self.t_1(adjust=420, x= 10 + x, y= 10 + y)
        self.a_1(adjust=550, x= 10 + x, y= 10+ y)
        self.j(adjust=630, x=10 + x, y=10 + y)
    def imamul_text(self, x=0, y=0):
        self.i(adjust=50, x= 10+ x, y= 10+ y)
        self.m_1(adjust=180, x= 10 + x, y= 10 + y)
        self.a_1(adjust=310, x= 10 + x, y= 10 + y)
        self.m_1(adjust=420, x= 10 + x, y= 10 + y)
        self.u(adjust=550, x= 10 + x, y= 10+ y)
        self.l_1(adjust=680, x=10 + x, y=10 + y)
    def asif_text(self, x=0, y=0):
        self.a_1(adjust=50, x= 10+ x, y= 10+ y)
        self.s_1(adjust=180, x= 10 + x, y= 10 + y)
        self.i(adjust=310, x= 10 + x, y= 10 + y)
        self.f(adjust=420, x= 10 + x, y= 10 + y)

    def a(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle

    def g(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom
        line.midpoint(x + 20 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle

    def m(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 45 + adjust, y + 10 + 80, x + 80 + adjust, y + 60 + 80)
        line.midpoint(x + 40 + adjust, y + 10 + 80, x + 0 + adjust, y + 60 + 80)

    def e(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 0 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def o(self,  x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 00, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom

    def v(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 150, x + 45 + adjust, y + 0)  # Left
        line.midpoint(x + 45 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right
    def r(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 70, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle
        line.midpoint(x + 80 + adjust, y + 0, x + 30 + adjust, y + 65)  # Bottom Left Corner

    def h(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 150)  # Right
        line.midpoint(x + 0 + adjust, y + 70, x + 80 + adjust, y + 70)  # Middle,

    def l(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 80 + adjust, y + 0)  # Bottom

    def t(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 35 + adjust, y + 0, x + 35 + adjust, y + 150)  # Left

    def s(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 70, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 70 + adjust, y + 0, x + 70 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 0 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def c(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 150)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 0 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom

    def s_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 50, x + 0 + adjust, y + 100)  # Left Top
        line.midpoint(x + 0 + adjust, y + 50, x + 50 + adjust, y + 50)  # Left Top
        line.midpoint(x + 0 + adjust, y + 100, x + 50 + adjust, y + 100)  # Left Top
        line.midpoint(x + 50 + adjust, y + 50, x + 50 + adjust, y + 0)  # Left Top
        line.midpoint(x + 0 + adjust, y + 0, x + 50 + adjust, y + 0)  # Left Top

    def a_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left
        line.midpoint(x + 50 + adjust, y + 0, x + 50 + adjust, y + 100)  # right
        line.midpoint(x + 0 + adjust, y + 100, x + 50 + adjust, y + 100)  # right
        line.midpoint(x + 0 + adjust, y + 50, x + 50 + adjust, y + 50)  # middle

    def r_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left
        line.midpoint(x + 50 + adjust, y + 50, x + 50 + adjust, y + 100)  # right
        line.midpoint(x + 0 + adjust, y + 100, x + 50 + adjust, y + 100)  # right
        line.midpoint(x + 0 + adjust, y + 50, x + 50 + adjust, y + 50)  # middle
        line.midpoint(x + 50 + adjust, y + 0, x + 30 + adjust, y + 50)

    def t_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 100, x + 80 + adjust, y + 100)  # Top
        line.midpoint(x + 50 + adjust, y + 0, x + 50 + adjust, y + 100)  # Left

    def j(self, x=0, y=0, adjust=0):
        line.midpoint(x + 50 + adjust, y + 0, x + 75 + adjust, y + 0)  # bottom
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 100)  # Left
        line.midpoint(x + 50 + adjust, y + 0, x + 50 + adjust, y + 30)  # Left
    def i(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # bottom

    def m_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left
        line.midpoint(x + 50 + adjust, y + 0, x + 50 + adjust, y + 100)  # Right,
        line.midpoint(x + 0 + adjust, y + 100, x + 25 + adjust, y + 50)  # Right,
        line.midpoint(x + 50 + adjust, y + 100, x + 25 + adjust, y + 50)  # Right
    def u(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left
        line.midpoint(x + 50 + adjust, y + 0, x + 50 + adjust, y + 100)  # Right,
        line.midpoint(x + 0 + adjust, y + 0, x + 50 + adjust, y + 0)  # Left
    def l_1(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 0, x + 50 + adjust, y + 0)  # Bottom

    def f(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 100)  # Left
        line.midpoint(x + 0 + adjust, y + 100, x + 50 + adjust, y + 100)  # right
        line.midpoint(x + 0 + adjust, y + 50, x + 50 + adjust, y + 50)  # middle


