from common.utils import get_input


ranges, ingredients = get_input(day=5).split('\n\n')
ranges = [tuple(map(int, r.split('-'))) for r in ranges.splitlines()]
ingredients = list(map(int, ingredients.splitlines()))

def first_part():
    return len(set(ingredient for a, b in ranges for ingredient in ingredients if a <= ingredient <= b))

def second_part():
    ranges.sort()
    count = 0
    last_a, last_b = ranges[0]
    
    for a, b in ranges[1:]:
        if last_b < a:
            count += last_b - last_a + 1
            last_a, last_b = a, b
        else:
            last_a, last_b = last_a, max(last_b, b)

    return count + last_b - last_a + 1

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")
