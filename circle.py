from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


class MidpointCircle:
    def __init__(self):
        self.__radius = None
        self.__center_x = None
        self.__center_y = None
        self.__midpoint_points = []

    def set_circle_values(self, radius, center_x=0, center_y=0):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def convert_to_other_zone(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def midpoint_circle_algorithm(self, radius, center_x=0.0, center_y=0.0, y=0):
        glBegin(GL_POINTS)
        # glVertex2f(center_x, center_y)

        d = 1 - radius
        # d_N = 2 * y + 3
        # d_NW = 2 * y - 2 * radius + 5

        x = radius
        glVertex2f(x + center_x, y + center_y)

        for i in range(8):
            x_other, y_other = self.convert_to_other_zone(x, y, i)
            glVertex2f(x_other + center_x, y_other + center_y)

        while x > y:
            if d < 0:
                y = y + 1
                d = d + 2 * y + 3
            else:
                x = x - 1
                y = y + 1
                d = d + 2 * y - 2 * x + 5

            self.__midpoint_points.append((x, y))

            glVertex2f(x + center_x, y + center_y)

            for i in range(8):
                x_other, y_other = self.convert_to_other_zone(x, y, i)
                self.__midpoint_points.append((x_other, y_other))
                glVertex2f(x_other + center_x, y_other + center_y)

        glEnd()


    def draw_space_car(self, radius, center_x=0, center_y=0, angle=0.0):
        car_width = radius * 1.2
        car_length = radius * 1.5

        glPushMatrix()
        glTranslatef(center_x, center_y, 0.0)
        glRotatef(angle, 0.0, 0.0, 1.0)

        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 1.0)  # Blue body

        # Body of the car
        glVertex2f(-car_width / 2, -car_length / 2)
        glVertex2f(car_width / 2, -car_length / 2)
        glVertex2f(car_width / 4, car_length / 2)
        glVertex2f(-car_width / 4, car_length / 2)

        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # Red flames

        # Left flame
        glVertex2f(-car_width / 2, -car_length / 2)
        glVertex2f(-car_width / 2, -car_length / 2 - car_length / 4)
        glVertex2f(-car_width / 4, -car_length / 2 - car_length / 8)

        # Right flame
        glVertex2f(car_width / 2, -car_length / 2)
        glVertex2f(car_width / 2, -car_length / 2 - car_length / 4)
        glVertex2f(car_width / 4, -car_length / 2 - car_length / 8)

        glEnd()

        glPopMatrix()




