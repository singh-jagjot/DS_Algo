from typing import List


def tandem_bicycle(red: List, blue: List, fastest: bool) -> int:
    red.sort()
    if fastest:
        blue.sort(reverse=True)
    else:
        blue.sort()

    tot = 0
    for idx in range(len(red)):
        tot += max(red[idx], blue[idx])
    return tot
