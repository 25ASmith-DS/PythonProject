import pygame
import math
from src.image import create_info_text, render_fractal
from src.math import screen_coords
from src.init import SIZE, RED, FONT_SIZE, init_font, \
        init_window, WIDTH, HEIGHT, init_clock

pygame.init()
window = init_window()
font = init_font()
clock = init_clock()

window.fill(RED)

cam_x, cam_y = 0.0, 0.0
zoom = 0.1
loops = 125


def gen_points(w, h):
    points = []
    for y in range(h):
        for x in range(w):
            points.append((x, y))
    return points


points = gen_points(WIDTH, HEIGHT)

while True:
    render_fractal(window, points, (cam_x, cam_y), zoom, loops)
    finished = window.copy()

    # number precision (increases as zoom increases)
    precision = 3 + math.ceil(math.log10(math.ceil(zoom)))

    info_text = create_info_text(font, (cam_x, cam_y), zoom, precision)

    reset = False
    # Main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                reset = True

        window.blit(finished, (0, 0))
        window.blit(info_text, (0, 0))

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
        window.blit(y_text, (0, FONT_SIZE))

        pygame.display.flip()

        if reset:
            window.fill(RED)
            pygame.display.flip()
            cam_x, cam_y = mouse_pos_real
            zoom = zoom * 10
            break
        clock.tick(15)
