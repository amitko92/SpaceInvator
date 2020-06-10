import math


def get_distance(a, b):
    return math.sqrt((a.loc_w - b.loc_w) ** 2 + (a.loc_h - b.loc_h) ** 2)


color_map = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (255, 0, 0),
    'gray': (128, 128, 128),
    'slate gray': (112, 124, 144)
}
