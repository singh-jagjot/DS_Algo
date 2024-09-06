class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}

        for ch in s:
            if ch not in charMap:
                charMap[ch] = 0
            charMap[ch] += 1

        for idx, ch in enumerate(s):
            if charMap[ch] == 1:
                return idx
        return -1