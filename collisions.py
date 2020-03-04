import pygame
import random
import math


class Ball:
    def __init__(self, px, py, r, m, vx, vy, col):
        self.posX = px
        self.posY = py
        self.velX = vx
        self.velY = vy
        self.colour = col
        self.rad = r
        self.mass = m

    def setPos(self):
        global counter
        self.posX = toInt(self.posX + self.velX)
        self.posY = toInt(self.posY + self.velY)

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.posX, self.posY), self.rad, 0)

    def wallColl(self):     # Checks and handles wall collisions
        if self.posX - self.rad <= 0:
            self.posX = self.rad + 1
            self.velX = - self.velX
        elif self.posX + self.rad >= screenWidth:
            self.posX = screenWidth - self.rad - 1
            self.velX = - self.velX 
        if self.posY - self.rad <= 0:
            self.posY = self.rad + 1
            self.velY = - self.velY
        elif self.posY + self.rad >= screenHeight:
            self.posY = screenHeight - self.rad - 1
            self.velY = - self.velY


def collision(ball1, ball2):        # Handles ball-ball collisions
    dist = math.sqrt(distanceSq(ball1, ball2))
    overlap = ball1.rad + ball2.rad - dist
    dx = abs(ball1.posX - ball2.posX)
    dy = abs(ball1.posY - ball2.posY)
    overx = 0.5 * overlap * dx / dist
    overy = 0.5 * overlap * dy / dist
    if ball1.posX - ball2.posX < 0:
        ball1.posX -= toInt(overx)
        ball2.posX += toInt(overx)
    else:
        ball1.posX += toInt(overx)
        ball2.posX -= toInt(overx)
    if ball1.posY - ball2.posY > 0:
        ball1.posY += toInt(overy)
        ball2.posY -= toInt(overy)
    else:
        ball1.posY -= toInt(overy)
        ball2.posY += toInt(overy)
    dsq = distanceSq(ball1, ball2)
    f1 = ((ball1.velX - ball2.velX)*(ball1.posX - ball2.posX) + (ball1.velY - ball2.velY)*(ball1.posY - ball2.posY)) / dsq
    ball1.velX -= (2 * ball2.mass / (ball1.mass + ball2.mass)) * f1 * (ball1.posX - ball2.posX)
    ball1.velY -= (2 * ball2.mass / (ball1.mass + ball2.mass)) * f1 * (ball1.posY - ball2.posY)
    ball2.velX -= (2 * ball1.mass / (ball1.mass + ball2.mass)) * f1 * (ball2.posX - ball1.posX)
    ball2.velY -= (2 * ball1.mass / (ball1.mass + ball2.mass)) * f1 * (ball2.posY - ball1.posY)

def distanceSq(ballX, ballY):
    dx = ballX.posX - ballY.posX
    dy = ballX.posY - ballY.posY
    return dx ** 2 + dy ** 2

def toInt(x):
    if x - int(x) < 0.5:
        return int(x)
    else:
        return int(x+1)


fps = pygame.time.Clock()
screenWidth = 800
screenHeight = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
COL1 = (128, 128, 128)
COL2 = (120, 15, 65)
ball1 = Ball(25, 25, 20, 1, random.randint(1, 4), random.randint(1, 4), WHITE)
ball2 = Ball(160, 110, 35, 2, random.randint(1, 4), random.randint(1, 4), GREEN)
ball3 = Ball(310, 280, 20, 1, random.randint(1, 4), random.randint(1, 4), RED)
ball4 = Ball(600, 500, 20, 1, random.randint(1, 4), random.randint(1, 4), COL1)
ball5 = Ball(200, 500, 20, 1, random.randint(1, 4), random.randint(1, 4), COL2)
ballList = [ball1, ball2, ball3, ball4, ball5]
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Collision')

def main():
    screen.fill(BLACK)
    for ball in ballList:
        ball.draw()
        ball.wallColl()
        for ball2 in ballList:
            if ball != ball2 and distanceSq(ball, ball2) <= (ball.rad + ball2.rad) ** 2:
                collision(ball, ball2)
        ball.setPos()
    pygame.display.flip()

while True:
    main()
    fps.tick(60)



