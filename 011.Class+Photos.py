from typing import List


def classPhotos(redShirtsHeight: List, blueShirtsHeight: List) -> bool:
    redShirtsHeight.sort(reverse=True)
    blueShirtsHeight.sort(reverse=True)

    firstRowColor = 'RED' if redShirtsHeight[0] < blueShirtsHeight[0] else 'BLUE'

    for idx in range(len(redShirtsHeight)):
        if firstRowColor == 'RED':
            if redShirtsHeight[idx] >= blueShirtsHeight[idx]: return False
        else:
            if blueShirtsHeight[idx] >= redShirtsHeight[idx]: return False
    return True

