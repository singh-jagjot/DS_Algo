from typing import List


class Node:
    def __init__(self, value) -> None:
        self.children = []
        self.value = value
    
    def addChild(self, value):
        self.children.append(Node(value))
    
    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array: List) -> List:
        array.append(self.value)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
