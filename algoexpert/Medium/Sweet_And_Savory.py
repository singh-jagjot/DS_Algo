# O(nlog(n)) time | O(n) space
def sweetAndSavory(dishes, target):
    # Write your code here.
    sweetDishes = []
    savoryDishes = []
    for dish in dishes:
        if dish < 0:
            sweetDishes.append(dish)
        else:
            savoryDishes.append(dish)
    sweetDishes.sort(key=abs)
    savoryDishes.sort()
    bestDiff = float('inf')
    fianlDishes = [0, 0]
    sweetIdx = savoryIdx = 0
    while sweetIdx < len(sweetDishes) and savoryIdx < len(savoryDishes):
        sweetDish = sweetDishes[sweetIdx]
        savoryDish = savoryDishes[savoryIdx]
        currentCombFlavor = sweetDish + savoryDish
        if currentCombFlavor <= target:
            currentDiff = target - currentCombFlavor
            if currentDiff < bestDiff:
                bestDiff = currentDiff
                fianlDishes = [sweetDish, savoryDish]
            savoryIdx += 1
        else:
            sweetIdx += 1
    return fianlDishes
