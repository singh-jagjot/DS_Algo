# O(nlog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x:x[0])
    newIntervals = [intervals[0]]
    currentInterval = intervals[0]

    for nextInterval in intervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            newIntervals.append(currentInterval)

    return newIntervals