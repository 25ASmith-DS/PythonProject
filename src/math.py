
def screen_coords(p, size, scale, offset):
    width, height = size
    ratio = width / height

    x = (p[0] / width - 0.5) * ratio
    y = p[1] / height - 0.5
    x /= scale
    y /= scale
    x += offset[0]
    y += offset[1]

    return x, y


def complex_square(a, b):
    return (a*a - b*b, 2.0*a*b)


def cartesian_product(a, b):
    appendee = []
    for x in b:
        for y in a:
            appendee.append((x, y))
    return appendee


def inside_set(p, loops):
    a, b = p

    i = 0
    while i < loops:
        a, b = complex_square(a, b)
        a, b = a + p[0], b + p[1]
        if (abs(a) > 2.0 or abs(a) > 2.0):
            return False
        i += 1
    return True
