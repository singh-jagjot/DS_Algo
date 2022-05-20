from typing import List


def minWaitTime(inp: List):
    inp.sort()
    waitTime = 0
    total = 0
    for idx in range(len(inp)):
        if idx == 0:
            continue
        waitTime = waitTime + inp[idx - 1]
        total += waitTime

    return total

# Better solution with less code.


def minWaitTime2(queries: List) -> int:
    queries.sort()
    totalWaitingTime = 0
    for idx, query in enumerate(queries):
        queriesRemain = len(queries) - (idx + 1)
        totalWaitingTime += query*queriesRemain

    return totalWaitingTime

