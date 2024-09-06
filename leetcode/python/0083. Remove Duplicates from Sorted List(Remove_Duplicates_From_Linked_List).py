# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = None
        currentNode = head
        if currentNode is None: return head
        while True:
            nextNode = currentNode.next
            if nextNode is None: break
            if currentNode.val == nextNode.val:
                currentNode.next = nextNode.next
            else:
                currentNode = nextNode

        return head