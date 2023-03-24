import pygame
pygame.init()
width = 700
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

  pygame.draw.circle(window, green, [100, 100], 7)
  pygame.display.update()

pygame.quit()
quit()