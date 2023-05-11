import pygame
from src.math import inside_set


def fragment(p, size, mouse, scale) -> pygame.color.Color:
    width, height = size
    ratio = width / height

    x, y = (
        (p[0] / width - 0.5) * ratio,
        p[1] / height - 0.5
    )

    x /= scale
    y /= scale
    x += mouse[0]
    y += mouse[1]

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)

    xr = round(x, 2)
    yr = round(y, 2)

    if inside_set((x, y), 75):
        return white
    else:
        return black
