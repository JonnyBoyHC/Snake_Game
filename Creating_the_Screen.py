import pygame
pygame.init()
width = 700
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption("Snake Game")
game_over = False
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
pygame.quit()
quit()