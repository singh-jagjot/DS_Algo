/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Two-pointer approach: `fast` moves n steps ahead of `slow`
        ListNode slow = head, fast = head;

        // Move fast pointer n steps forward
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        // If fast is null here, it means we are removing the head node
        if (fast == null) {
            return head.next; // Simply skip the head
        }

        // Move both pointers until fast reaches the last node
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // `slow` is now just before the node to remove
        ListNode nodeToDelete = slow.next;
        slow.next = slow.next.next; // Skip the node
        nodeToDelete.next = null;   // Help GC (optional)

        return head;
    }
}
