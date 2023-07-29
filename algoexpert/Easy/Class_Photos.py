# O(nlog(n)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    backRow = 'r' if redShirtHeights[0] > blueShirtHeights[0] else 'b'

    for i in range(len(redShirtHeights)):
        if backRow == 'r':
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
            
    return True
