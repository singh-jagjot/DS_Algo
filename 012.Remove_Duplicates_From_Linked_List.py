class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def removeDuplicates(head: Node) -> Node:
    nextNode:Node = None
    currentNode = head
    if currentNode is None: return head
    while True:
        nextNode = currentNode.next
        if nextNode is None: break
        if currentNode.value == nextNode.value:
            currentNode.next = nextNode.next
        else:
            currentNode = nextNode

    return head