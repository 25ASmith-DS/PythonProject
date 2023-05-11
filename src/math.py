
def complex_square(a, b):
    return (a*a - b*b, 2.0*a*b)


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
