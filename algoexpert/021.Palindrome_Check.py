def is_palindrome(s: str) -> bool:
    left_idx = 0
    right_idx = len(s) - 1

    while left_idx < right_idx:
        if s[left_idx] != s[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True
