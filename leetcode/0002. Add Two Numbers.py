# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        place = 1
        res = 0
        while l1 != None or l2 != None:
            if l1 is None:
                s1 = 0
            else:
                s1 = l1.val * place
                l1 = l1.next
            
            if l2 is None:
                s2 = 0
            else:
                s2 = l2.val * place
                l2 = l2.next
            
            res += (s1 + s2)
            place *= 10
            
        res = str(res)
        node = None
        root = None
        for d in reversed(res):
            newnode = ListNode(d)
            if not node:
                node = newnode
                root = node
            else:
                node.next = newnode
                node = newnode
        return root
