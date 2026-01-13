from dataclasses import dataclass
from typing import Optional, Tuple

INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000


@dataclass(frozen=True)
class Rect:
    xmin: float
    ymin: float
    xmax: float
    ymax: float


def _compute_outcode(x: float, y: float, r: Rect) -> int:
    code = INSIDE
    if x < r.xmin:
        code |= LEFT
    elif x > r.xmax:
        code |= RIGHT
    if y < r.ymin:
        code |= BOTTOM
    elif y > r.ymax:
        code |= TOP
    return code


def cohen_sutherland_clip(
    x0: float, y0: float, x1: float, y1: float, r: Rect
) -> Optional[Tuple[float, float, float, float]]:
    """
    Returns the clipped line segment (x0,y0,x1,y1) inside rectangle r,
    or None if the segment lies completely outside.
    """
    out0 = _compute_outcode(x0, y0, r)
    out1 = _compute_outcode(x1, y1, r)

    while True:
        # Trivial accept: both endpoints inside
        if (out0 | out1) == 0:
            return (x0, y0, x1, y1)

        # Trivial reject: both endpoints share an outside zone
        if (out0 & out1) != 0:
            return None

        # Choose an endpoint that is outside
        out_out = out0 if out0 != 0 else out1

        # Find intersection with a window edge
        if out_out & TOP:
            # y = ymax
            if y1 == y0:
                return None  
            x = x0 + (x1 - x0) * (r.ymax - y0) / (y1 - y0)
            y = r.ymax

        elif out_out & BOTTOM:
            # y = ymin
            if y1 == y0:
                return None
            x = x0 + (x1 - x0) * (r.ymin - y0) / (y1 - y0)
            y = r.ymin

        elif out_out & RIGHT:
            # x = xmax
            if x1 == x0:
                return None  # vertical line outside; should rarely reach here
            y = y0 + (y1 - y0) * (r.xmax - x0) / (x1 - x0)
            x = r.xmax

        else:  # LEFT
            # x = xmin
            if x1 == x0:
                return None
            y = y0 + (y1 - y0) * (r.xmin - x0) / (x1 - x0)
            x = r.xmin

        # Replace the outside endpoint with intersection point, update outcode
        if out_out == out0:
            x0, y0 = x, y
            out0 = _compute_outcode(x0, y0, r)
        else:
            x1, y1 = x, y
            out1 = _compute_outcode(x1, y1, r)



if __name__ == "__main__":
    window = Rect(xmin=10, ymin=10, xmax=150, ymax=100)

    tests = [
        (0, 120, 130, 5)
    ]

    for seg in tests:
        clipped = cohen_sutherland_clip(*seg, window)
        print(f"{seg} -> {clipped}")