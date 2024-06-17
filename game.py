import pygame
import sys
import random
import time
#variables
screen_width = 1000
screen_height = 800
player_x, player_y = 100, 720   # Initial position
player_speed = 5  # Speed of the square
player_size = 50
color = (255,0,0)
player_y_speed = 0
is_jumping = False
jump_speed = -30
gravity = 2
rect_x = random.randint(10, 800)
rect_y = 650
x = 1
rect_width = 100
rect_height = 10
rects = [(rect_x,rect_y,rect_width,rect_height)]
dash_speed = 20
dash_timer = 0
dash_cooldown = 30
points = 0
previous_points = 0

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")
clock = pygame.time.Clock()
running = True



while running:
   # Handle events
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         sys.exit()


      

   
   keys = pygame.key.get_pressed()
   if keys[pygame.K_d]:
      player_x += player_speed
   if keys[pygame.K_a]:
      player_x -= player_speed
   if keys[pygame.K_SPACE] and not is_jumping:
      player_y_speed = jump_speed
      is_jumping = True
      rect_x = random.randint(10,800)
      rects.append((rect_x,rect_y,rect_width,rect_height))
   if keys[pygame.K_LSHIFT] and is_jumping:
      if keys[pygame.K_a]:
         
         player_x -= dash_speed


      if keys[pygame.K_d]:
         
         player_x += dash_speed

      
   player_y_speed += gravity
   player_y += player_y_speed
   if player_y >= screen_height - player_size - 30:
      player_y = screen_height - player_size - 30
      player_y_speed = 0
      is_jumping = False

   if player_y <= 0:
      player_y = 0
   if player_y >= 850:
      player_y = 850
   if (player_x + player_size > rect_x
      and player_x < rect_x + rect_width
      and player_y + player_size > rect_y
      and player_y + player_size - player_y_speed <= rect_y + rect_height
      and player_y_speed > 0):
      points += 1
      player_y = rect_y - player_size
      player_y_speed = 0
      is_jumping = False

   screen.fill((0, 0,0))
   player = pygame.draw.rect(screen, color, pygame.Rect(player_x, player_y, player_size, player_size))
    
   for rectss in rects:
      rect = pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, rect_width, rect_height))
   
    # Print points only if they have increased
   if points > previous_points:
      print(points)
      previous_points = points  # Update previous points

   pygame.display.flip()

   pygame.time.Clock().tick(60)
    


pygame.quit()


