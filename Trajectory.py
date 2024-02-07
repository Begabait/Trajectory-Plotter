import pygame
import math

pygame.init()

win = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Analytical Approach To Trajectories')

radius = 10
red = (255, 0, 0)


class Ball(object):

    def __init__(self, angle, velocity):
        self.angle = angle
        self.init_velocity = velocity
        self.x_init_velocity = self.init_velocity * math.cos(angle)
        self.y_init_velocity = self.init_velocity * math.sin(angle)
        self.y_velocity = 0
        self.top_time = self.y_init_velocity / 9.81
        self.total_time = self.top_time * 2
        self.time = 0
        self.range = 2 * self.top_time * self.x_init_velocity
        self.x = radius
        self.y = HEIGHT - radius
        self.coors = []

    def draw(self):
        pygame.draw.circle(win, red, (self.x, self.y), radius)

    def trace(self):
        for i in self.coors:
            pygame.draw.circle(win, red, i, 5)


def draw(window):
    window.fill((255, 255, 255))
    if ball_on_screen:
        ball.draw()
        ball.trace()
    pygame.display.update()


running = True
ball_on_screen = False
ball = None

while running:
    WIDTH = win.get_width()
    HEIGHT = win.get_height()
    clock = pygame.time.Clock()
    clock.tick(30)
    draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # could add back 'and not ball_on_screen'
            pos = pygame.mouse.get_pos()
            initial_vel = math.sqrt(pos[0] ** 2 + (HEIGHT - pos[1]) ** 2)
            if pos[0] == 0:
                theta = 0
            else:
                theta = math.atan((HEIGHT - pos[1]) / pos[0])
            ball = Ball(theta, initial_vel)
            ball_on_screen = True

    if ball_on_screen:
        if ball.time > 1.1 * ball.total_time:
            ball = None
            ball_on_screen = False
        else:
            ball.x = ball.x_init_velocity * ball.time
            ball.y = HEIGHT - ((ball.x * math.tan(ball.angle)) - ((9.81 * ball.x ** 2) / (2 * ball.x_init_velocity ** 2)))
            ball.coors.append([ball.x, ball.y])
            ball.time += 1

pygame.quit()
