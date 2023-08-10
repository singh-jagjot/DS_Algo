# O(n) time | O(1) space
def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0
    left = 0
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1
        currentSpace = right - left - 1
        if currentSpace > maxSpace:
            maxSpace = currentSpace
            bestSeat = (left+right)//2
        left = right
    return bestSeat


def bestSeat(seats):
    # Write your code here.
    leftIdx = rightIdx = 0
    idx = 0
    space = 0
    finalSeat = -1
    while idx < len(seats):
        if seats[idx] == 0:
            leftIdx = idx
            currentSpace = 0
            while seats[idx] == 0:
                idx += 1
                currentSpace += 1
            rightIdx = idx - 1
            if currentSpace > space:
                finalSeat = (leftIdx+rightIdx)//2
                space = currentSpace

    return finalSeat
