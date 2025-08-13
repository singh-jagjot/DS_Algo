public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Two pointers starting from heads of both lists
        ListNode pA = headA;
        ListNode pB = headB;

        // Move both pointers until they meet
        // If one pointer reaches end, redirect it to the other list's head
        while (pA != pB) {
            pA = (pA == null) ? headB : pA.next;
            pB = (pB == null) ? headA : pB.next;
        }

        // Either intersection node or null if no intersection
        return pA;
    }
}

// Below solution is easier to understand (Above recommended).
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Step 1: Find lengths of both lists
        int lengthA = 0, lengthB = 0;
        ListNode currA = headA, currB = headB;

        while (currA != null) {
            lengthA++;
            currA = currA.next;
        }
        while (currB != null) {
            lengthB++;
            currB = currB.next;
        }

        // Step 2: Align both pointers by skipping the extra nodes in the longer list
        ListNode longer = (lengthA > lengthB) ? headA : headB;
        ListNode shorter = (lengthA > lengthB) ? headB : headA;
        for (int i = 0; i < Math.abs(lengthA - lengthB); i++) {
            longer = longer.next;
        }

        // Step 3: Traverse both lists together until intersection is found
        while (longer != shorter) {
            longer = longer.next;
            shorter = shorter.next;
        }

        return longer; // Either intersection node or null
    }
}
