from math import prod
from common.utils import get_input


lines = get_input(day=6).splitlines()

def first_part():
    numbers_cols = zip(*[map(int, line.split()) for line in lines[:-1]])
    operations = lines[-1].split()

    return sum(
        sum(numbers) if operation == '+' else prod(numbers)
        for numbers, operation 
        in zip(numbers_cols, operations)
    )

def second_part():
    total = 0
    current = 0

    for column in zip(*lines):
        if all(c == ' ' for c in column): 
            continue

        if column[-1] != ' ':
            total += current
            operator = column[-1]
            current = 0 if column[-1] == '+' else 1

        current = eval(f"current {operator} {"".join(column[:-1])}")        

    return current + total

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")
