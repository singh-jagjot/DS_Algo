# O(n) time | O(1) space
def longestPeak(array):
    # Write your code here.
    i = 1
    longestPeakLength = 0
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            left = i - 2
            right = i + 2
            while left >= 0 and array[left] < array[left + 1]:
                left -= 1
            while right < len(array) and array[right - 1] > array[right]:
                right += 1
            longestPeakLength = max(longestPeakLength, right - left - 1)
            i = right
        else:
            i += 1
    return longestPeakLength

# This one is kinda missleading as here is asked to find the longest peak for which we have
# to traverse the whole array.
# To find whether a peak exists or not there exists more efficient O(logN) algorithm using
# binary search. See answer 162 in leetcode for more details.