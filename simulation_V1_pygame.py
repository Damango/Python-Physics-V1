import pygame
import sys
from pygame import gfxdraw
from pygame import display
import random

height = 600
width = 900

pygame.init()
pygame.display.set_caption('Simulation')
screen = pygame.display.set_mode((width,height))


clock = pygame.time.Clock()
ballCount = 20
balls = []


def colorMap(ball):
   theColor = ball.velY
   theFinal = int(theColor / 2.3)
   theFinal = theFinal * theFinal
   return theFinal

class Ball:
    def __init__(self, x, y, velX, velY, r, pType, color):
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.r = r
        self.pType = pType
        self.color = color
        
        
    def pull(self, other):
        if(other.x + other.r > self.x + self.r):
            other.velX -= 1
            other.x += other.velX
            
        if(other.x + other.r < self.x + self.r):
            other.velX += 1
            other.x += other.velX
            
        if(other.y + other.r < self.y + self.r ):
            other.velY += 1
            other.y += other.velY
            
        if(other.y + other.r > self.y + self.r ):
            other.velY -= 1
            other.y += other.velY
        
    def move(self):
        self.x += self.velX
        self.y += self.velY
      
        if(self.x + self.r + self.velX >= width or self.x + self.r + self.velX <= 10 ):
            self.velX *= -1
        if(self.y + self.r + self.velY >= height):
            self.velY *= -1
            self.y = height - 10
            
        if(self.y + self.r + self.velY <= 10):
            self.velY *= -1
           
        self.velY += 1

    def collisions(self, other):
        if((self.x + self.velX ) == (other.x + other.velX)):
            self.velX = -self.velX
            other.velX = -other.velX
            

for i in range(0, ballCount):
    balls.append(Ball(int(random.random() * 800),int(random.random() * 550) , 2, 2, 8, 'no-pull', i * 5))
    
running = True
while running:
   
    pygame.display.update()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for ball in balls:
    
        if(ball.pType == 'pull'):
            pygame.draw.circle(screen, (0,255,0), (450, 300), 30)
            
        else:
            pygame.draw.circle(screen, (ball.color,ball.color,ball.color), (ball.x, ball.y), ball.r)
            
        ball.move()

    
    pygame.display.flip()

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
             sys.exit(0)
