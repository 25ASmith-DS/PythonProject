import pygame
from src.math import inside_set, screen_coords, cartesian_product
from src.init import RED, WIDTH, HEIGHT


def fragment(p, size, offset, scale, loops) -> pygame.color.Color:

    x, y = screen_coords(p, size, scale, offset)

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)

    if inside_set((x, y), loops):
        return white
    else:
        return black


def render_fractal(window: pygame.Surface, points, camera, zoom, loops):
    cam_x, cam_y = camera
    for i, p in enumerate(points):
        color = fragment(p, (WIDTH, HEIGHT), (cam_x, cam_y), zoom, loops)
        window.set_at(p, color)
        if p[0] == 0:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


def create_info_text(font, camera_pos, zoom, precision):
    surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)

    cam_x, cam_y = camera_pos

    zoom_text = font.render(f"Zoom: {zoom}", True, RED)
    cam_text_x = font.render(f"Center X: {round(cam_x, precision)}", True, RED)
    cam_text_y = font.render(f"Center X: {round(cam_y, precision)}", True, RED)

    text_height = zoom_text.get_height() \
        + cam_text_x.get_height() \
        + cam_text_y.get_height()

    y = HEIGHT - text_height
    surf.blit(zoom_text, (0, y))
    y += zoom_text.get_height()
    surf.blit(cam_text_x, (0, y))
    y += cam_text_x.get_height()
    surf.blit(cam_text_y, (0, y))
    y += cam_text_y.get_height()

    return surf
