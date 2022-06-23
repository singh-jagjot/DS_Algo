class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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