import math


def get_distance(a, b):
    return math.sqrt((a.loc_w - b.loc_w) ** 2 + (a.loc_h - b.loc_h) ** 2)


def is_collision(a, b):
    distance = get_distance(a, b)
    if a.radius > distance or b.radius > distance:
        return True
    else:
        return False
