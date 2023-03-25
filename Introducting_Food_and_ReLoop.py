import pygame
import time
import random
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

snake_circle = 10

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
  msg = font_style.render(msg, True, color)
  window.blit(msg, [width/2 - 85, height/2 - 20] )

def game_loop():

  x1 = width / 2
  y1 = height / 2

  game_over = False
  game_close = False

  x1_change = 0
  y1_change = 0

  foodx = round(random.randrange(0, width - snake_circle) / 10.0) * 10.0
  foody = round(random.randrange(0, height - snake_circle) / 10.0) * 10.0

  while not game_over:
    while game_close == True:
      window.fill(black)
      message("You Lost. Press Q to quit C to continue.", red)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over = True
            game_close = False
          if event.key == pygame.K_c:
            game_loop()

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
      game_close = True

    x1 += x1_change
    y1 += y1_change

    window.fill(black)
    pygame.draw.circle(window, red, [foodx, foody], snake_circle - 3)
    pygame.draw.circle(window, green, [x1, y1], snake_circle)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
      print("Food Eaten")

    clock.tick(snake_speed)

  pygame.quit()
  quit()

game_loop()