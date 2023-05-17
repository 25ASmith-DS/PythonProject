import pygame
from src.math import inside_set, screen_coords, cartesian_product


def fragment(p, size, offset, scale, loops) -> pygame.color.Color:

    x, y = screen_coords(p, size, scale, offset)

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)

    if inside_set((x, y), loops):
        return white
    else:
        return black


def render_fractal(window: pygame.Surface, camera, zoom, loops):
    w, h = window.get_size()
    cam_x, cam_y = camera
    points = cartesian_product(w, h)
    
    for i, p in enumerate(points):
        color = fragment(p, (w, h), (cam_x, cam_y), zoom, loops)
        window.set_at(p, color)
        if p[0] == 0:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    