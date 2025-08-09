import pygame
import random
from pygame.math import Vector2

# define classes
class Ball():
    def __init__(self, x, y, radius, color):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.radius = radius
        self.color = color

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, 
                           (int(self.position.x), int(self.position.y)),self.radius)


# initialize pygame
pygame.init()

# define display_surface 
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("kinemetic movement")

# set the game values
GRAVITY = Vector2(0, 0.5)



# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()

ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT - 50, 24, 'red')
#ball = Ball(WINDOW_WIDTH//2, 50, 24, 'red')
initial_velocity_x = 5
initial_velocity_y = -25.0

ball.velocity.x = initial_velocity_x
ball.velocity.y = initial_velocity_y
ball.acceleration = GRAVITY

# main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()

    # fill the backgound
    display_surface.fill('black')

    # draw the assets
    ball.draw(display_surface)

    # update the display
    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()


