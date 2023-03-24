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

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -10
        y1_change = 0
      elif event.key == pygame.K_RIGHT:
        x1_change = 10
        y1_change = 0
      elif event.key == pygame.K_UP:
        x1_change = 0
        y1_change = -10
      elif event.key == pygame.K_DOWN:
        x1_change = 0
        y1_change = 10

  x1 += x1_change
  y1 += y1_change

  window.fill(black)

  pygame.draw.circle(window, green, [x1, y1], 7)
  pygame.display.update()
  clock.tick(30)

pygame.quit()
quit()