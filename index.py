import pygame
from sys import exit
from pygame.locals import *

pygame.init()

size = 640, 480 #width, height
speed = []
blackgroundColor = pygame.Color(0, 0, 0, 1)

screen = pygame.display.set_mode(size) #tela

pygame.display.set_caption("tic tac toe")

while True:
  for event in pygame.event.get(): #deixar a tela em loop
    if event.type == QUIT:
      pygame.quit()
      exit()
    
    pygame.draw.rect(screen, (255, 0, 0), (200, 300, 40, 50))
    pygame.draw.circle(screen, (0, 0, 255), (100, 200), 50)
    pygame.draw.line(screen, (255, 255, 0), (10, 50), (10, 200), 5)
    pygame.display.update()