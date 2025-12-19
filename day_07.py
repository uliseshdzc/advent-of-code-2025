import collections
from common.utils import get_input


lines = get_input(day=7).splitlines()
tachyons_count = {lines[0].index('S'): 1}
splits = 0

for line in lines[2::2]:
    new_tachyons_count = collections.defaultdict(int)
    splitters = [i for i, c in enumerate(line) if c == '^']

    for tachyon, count in tachyons_count.items():
        if tachyon in splitters:
            splits += 1
            new_tachyons_count[tachyon + 1] += count
            new_tachyons_count[tachyon - 1] += count
        else:
            new_tachyons_count[tachyon] += count

    tachyons_count = new_tachyons_count

def first_part():
    return splits

def second_part():
    return sum(tachyons_count.values())

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")
