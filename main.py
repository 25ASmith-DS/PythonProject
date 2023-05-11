import pygame
from src.image import fragment

width, height = 800, 600

points = []
for y in range(height):
    for x in range(width):
        points.append((x, y))


pygame.init()
surf = pygame.Surface((width, height))
window = pygame.display.set_mode((width, height))

window.fill((255, 0, 0))
pygame.display.flip()

for i, p in enumerate(points):
    color = fragment(p, (width, height), (0.1, 0.6209), 200.0)
    window.set_at(p, color)
    if p[0] == 0:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False




