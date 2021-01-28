import sys
import pygame

pygame.init()

x = 900
y = 600
black = (0, 0, 0)

display_surface = pygame.display.set_mode((x, y))

pygame.display.set_caption('Stars')

image = pygame.image.load('images/star.jpg')

while True:
    display_surface.fill(black)
    display_surface.blit(image, (0, 0))

if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()

pygame.display.update()
