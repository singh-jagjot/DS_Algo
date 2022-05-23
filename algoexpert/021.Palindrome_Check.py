def isPalindrome(s: str) -> bool:
    leftIdx = 0
    rightIdx = len(s) - 1

    while leftIdx < rightIdx:
        if s[leftIdx] != s[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
