def run_line_encoding(s: str) -> str:
    head = 1
    rle = []
    for i in range(1, len(s)):
        if s[i] != s[i - 1] or head == 9:
            rle.append(str(head))
            rle.append(s[i-1])
            head = 0
        head += 1
    rle.append(str(head))
    rle.append(s[len(s) - 1])
    return ''.join(rle)


print(run_line_encoding('AAAAAAAAAAAAABBCCCCDD'))
