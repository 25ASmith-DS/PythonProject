import pygame

RED = (255, 0, 0)
WIDTH, HEIGHT = 800, 600
SIZE = WIDTH, HEIGHT

FONT_SIZE = 20
FONT_NAME = pygame.font.get_default_font()


def init_window():
    return pygame.display.set_mode((WIDTH, HEIGHT))


def init_font():
    return pygame.font.Font(FONT_NAME, FONT_SIZE)


def init_clock():
    return pygame.time.Clock()
