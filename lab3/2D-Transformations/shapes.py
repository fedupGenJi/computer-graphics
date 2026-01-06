import numpy as np
import math

def create_circle(cx, cy, r, segments=100):
    points = []
    for i in range(segments):
        theta = 2 * math.pi * i / segments
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        points.append([x, y, 1])
    return np.array(points)

shapes = {
    "Triangle": np.array([
        [50, 50, 1],
        [100, 50, 1],
        [75, 100, 1]
    ]),

    "Rectangle": np.array([
        [150, 50, 1],
        [250, 50, 1],
        [250, 120, 1],
        [150, 120, 1]
    ]),

    "Line": np.array([
        [50, 200, 1],
        [200, 300, 1]
    ]),

    # "Circle": create_circle(cx=350, cy=200, r=50, segments=100)
}

def apply_transform(shape, matrix):
    return shape @ matrix.T