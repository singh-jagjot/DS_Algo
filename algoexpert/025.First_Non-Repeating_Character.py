# O(n) time | O(1) space (as we have only 26 letters in english alphabet)
def fnrc(string: str) -> int:
    char_map = {}

    for ch in string:
        if ch not in char_map:
            char_map[ch] = 0
        char_map[ch] += 1

    for idx, ch in enumerate(string):
        if char_map[ch] == 1:
            return idx
    return -1


print(fnrc('abcdcaf'))
