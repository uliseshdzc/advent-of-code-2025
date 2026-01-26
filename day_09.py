from common.utils import get_input
from shapely import Polygon, box


red_tiles = [tuple(map(int, line.split(','))) for line in get_input(day=9).splitlines()]
possibilities = [(x1, y1, x2, y2) for i, (x1, y1) in enumerate(red_tiles) for x2, y2 in red_tiles[i:]]

def area(points):
    x1, y1, x2, y2 = points
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def first_part():
    return max(area(points) for points in possibilities)

def second_part():
    polygon = Polygon(red_tiles)
    return max(
        area(points) for points in possibilities
        if polygon.contains(box(*points))
    )

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")
