from typing import List

# O(nlog(n)) time | O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    time = 0
    tottime = 0
    for i in range(1, len(queries)):
        time += queries[i - 1]
        tottime += time
    return tottime


# Better solution with good logic.
# O(nlog(n)) time | O(1) space
def min_wait_time2(queries: List) -> int:
    queries.sort()
    total_waiting_time = 0
    for idx, query in enumerate(queries):
        queries_remain = len(queries) - (idx + 1)
        total_waiting_time += query * queries_remain

    return total_waiting_time


print(minimumWaitingTime([2, 3, 1, 5, 6]))
print(min_wait_time2([2, 3, 1, 5, 6]))
