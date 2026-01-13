from dataclasses import dataclass
from typing import List, Tuple, Optional

Point = Tuple[float, float]

@dataclass(frozen=True)
class Rect:
    xmin: float
    ymin: float
    xmax: float
    ymax: float


def clip_polygon_rect(polygon: List[Point], r: Rect) -> List[Point]:
    """Sutherland–Hodgman polygon clipping against an axis-aligned rectangle."""
    def clip_edge(poly: List[Point], inside_fn, intersect_fn) -> List[Point]:
        if not poly:
            return []

        out: List[Point] = []
        S = poly[-1]  # start with last vertex as "previous"
        for E in poly:
            S_in = inside_fn(S)
            E_in = inside_fn(E)

            if E_in:
                if S_in:
                    # in -> in : keep E
                    out.append(E)
                else:
                    # out -> in : add intersection, then E
                    out.append(intersect_fn(S, E))
                    out.append(E)
            else:
                if S_in:
                    # in -> out : add intersection only
                    out.append(intersect_fn(S, E))
                # out -> out : add nothing

            S = E
        return out

    def intersect_with_vertical(S: Point, E: Point, x: float) -> Point:
        x0, y0 = S
        x1, y1 = E
        if x1 == x0:
            # segment parallel to vertical line; return something stable
            return (x, y0)
        t = (x - x0) / (x1 - x0)
        return (x, y0 + t * (y1 - y0))

    def intersect_with_horizontal(S: Point, E: Point, y: float) -> Point:
        x0, y0 = S
        x1, y1 = E
        if y1 == y0:
            # segment parallel to horizontal line
            return (x0, y)
        t = (y - y0) / (y1 - y0)
        return (x0 + t * (x1 - x0), y)

    poly = polygon[:]

    # Left: x >= xmin
    poly = clip_edge(
        poly,
        inside_fn=lambda p: p[0] >= r.xmin,
        intersect_fn=lambda S, E: intersect_with_vertical(S, E, r.xmin),
    )

    # Right: x <= xmax
    poly = clip_edge(
        poly,
        inside_fn=lambda p: p[0] <= r.xmax,
        intersect_fn=lambda S, E: intersect_with_vertical(S, E, r.xmax),
    )

    # Bottom: y >= ymin
    poly = clip_edge(
        poly,
        inside_fn=lambda p: p[1] >= r.ymin,
        intersect_fn=lambda S, E: intersect_with_horizontal(S, E, r.ymin),
    )

    # Top: y <= ymax
    poly = clip_edge(
        poly,
        inside_fn=lambda p: p[1] <= r.ymax,
        intersect_fn=lambda S, E: intersect_with_horizontal(S, E, r.ymax),
    )

    return poly


if __name__ == "__main__":
    window = Rect(0, 0, 10, 10)

    poly = [(-5, 3), (5, 15), (15, 7), (6, -4)]

    clipped = clip_polygon_rect(poly, window)
    print("Original:", poly)
    print("Clipped: ", clipped)