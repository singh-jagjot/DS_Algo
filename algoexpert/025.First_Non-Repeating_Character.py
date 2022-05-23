# O(n) time | O(1) space (as we have only 26 letters in english alphabet)
def fnrc(string: str) -> str:
    charMap = {}

    for ch in string:
        if ch not in charMap:
            charMap[ch] = 0
        charMap[ch] += 1

    for idx, ch in enumerate(string):
        if charMap[ch] == 1:
            return idx
    return -1


print(fnrc('abcdcaf'))
