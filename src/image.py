import pygame
from src.math import inside_set, screen_coords


def fragment(p, size, mouse, scale, loops) -> pygame.color.Color:

    x, y = screen_coords(p[0], p[1], size)

    x /= scale
    y /= scale
    x += mouse[0]
    y += mouse[1]

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)

    if inside_set((x, y), loops):
        return white
    else:
        return black
