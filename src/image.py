import pygame
from src.math import inside_set


def fragment(p, size, mouse, scale, loops) -> pygame.color.Color:
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

    if inside_set((x, y), loops):
        return white
    else:
        return black
