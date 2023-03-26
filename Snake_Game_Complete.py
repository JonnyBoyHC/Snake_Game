import pygame
import time
import random
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

game_Music = pygame.mixer.music
game_Music.load('sounds/Cocktail.mp3')
game_Music.set_volume(0.4)
game_Music.play()

died_Sound = pygame.mixer.Sound('sounds/kl-peach-game-over-iii-142453.mp3')
died_Sound.set_volume(0.5)

eat_Sound = pygame.mixer.Sound('sounds/bleep.ogg')
eat_Sound.set_volume(0.5)

red = (255, 0, 0)
green = (0, 255, 0)
yellow = [255, 255, 102]
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

snake_circle = 10

clock = pygame.time.Clock()
snake_speed = 20

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
  value = score_font.render("Your Score: " + str(score), True, yellow )
  window.blit(value, [0, 0])

def our_snake(snake_circle,  snake_List):
  for x in snake_List:
    pygame.draw.circle(window, green, [x[0], x[1]], snake_circle)

def message(msg, color, x_position, y_position):
  msg = font_style.render(msg, True, color)
  window.blit(msg, [x_position, y_position] )

def game_loop():

  x1 = width / 2
  y1 = height / 2

  game_over = False
  game_close = False

  x1_change = 0
  y1_change = 0

  snake_List = []
  snake_Length = 1

  foodx = round(random.randrange(0, width - snake_circle) / 10.0) * 10.0
  foody = round(random.randrange(0, height - snake_circle) / 10.0) * 10.0

  game_Music.unpause()

  while not game_over:

    while game_close == True:
      window.fill(black)
      message("You Lost!!!", red, width/2 - 45, height/2 - 40)
      message("Press Q to quit or C to continue.", red, width/2 - 150, height/2)
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
      game_Music.pause()
      died_Sound.play()

    x1 += x1_change
    y1 += y1_change

    window.fill(black)

    pygame.draw.circle(window, red, [foodx, foody], snake_circle - 3)

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > snake_Length:
      del snake_List[0]

    for x in snake_List[:-1]:
      if x == snake_Head:
        game_close = True
        game_Music.pause()
        died_Sound.play()

    our_snake(snake_circle, snake_List)
    your_score(snake_Length - 1)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, width - snake_circle) / 10.0) * 10.0
      foody = round(random.randrange(0, height - snake_circle) / 10.0) * 10.0
      eat_Sound.play()
      snake_Length += 1

    clock.tick(snake_speed)

  pygame.quit()
  quit()

game_loop()