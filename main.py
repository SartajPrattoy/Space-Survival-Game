from circle import MidpointCircle
from line import MidpointLine
from digits import Digits
from uiTexts import UI_Text

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from random import randint
from threading import Thread
from time import sleep
from pynput.keyboard import Key, Controller


auto_key_press = Controller()
scale_radius = 0
SCORE = 0
HEALTH = 99

line = MidpointLine()
circle = MidpointCircle()
ui_text = UI_Text()
colors = 0, 0, 0

PLAYER_CURRENT_X_POSITION = 0
PLAYER_CURRENT_Y_POSITION = - 600
PLAYER_RADIUS = 65

OBJECT1_CURRENT_X_POSITION = randint(-600, 600)
OBJECT1_CURRENT_Y_POSITION = 900
OBJECT1_SPEED = 10

OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
OBJECT2_CURRENT_Y_POSITION = 900
OBJECT2_SPEED = 12

OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
OBJECT3_CURRENT_Y_POSITION = 900
OBJECT3_SPEED = 20

OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
OBJECT4_CURRENT_Y_POSITION = 900
OBJECT4_SPEED = 14

OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
OBJECT5_CURRENT_Y_POSITION = 900
OBJECT5_SPEED = 22

OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
OBJECT6_CURRENT_Y_POSITION = 900
OBJECT6_SPEED = 10

OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
OBJECT7_CURRENT_Y_POSITION = 900
OBJECT7_SPEED = 8

OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
OBJECT8_CURRENT_Y_POSITION = 900
OBJECT8_SPEED = 14

OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
OBJECT9_CURRENT_Y_POSITION = 900
OBJECT9_SPEED = 20

OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
OBJECT10_CURRENT_Y_POSITION = 900
OBJECT10_SPEED = 12

SPEED_MULTIPLIER = 2


GAME_OVER = False


def player_health_system():
    global PLAYER_RADIUS, \
        HEALTH, \
        GAME_OVER

    PLAYER_RADIUS += 1
    HEALTH -= 1
    if HEALTH <= 0:
        HEALTH = 0
        GAME_OVER = True

def update():
    global colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, \
        OBJECT2_SPEED, \
        OBJECT3_SPEED, \
        OBJECT4_SPEED, \
        OBJECT5_SPEED, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED, \
        OBSTACLE_RADIUS, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_CURRENT_X_POSITION, \
        SPEED_MULTIPLIER, \
        GAME_OVER

    while True:
        SPEED_MULTIPLIER += 0.0001
        colors = 1, 1, 1
        auto_key_press.press(",")
        sleep(0.1)

        if GAME_OVER:
            break



        # Obstacles
        OBJECT1_CURRENT_Y_POSITION += - OBJECT1_SPEED * SPEED_MULTIPLIER
        if OBJECT1_CURRENT_Y_POSITION < - 900:
            OBJECT1_CURRENT_Y_POSITION = 900
            OBJECT1_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT2_CURRENT_Y_POSITION += - OBJECT2_SPEED * SPEED_MULTIPLIER
        if OBJECT2_CURRENT_Y_POSITION < - 900:
            OBJECT2_CURRENT_Y_POSITION = 900
            OBJECT2_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT3_CURRENT_Y_POSITION += - OBJECT3_SPEED * SPEED_MULTIPLIER
        if OBJECT3_CURRENT_Y_POSITION < - 900:
            OBJECT3_CURRENT_Y_POSITION = 900
            OBJECT3_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT4_CURRENT_Y_POSITION += - OBJECT4_SPEED * SPEED_MULTIPLIER
        if OBJECT4_CURRENT_Y_POSITION < - 900:
            OBJECT4_CURRENT_Y_POSITION = 900
            OBJECT4_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT5_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT5_CURRENT_Y_POSITION < - 900:
            OBJECT5_CURRENT_Y_POSITION = 900
            OBJECT5_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT6_CURRENT_Y_POSITION += - OBJECT6_SPEED * SPEED_MULTIPLIER
        if OBJECT6_CURRENT_Y_POSITION < - 900:
            OBJECT6_CURRENT_Y_POSITION = 900
            OBJECT6_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT7_CURRENT_Y_POSITION += - OBJECT7_SPEED * SPEED_MULTIPLIER
        if OBJECT7_CURRENT_Y_POSITION < - 900:
            OBJECT7_CURRENT_Y_POSITION = 900
            OBJECT7_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT8_CURRENT_Y_POSITION += - OBJECT8_SPEED * SPEED_MULTIPLIER
        if OBJECT8_CURRENT_Y_POSITION < - 900:
            OBJECT8_CURRENT_Y_POSITION = 900
            OBJECT8_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT9_CURRENT_Y_POSITION += - OBJECT9_SPEED * SPEED_MULTIPLIER
        if OBJECT9_CURRENT_Y_POSITION < - 900:
            OBJECT9_CURRENT_Y_POSITION = 900
            OBJECT9_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT10_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT10_CURRENT_Y_POSITION < - 900:
            OBJECT10_CURRENT_Y_POSITION = 900
            OBJECT10_CURRENT_X_POSITION = randint(-600, 600)

        # Re-render the display
        glutPostRedisplay()


