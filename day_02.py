from common.utils import get_input


ranges = [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in get_input(day=2).split(',')]

def first_part():
    def is_invalid(value: int):
        s = str(value)
        index = int(len(s) / 2)
        return s[0:index] == s[index:]
    
    return sum(value for r in ranges for value in r if is_invalid(value))


def second_part():
    def is_invalid(value: int):
        s = str(value)
        for times in range(2, len(s) + 1):
            if s[:len(s) // times] * times == s:
                return True
        
        return False
    
    return sum(value for r in ranges for value in r if is_invalid(value))

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")