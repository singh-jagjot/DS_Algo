class Solution {
    public int getDecimalValue(ListNode head) {
        StringBuilder str = new StringBuilder();

        ListNode node = head;

        while (node != null) {
            str.append(node.val);
            node = node.next;
        }
        
        return Integer.parseInt(str.toString(), 2);
    }
}