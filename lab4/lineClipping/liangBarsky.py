from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class Rect:
    xmin: float
    ymin: float
    xmax: float
    ymax: float

def liang_barsky_clip(
    x0: float, y0: float, x1: float, y1: float, r: Rect
) -> Optional[Tuple[float, float, float, float]]:
    """
    Liang–Barsky line clipping for axis-aligned rectangular window.
    Returns (cx0, cy0, cx1, cy1) if visible, else None.
    """
    dx = x1 - x0
    dy = y1 - y0

    # Parameter interval for visible portion
    t_enter = 0.0
    t_leave = 1.0

    # Each boundary contributes one (p, q)
    constraints = [
        (-dx, x0 - r.xmin),  # left:   x >= xmin
        ( dx, r.xmax - x0),  # right:  x <= xmax
        (-dy, y0 - r.ymin),  # bottom: y >= ymin
        ( dy, r.ymax - y0),  # top:    y <= ymax
    ]

    for p, q in constraints:
        if p == 0:
            # Line is parallel to this boundary
            if q < 0:
                return None  # outside -> reject
            else:
                continue     # inside wrt this boundary -> no effect

        t = q / p

        if p < 0:
            # Entering
            if t > t_enter:
                t_enter = t
        else:
            # Leaving
            if t < t_leave:
                t_leave = t

        # If interval becomes empty -> reject
        if t_enter > t_leave:
            return None

    cx0 = x0 + t_enter * dx
    cy0 = y0 + t_enter * dy
    cx1 = x0 + t_leave * dx
    cy1 = y0 + t_leave * dy

    return (cx0, cy0, cx1, cy1)


if __name__ == "__main__":
    window = Rect(xmin=0, ymin=0, xmax=10, ymax=10)

    tests = [
        (-5,3,15,9)
    ]

    for seg in tests:
        clipped = liang_barsky_clip(*seg, window)
        print(f"{seg} -> {clipped}")