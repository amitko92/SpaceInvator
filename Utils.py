import math

def get_distance(a, b):
    return math.sqrt((a.loc_w - b.loc_w) ** 2 + (a.loc_h - b.loc_h) ** 2)


def is_collision(a, b):
    distance = get_distance(a, b)
    if a.radius > distance or b.radius > distance:
        return True
    else:
        return False


color_map = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (255, 0, 0),
    'gray': (128, 128, 128),
    'slate gray': (112, 124, 144)
}
