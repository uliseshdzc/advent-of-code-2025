import math
from common.utils import get_input


codes = list(map(lambda c: int(('-' if c[0] == 'L' else '+') + c[1:]), get_input(day=1).split('\n')))

def first_part():
    current = 50
    dial_points = [current := (code + current) % 100 for code in codes]
    return sum(dial_point == 0 for dial_point in dial_points)

def second_part():
    current = 50
    result = 0
    for code in codes:
        div, mod = divmod(code, 100 * math.copysign(1, code))
        result += abs(div)
        if (mod + current <= 0 or mod + current >= 100) and current != 0:
            result += 1

        current = (code + current) % 100

    return int(result)

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")