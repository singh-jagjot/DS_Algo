class Tree_Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def klargest(root: Tree_Node, k: int) -> int:
    # Iterative solution using a Stack with O(N) time and O(N) space complexity
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.value
        curr = curr.left


def klargest2(root: Tree_Node, k: int) -> int:
    # Recursive solution O(N) time | O(N) space
    arr = []

    def reverseInorder(root):
        if not root or len(arr) == k:
            return None
        reverseInorder(root.right)
        arr.append(root.value)
        reverseInorder(root.left)

    reverseInorder(root)
    return arr[k - 1]


class Tree_Info:
    # O(h + k) time | O(h) space

    def __init__(self, nodes_visited, latest_visited_node) -> None:
        self.nodes_visited = nodes_visited
        self.latest_visited_node = latest_visited_node


def klargest3(root: Tree_Node, k):
    def reverseInorder(root: Tree_Node, k, tree_info: Tree_Info):
        if root is None or tree_info.nodes_visited >= k:
            return
        reverseInorder(root.right, k, tree_info)
        if tree_info.nodes_visited < k:
            tree_info.nodes_visited += 1
            tree_info.latest_visited_node = root.value
            reverseInorder(root.left, k, tree_info)
    info = Tree_Info(0, -1)
    reverseInorder(root, k, info)
    return info.latest_visited_node
