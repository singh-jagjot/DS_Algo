class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def remove_duplicates(head: Node) -> Node:
    next_node = None
    current_node = head
    if current_node is None:
        return head
    while True:
        next_node = current_node.next
        if next_node is None:
            break
        if current_node.value == next_node.value:
            current_node.next = next_node.next
        else:
            current_node = next_node

    return head
