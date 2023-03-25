import pygame
import time
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

x1 = width / 2
y1 = height / 2

snake_circle = 7

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
  msg = font_style.render(msg, True, color)
  window.blit(msg, [width/2 - 85, height/2 - 20] )

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -snake_circle
        y1_change = 0
      elif event.key == pygame.K_RIGHT:
        x1_change = snake_circle
        y1_change = 0
      elif event.key == pygame.K_UP:
        x1_change = 0
        y1_change = -snake_circle
      elif event.key == pygame.K_DOWN:
        x1_change = 0
        y1_change = snake_circle

  if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
    game_over = True

  x1 += x1_change
  y1 += y1_change

  window.fill(black)

  pygame.draw.circle(window, green, [x1, y1], snake_circle)
  pygame.display.update()
  clock.tick(snake_speed)

message("You Lost!!!", red)
pygame.display.update()
time.sleep(6)
pygame.quit()
quit()