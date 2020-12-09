import pygame
import os

os.chdir('./Documents/Python3.8/pygame')
print(os.getcwd())

pygame.init ()

#create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Define Player
playerImg = pygame.image.load('spaceship.png')
playerX = 400
playerY = 480

def player(x,y):
    screen.blit(playerImg,(playerX,playerY))

running = True

while running:
    # RGB = Red,Green, Blue
    screen.fill((100,0,0))
    playerX += .1
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX,playerY)
    pygame.display.update()