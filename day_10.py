from itertools import combinations
import re
import z3

from common.utils import get_input


input = get_input(day=10)

def parse_line(line):
    lights, buttons, joltage = re.match(r"\[(.*)\](.*)\{(.*)\}", line).groups()
    lights = {i for i, light in enumerate(lights) if light == '#'}
    buttons = [set(map(int, g[1:-1].split(','))) for g in re.findall(r"\(.*?\)", buttons)]
    joltage = [int(j) for j in joltage.split(',')]

    return lights, buttons, joltage    

def min_line_count(line):
    lights, buttons, _ = parse_line(line)
    for count in range(1, len(buttons) + 1):
        for possibilities in combinations(buttons, r=count):
            state = set()
            for button in possibilities:
                state ^= button # https://www.w3schools.com/python/ref_set_symmetric_difference.asp

            if state == lights:
                return count
            
def min_presses_for_joltage(line):
    _, buttons, joltages = parse_line(line)
  
    o = z3.Optimize()
    vars = z3.Ints(f"b{i}" for i in range(len(buttons)))
    [o.add(var >= 0) for var in vars]

    for i, joltage in enumerate(joltages):
        equation = sum([vars[b] for b, button in enumerate(buttons) if i in button]) 
        o.add(equation == joltage)

    o.minimize(sum(vars))
    o.check()

    return o.model().eval(sum(vars)).as_long()

print(f"Part 1: {sum(min_line_count(line) for line in input.splitlines())}")
print(f"Part 2: {sum(min_presses_for_joltage(line) for line in input.splitlines())}")
