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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode ll = new ListNode(0);
        ListNode head = ll;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                ll.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                ll.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            ll = ll.next;
        }

        // Attach the remainder of the non-empty list
        ll.next = list1 != null ? list1 : list2;

        // The real head is head.next (skip the first node)
        return head.next;
    }
}