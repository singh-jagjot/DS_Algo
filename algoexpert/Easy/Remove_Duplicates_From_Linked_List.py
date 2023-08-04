class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# O(n) time | O(1) Space
def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currentNode = linkedList
    while currentNode != None:
        nextNode = currentNode.next
        while nextNode != None and currentNode.value == nextNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode

    return linkedList

def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    next_node = None
    current_node = linkedList
    if current_node is None:
        return linkedList
    while True:
        next_node = current_node.next
        if next_node is None:
            break
        if current_node.value == next_node.value:
            current_node.next = next_node.next
        else:
            current_node = next_node

    return linkedList

