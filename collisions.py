from __future__ import division
import pygame
import random


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


def collision(ball1, ball2):        # Handles ball-ball collisions
    dsq = distanceSq(ball1, ball2)
    f1 = ((ball1.velX - ball2.velX)*(ball1.posX - ball2.posX) + (ball1.velY - ball2.velY)*(ball1.posY - ball2.posY)) / dsq
    f2 = ((ball2.velX - ball1.velX)*(ball2.posX - ball1.posX) + (ball2.velY - ball1.velY)*(ball2.posY - ball1.posY)) / dsq
    ball1.velX -= (2 * ball2.mass / (ball1.mass + ball2.mass)) * f1 * (ball1.posX - ball2.posX)
    ball1.velY = ball1.velY - (2 * ball2.mass / (ball1.mass + ball2.mass)) * f1 * (ball1.posY - ball2.posY)
    ball2.velX = ball2.velX - (2 * ball1.mass / (ball1.mass + ball2.mass)) * f2 * (ball2.posX - ball1.posX)
    ball2.velY = ball2.velY - (2 * ball1.mass / (ball1.mass + ball2.mass)) * f2 * (ball2.posY - ball1.posY)
    #p = (2 * ball2.mass / (ball1.mass + ball2.mass)) * f1 * (ball1.posX - ball2.posX) / dsq
    ball1.setPos()
    ball2.setPos()


def distanceSq(ballX, ballY):
    dx = ballX.posX - ballY.posX
    dy = ballX.posY - ballY.posY
    return square(dx) + square(dy)


def square(x):
    return x*x



fps = pygame.time.Clock()

screenWidth = 800
screenHeight = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
TEST = (128, 128, 128)
ball1 = Ball(25, 25, 20, 1, random.randint(0, 4), random.randint(0, 4), WHITE)
ball2 = Ball(160, 110, 20, random.randint(0, 4), random.randint(0, 4), -3, GREEN)
ball3 = Ball(310, 280, 40, random.randint(0, 4), random.randint(0, 4), 3, RED)
ballList = [ball2, ball1, ball3]
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Collision')

def main():
    screen.fill(BLACK)
    for ball in ballList:
        ball.draw()
        ball.wallColl()
        ball.setPos()
    pygame.display.flip()
    ballColl()

while True:
    main()
    fps.tick(50)
