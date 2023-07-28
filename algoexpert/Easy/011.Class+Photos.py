from typing import List


def class_photos(red_shirts_height: List, blue_shirts_height: List) -> bool:
    red_shirts_height.sort(reverse=True)
    blue_shirts_height.sort(reverse=True)

    first_row_color = 'RED' if red_shirts_height[0] < blue_shirts_height[0] else 'BLUE'

    for idx in range(len(red_shirts_height)):
        if first_row_color == 'RED':
            if red_shirts_height[idx] >= blue_shirts_height[idx]:
                return False
        else:
            if blue_shirts_height[idx] >= red_shirts_height[idx]:
                return False
    return True
