from common.utils import get_input


banks = get_input(day=3).splitlines()

def first_part():
    return sum(
        int((first_digit := max(bank[:-1])) + max(bank[bank.index(first_digit) + 1:])) for bank in banks
    )

def second_part():
    result = 0
    for bank in banks:
        start_index = 0
        stop_index = len(bank) - 11
        digits = ""
        for _ in range(12):
            digit = max(bank[start_index:stop_index])
            start_index = bank[start_index:].index(digit) + start_index + 1
            stop_index += 1

            digits += digit
        result += int(digits)

    return result

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")