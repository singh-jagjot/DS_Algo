from typing import List


def generate_document(characters: List, document: List) -> bool:
    char_map = {}

    for ch in characters:
        if ch not in char_map:
            char_map[ch] = 0
        char_map[ch] += 1

    for ch in document:
        if ch not in char_map or char_map[ch] == 0:
            return False
        char_map[ch] -= 1
    return True
