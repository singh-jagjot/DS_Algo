def minDiff(root, key):
    currentClosestDiff = abs(key - root.data)
    currentNode = root
    while True:
        if key < currentNode.data:
            if currentNode.left is not None:
                currentNode = currentNode.left
                diff = abs(key - currentNode.data)
                if diff < currentClosestDiff:
                    currentClosestDiff = diff
            else:
                break
        elif key > currentNode.data:
            if currentNode.right is not None:
                currentNode = currentNode.right
                diff = abs(key - currentNode.data)
                if diff < currentClosestDiff:
                    currentClosestDiff = diff
            else:
                return currentClosestDiff
        else:
            break
    return currentClosestDiff

#Better solution with less code but same complexity
def findClosestValueInBst(tree, target):
    currentNode = tree
    closest = float('inf')
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

#Recursive Solution
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest