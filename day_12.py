import re

from common.utils import get_input


def gifts_fit(region):
    x, y, *gifts = list(map(int, re.findall(r"\d+", region)))
    return (x // 3) * (y // 3) >= sum(gifts)

print(
    f"Part 1: {sum([gifts_fit(region) for region in get_input(day=12).split('\n\n')[-1].splitlines()])}"
)
