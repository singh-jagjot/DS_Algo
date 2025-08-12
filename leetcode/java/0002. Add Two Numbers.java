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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy head to simplify edge cases (no need to handle first node separately)
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        int carry = 0; // Carry from previous addition

        // Loop until both lists are fully processed
        while (l1 != null || l2 != null) {
            // Get values from current nodes (0 if null)
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            // Sum current digits + carry
            int sum = x + y + carry;

            // Update carry for next iteration
            carry = sum / 10;

            // Create new node with the unit digit
            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            // Move to next nodes if available
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // If carry remains, append it as a new node
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }

        return dummy.next; // First node after dummy is the result
    }
}