def score_increment():
    global SCORE
    while True:
        sleep(1)
        glutPostRedisplay()
        SCORE += 1
        if GAME_OVER:
            break


def RESTART():
    global colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, OBJECT2_SPEED, \
        OBJECT3_SPEED, OBJECT4_SPEED, \
        OBJECT5_SPEED, SPEED_MULTIPLIER, \
        PLAYER_CURRENT_X_POSITION, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_RADIUS, \
        SCORE, \
        OBSTACLE_RADIUS, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED

    PLAYER_CURRENT_X_POSITION = 0
    PLAYER_CURRENT_Y_POSITION = - 600
    PLAYER_RADIUS = 65

    SCORE = 0

    OBJECT1_CURRENT_X_POSITION = randint(-600, 600)  # - 600 => 600
    OBJECT1_CURRENT_Y_POSITION = 900
    OBJECT1_SPEED = 10

    OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT2_CURRENT_Y_POSITION = 900
    OBJECT2_SPEED = 12

    OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT3_CURRENT_Y_POSITION = 900
    OBJECT3_SPEED = 20

    OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT4_CURRENT_Y_POSITION = 900
    OBJECT4_SPEED = 14

    OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT5_CURRENT_Y_POSITION = 900
    OBJECT5_SPEED = 22

    OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT6_CURRENT_Y_POSITION = 900
    OBJECT6_SPEED = 10

    OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT7_CURRENT_Y_POSITION = 900
    OBJECT7_SPEED = 8

    OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT8_CURRENT_Y_POSITION = 900
    OBJECT8_SPEED = 14

    OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT9_CURRENT_Y_POSITION = 900
    OBJECT9_SPEED = 20

    OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT10_CURRENT_Y_POSITION = 900
    OBJECT10_SPEED = 12

    SPEED_MULTIPLIER = 2

# def draw_star(x, y, outer_radius, inner_radius, num_points):
#     angle = math.pi / num_points
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex2f(x, y)
#     for i in range(num_points * 2 + 1):
#         radius = outer_radius if i % 2 == 0 else inner_radius
#         x_pos = x + radius * math.cos(i * angle)
#         y_pos = y + radius * math.sin(i * angle)
#         glVertex2f(x_pos, y_pos)
#     glEnd()
# def draw_asteroid(x, y, outer_radius, inner_radius, num_points):
#     angle = math.pi / num_points
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex2f(x, y)
#     for i in range(num_points * 2 + 1):
#         radius = outer_radius if i % 2 == 0 else inner_radius
#         deviation = randint(1, 10)  # Random deviation from the radius
#         x_pos = x + (radius + deviation) * math.cos(i * angle)
#         y_pos = y + (radius + deviation) * math.sin(i * angle)
#         glVertex2f(x_pos, y_pos)
#     glEnd()

def asteroid(x, y):
    glBegin(GL_POLYGON)
    glColor3f(1, 0.0, 0.0)  # Red color for asteroid
    num_segments = 20
    outer_radius = 30
    inner_radius = 20

    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        outer_x = outer_radius * math.cos(theta)
        outer_y = outer_radius * math.sin(theta)
        inner_theta = 2.0 * math.pi * (i + 0.5) / num_segments
        inner_x = inner_radius * math.cos(inner_theta)
        inner_y = inner_radius * math.sin(inner_theta)

        glVertex2f(x + outer_x, y + outer_y)
        glVertex2f(x + inner_x, y + inner_y)

    glEnd()


def meteorite(x, y):
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)  # Gray color for meteorite
    num_segments = 20
    radius = 15

    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        cx = radius * math.cos(theta)
        cy = radius * math.sin(theta)
        glVertex2f(x + cx, y + cy)

    glEnd()


