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

    //Improved
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.val));

        for(ListNode node: lists) if(node != null) pq.offer(node);

        ListNode dummy = new ListNode(); //Here val will be 0, defaul for int;
        ListNode tail = dummy;
        while(!pq.isEmpty()){
            var minNode = pq.poll();
            tail.next = minNode;
            tail = tail.next;

            if(minNode.next != null) pq.offer(minNode.next);
        }

        return dummy.next;
    }

    //See improved version above
    public ListNode mergeKLists(ListNode[] lists) {
        record Pair(int val, int lstIdx) implements Comparable<Pair>{
            @Override
            public int compareTo(Pair o) {
                return Integer.compare(val, o.val);
            }

        }
        Queue<Pair> pq = new PriorityQueue<>();
        for (int i = 0; i < lists.length; i++) {
            if(lists[i] != null) pq.add(new Pair(lists[i].val, i));
        }

        ListNode curr = null;

        while(!pq.isEmpty()){
            // for(var e: pq) System.out.print(e.val + ",");
            // System.out.println("\n" + pq.size());
            var pair = pq.poll();

            var newNode = new ListNode(pair.val);
            newNode.next = curr;
            curr = newNode;

            lists[pair.lstIdx] = lists[pair.lstIdx].next;
            if(lists[pair.lstIdx] != null){
                var newPair = new Pair(lists[pair.lstIdx].val, pair.lstIdx);
                pq.offer(newPair);
            }
        }

        ListNode res = null;

        while(curr != null) {
            var node = new ListNode(curr.val, res);
            res = node;
            curr = curr.next;
        }

        return res;
    }
}