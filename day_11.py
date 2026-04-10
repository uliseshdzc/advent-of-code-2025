from functools import cache

from common.utils import get_input


input = get_input(day=11)
devices = {line.split(' ')[0][:-1]: line.split(' ')[1:] for line in input.splitlines()}

@cache
def dfs(start, end):
    if start == end: return 1
    return sum(dfs(new, end) for new in devices.get(start, []))

print(f"Part 1: {dfs("you", "out")}")
print(f"Part 2: {
    dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out") + \
    dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")
}")
