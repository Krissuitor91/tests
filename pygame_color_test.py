import pygame


pygame.init()

display_width = 1200
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))
color = [0, 0, 0]
screen.fill(color)


image = pygame.image.load('images/led_pixels_mario.bmp')
x = (display_width * 0.45)
y = (display_height * 0.8)
screen.blit(image, (x,y))

pygame.display.flip()

        
