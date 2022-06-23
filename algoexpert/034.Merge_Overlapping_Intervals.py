from typing import List


# my solution O(nlog(n)) time | O(n) space
# def moi(intervals: List):
#     intervals.sort(key=lambda x: x[0])
#     merged_intervals = [[intervals[0][0],intervals[0][1]]]
#     a = b = None
#     idx = 0
#     for i in range(1, len(intervals)):
#         if merged_intervals[idx][1] >= intervals[i][0]:
#
#             a = merged_intervals[idx][0]
#             b = max(merged_intervals[idx][1], intervals[i][1])
#             merged_intervals.pop()
#             merged_intervals.append([a, b])
#         else:
#             merged_intervals.append(intervals[i])
#             idx += 1
#     return merged_intervals

# better solution O(nlog(n)) time | O(n) space
def moi(intervals: List) -> List:
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    current_interval = intervals[0]
    merged_intervals.append(current_interval)

    for interval in intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = interval
        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = interval
            merged_intervals.append(current_interval)
    return merged_intervals


print(moi([[4, 5], [1, 3], [5, 7], [0, 1]]))
