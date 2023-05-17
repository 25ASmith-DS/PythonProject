import pygame

RED = (255, 0, 0)
WIDTH, HEIGHT = 800, 600
SIZE = WIDTH, HEIGHT


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
font_size = 20
font_name = pygame.font.get_default_font()
font = pygame.font.Font(font_name, font_size)

window.fill(RED)
