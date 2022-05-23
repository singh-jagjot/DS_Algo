from typing import List


def generateDocument(characters: List, document: List) -> bool:
    charMap = {}

    for ch in characters:
        if ch not in charMap:
            charMap[ch] = 0
        charMap[ch] += 1

    for ch in document:
        if ch not in charMap or charMap[ch] == 0:
            return False
        charMap[ch] -= 1
    return True
