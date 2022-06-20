from typing import List


def min_wait_time(inp: List):
    inp.sort()
    wait_time = 0
    total = 0
    for idx in range(len(inp)):
        if idx == 0:
            continue
        wait_time += inp[idx - 1]
        total += wait_time

    return total


# Better solution with less code.


def min_wait_time2(queries: List) -> int:
    queries.sort()
    total_waiting_time = 0
    for idx, query in enumerate(queries):
        queries_remain = len(queries) - (idx + 1)
        total_waiting_time += query * queries_remain

    return total_waiting_time


print(min_wait_time([2, 3, 1, 5, 6]))
print(min_wait_time2([2, 3, 1, 5, 6]))