class Survive_In_Space:
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0, pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.pixel_size = pixel_size

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(b'RAJAProject')
        glClearColor(0, 0, 0, 0)
        glutDisplayFunc(self.show_screen)

        glutKeyboardFunc(self.buttons)

        animation_thread = Thread(target=update)
        animation_thread.start()

        global score_thread
        score_thread = Thread(target=score_increment)
        score_thread.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def buttons(self, key, x, y):
        global PLAYER_CURRENT_Y_POSITION, \
            PLAYER_CURRENT_X_POSITION, \
            PLAYER_RADIUS, \
            GAME_OVER, \
            HEALTH, \
            SCORE

        move = 50

        # Movement inputs
        if key == b"w":
            PLAYER_CURRENT_Y_POSITION += move
        if key == b"a" and PLAYER_CURRENT_X_POSITION > - 600:
            PLAYER_CURRENT_X_POSITION -= move
        if key == b"s":
            PLAYER_CURRENT_Y_POSITION -= move
        if key == b"d" and PLAYER_CURRENT_X_POSITION < 600:
            PLAYER_CURRENT_X_POSITION += move

        # Restart game when "r" button is pressed
        if key == b"r":
            GAME_OVER = False
            PLAYER_RADIUS = 65
            HEALTH = 99

            restart = Thread(target=update)
            restart.start()

            SCORE = 0
            restart_score = Thread(target=score_increment)
            restart_score.start()

        if PLAYER_CURRENT_Y_POSITION < - self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = self.win_size_y

        if PLAYER_CURRENT_X_POSITION < - self.win_size_x:
            PLAYER_CURRENT_X_POSITION = self.win_size_x

        if PLAYER_CURRENT_Y_POSITION > self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = - self.win_size_y

        if PLAYER_CURRENT_X_POSITION > self.win_size_x:
            PLAYER_CURRENT_X_POSITION = - self.win_size_x


        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 1")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 2")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 3")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 4")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 5")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 6")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 7")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 8")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 9")
            player_health_system()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Ahha!! Touch lege gelo, 10")
            player_health_system()

        glutPostRedisplay()

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        # Drawing methods
        self.road(),
        ui_text.health_text(-1800,600)
        ui_text.score_text(950, 600)
        glColor3f(0, 1, 0)
        ui_text.sartaj_text(-1800, -300)
        ui_text.imamul_text(-1800, -500)
        ui_text.asif_text(-1800, -700)

        # Obstacles
        glColor3f(0, 0, 1)
        glPointSize(2)
        self.obstacle(OBJECT1_CURRENT_X_POSITION, OBJECT1_CURRENT_Y_POSITION)
        self.obstacle(OBJECT2_CURRENT_X_POSITION, OBJECT2_CURRENT_Y_POSITION)
        self.obstacle(OBJECT3_CURRENT_X_POSITION, OBJECT3_CURRENT_Y_POSITION)
        self.obstacle(OBJECT4_CURRENT_X_POSITION, OBJECT4_CURRENT_Y_POSITION)
        self.obstacle(OBJECT5_CURRENT_X_POSITION, OBJECT5_CURRENT_Y_POSITION)
        self.obstacle(OBJECT6_CURRENT_X_POSITION, OBJECT6_CURRENT_Y_POSITION)
        self.obstacle(OBJECT7_CURRENT_X_POSITION, OBJECT7_CURRENT_Y_POSITION)
        self.obstacle(OBJECT8_CURRENT_X_POSITION, OBJECT8_CURRENT_Y_POSITION)
        self.obstacle(OBJECT9_CURRENT_X_POSITION, OBJECT9_CURRENT_Y_POSITION)
        self.obstacle(OBJECT10_CURRENT_X_POSITION, OBJECT10_CURRENT_Y_POSITION)

        # Player
        glColor3f(1, 1, 1)
        circle.draw_space_car(PLAYER_RADIUS, PLAYER_CURRENT_X_POSITION, PLAYER_CURRENT_Y_POSITION)
        glPointSize(10)

        # Score
        score_and_health_text = Digits()
        digit_position = 900

        glColor3f(colors[0], colors[1], colors[2])
        score_and_health_text.draw_digit(f"{SCORE}", offset_x=10, offset_y=-350+10, digit_position_x= 850)

        glColor3f(colors[2], colors[1], colors[0])
        score_and_health_text.draw_digit(f"{HEALTH}", digit_position_x= -1900+10, offset_x=10, offset_y=-300)

        # Drawing cross marks when the game is over
        # Drawing cross marks when the game is over
        if GAME_OVER:
            glColor3f(0, 0, 1)

            for i in range(0, 10, 2):
                circle.midpoint_circle_algorithm(900 - i, 0, 0)

            glColor3f(1, 0, 0)
            ui_text.game_over_text(-650, 0)

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def road(self):
        left_x1, left_y1 = -700, -900
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, 900)

    def obstacle(self, obstacle_x_position, obstacle_y_position):
        if randint(0, 1) == 0:  # Randomly choose between meteorite and asteroid
            # circle_radius = OBSTACLE_RADIUS
            # circle.midpoint_circle_algorithm(circle_radius, obstacle_x_position, obstacle_y_position)
            meteorite(obstacle_x_position, obstacle_y_position)
        else:
            # star_outer_radius = randint(OBSTACLE_RADIUS - 10, OBSTACLE_RADIUS + 10)
            # star_inner_radius = randint(5, 20)
            # draw_star(obstacle_x_position, obstacle_y_position, star_outer_radius, star_inner_radius, num_points=5)
            # asteroid_outer_radius = randint(OBSTACLE_RADIUS - 10, OBSTACLE_RADIUS + 10)
            # asteroid_inner_radius = randint(5, 20)
            # draw_asteroid(obstacle_x_position, obstacle_y_position, asteroid_outer_radius, asteroid_inner_radius,
            #               num_points=8)
            asteroid(obstacle_x_position, obstacle_y_position)


survive_in_space = Survive_In_Space(win_size_x=1920, win_size_y=900, pixel_size=1)

survive_in_space.initialize()
survive_in_space.start_main_loop()
