from collections import Counter
import math

from common.utils import get_input

# Kruskal's algorithm
# https://www.geeksforgeeks.org/dsa/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

# DSU
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure

def parse_input(input):
    boxes = [tuple(map(int, line.split(','))) for line in input.splitlines()]
    links = [(i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes))]
    links.sort(key=lambda box: math.hypot(*[a - b for a, b in zip(boxes[box[0]], boxes[box[1]])]))
    parent = list(range(len(boxes)))

    return boxes, links, parent

def find(x, parent):
    if parent[x] == x: return x
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    parent[find(a, parent)] = find(b, parent)

input = get_input(day=8)

def first_part():
    boxes, links, parent = parse_input(input)

    [union(a, b, parent) for a, b in links[:1000]]
        
    sizes_counter = Counter(find(box, parent) for box in range(len(boxes)))
    sizes = sorted(sizes_counter.values(), reverse=True)

    return math.prod(sizes[:3])

def second_part():
    boxes, links, parent = parse_input(input)

    parent = list(range(len(boxes)))
    circuits = len(boxes)

    for a, b in links:
        if find(a, parent) == find(b, parent): continue
        union(a, b, parent)
        circuits -= 1
        if circuits == 1:
            return boxes[a][0] * boxes[b][0]

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")
