# O(nlog(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    tot = 0
    for idx in range(len(redShirtSpeeds)):
        tot += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
    return tot
