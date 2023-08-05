# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def middleNode(linkedList):
    slow = fast = linkedList
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def middleNode2(linkedList):
    # Write your code here.
    totatlNodes = 0
    node = linkedList
    while node != None:
        totatlNodes += 1
        node = node.next
    node = linkedList
    for _ in range(totatlNodes//2):
        node = node.next
    return node