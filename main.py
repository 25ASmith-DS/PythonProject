import pygame
import math
from src.image import fragment
from src.math import screen_coords
from src.init import WIDTH, HEIGHT, SIZE, RED, window, font, font_size


def gen_points(w, h):
    points = []
    for y in range(h):
        for x in range(w):
            points.append((x, y))
    return points


def generation_loop(window, points, camera, zoom, loops):
    for i, p in enumerate(points):
        color = fragment(p, (WIDTH, HEIGHT), (cam_x, cam_y), zoom, loops)
        window.set_at(p, color)
        if p[0] == 0:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


points = gen_points(WIDTH, HEIGHT)

# cam_x, cam_y = -0.745, 0.1
# zoom = 800
cam_x, cam_y = 0.0, 0.0
zoom = 0.1
loops = 125


generation_loop(window, points, (cam_x, cam_y), zoom, loops)
finished = window.copy()

# number precision (increases as zoom increases)
precision = 3 + math.ceil(math.log10(math.ceil(zoom)))

zoom_text = font.render(f"Zoom: {zoom}", True, RED)
cam_text_x = font.render(f"Center X: {round(cam_x, precision)}", True, RED)
cam_text_y = font.render(f"Center X: {round(cam_y, precision)}", True, RED)

info_text_w = max(
    cam_text_x.get_width(),
    cam_text_y.get_width(),
    zoom_text.get_width()
)
info_text_h = cam_text_x.get_height() \
     + cam_text_y.get_height() \
     + zoom_text.get_height()


info_text = pygame.Surface((info_text_w, info_text_h))
info_text.blit(zoom_text, (0, 0))
info_text.blit(cam_text_x, (0, zoom_text.get_height()))
info_text.blit(cam_text_y, (0, zoom_text.get_height() +
                            cam_text_x.get_height()))


# Main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.blit(finished, (0, 0))
    window.blit(info_text, (0, window.get_height() - info_text_h))

    mx, my = pygame.mouse.get_pos()
    mouse_pos_real = screen_coords(
        (mx, my),
        SIZE,
        zoom,
        (cam_x, cam_y)
    )
    mouse_pos_real = \
        round(mouse_pos_real[0], precision), \
        round(mouse_pos_real[1], precision)

    x_text = font.render(str(mouse_pos_real[0]), True, RED)
    y_text = font.render(str(mouse_pos_real[1]), True, RED)

    window.blit(x_text, (0, 0))
    window.blit(y_text, (0, font_size))

    pygame.display.flip()
