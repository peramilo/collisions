import pygame


class Ball:
    def __init__(self, px, py, r, m, vx, vy, col):
        self.posX = px
        self.posY = py
        self.velX = vx
        self.velY = vy
        self.colour = col
        self.rad = r
        self.m = m

    def setPos(self):
        self.posX = int(self.posX + self.velX)
        self.posY = int(self.posY + self.velY)

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.posX, self.posY), self.rad, 0)

    def wallColl(self):   # Checks and handles wall collisions
        if self.posX - self.rad <= 0 or self.posX + self.rad >= screenWidth:
            self.velX = - self.velX
        if self.posY - self.rad <= 0 or self.posY + self.rad >= screenHeight:
            self.velY = - self.velY


def ballColl():          # Checks for ball-ball collisions
    for i in range(0, len(ballList)):
        for j in range(0, len(ballList)):
            if i != j and distanceSq(ballList[i], ballList[j]) <= square(ballList[i].rad + ballList[j].rad):
                collision(ballList[i], ballList[j])


def collision(ball1, ball2):
    pass


def distanceSq(ballX, ballY):
    dx = ballX.posX - ballY.posX
    dy = ballX.posY - ballY.posY
    return square(dx) + square(dy)


def square(x):
    return x*x


#pygame.init()
fps = pygame.time.Clock()

screenWidth = 800
screenHeight = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
TEST = (128, 128, 128)
ball1 = Ball(25, 25, 20, 1, 5, 5, WHITE)
ball2 = Ball(160, 110, 20, 1, 4, -4, GREEN)
ball3 = Ball(310, 280, 40, 1, -3, 4, RED)
ballList = [ball2, ball1, ball3]
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Collision')

def main():
    screen.fill(BLACK)
    for ball in ballList:
        ball.draw()
    pygame.display.flip()
    for ball in ballList:
        ball.setPos()
        ball.wallColl()
    ballColl()

while True:
    main()
    fps.tick(60)
