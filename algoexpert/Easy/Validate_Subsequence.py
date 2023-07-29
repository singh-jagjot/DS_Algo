# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
    ai = si = 0

    while ai < len(array)  and si < len(sequence):
        if sequence[si] == array[ai]:
            si +=1
        ai +=1

    return si == len(sequence)