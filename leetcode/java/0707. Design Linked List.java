// Doubly Linked List Implementation
// size tracks number of nodes
// getNode(index) optimizes traversal from head or tail
// addAtHead/addAtTail handle empty list as a special case
// addAtIndex and deleteAtIndex rely on getNode()
// deleteAtIndex clears node references to help GC

class MyLinkedList {

    private static class Node {
        int val;
        Node next;
        Node prev;

        Node(int val, Node next, Node prev) {
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }

    Node head;
    Node tail;
    int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    public int get(int index) {
        Node node = getNode(index);
        return node == null ? -1 : node.val;
    }

    public void addAtHead(int val) {
        if (size == 0) {
            head = tail = new Node(val, null, null);
        } else {
            head = new Node(val, head, null);
            head.next.prev = head;
        }
        size++;
    }

    public void addAtTail(int val) {
        if (size == 0) {
            head = tail = new Node(val, null, null);
        } else {
            tail = new Node(val, null, tail);
            tail.prev.next = tail;
        }
        size++;
    }

    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        if (index == 0) addAtHead(val);
        else if (index == size) addAtTail(val);
        else {
            Node node = getNode(index);
            Node prev = node.prev;
            Node newNode = new Node(val, node, prev);
            prev.next = newNode;
            node.prev = newNode;
            size++;
        }
    }

    public void deleteAtIndex(int index) {
        Node node = getNode(index);
        if (node == null) return;

        if (size == 1) {
            head = tail = null;
        } else if (node == head) {
            head = node.next;
            head.prev = null;
        } else if (node == tail) {
            tail = node.prev;
            tail.next = null;
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
        // Help GC
        node.next = null;
        node.prev = null;
        size--;
    }

    private Node getNode(int index) {
        if (index < 0 || index >= size) return null;
        Node curr;

        if (index < (size >> 1)) {
            curr = head;
            for (int i = 0; i < index; i++) curr = curr.next;
        } else {
            curr = tail;
            for (int i = size - 1; i > index; i--) curr = curr.prev;
        }
        return curr;
    }

    public void printHead() {
        if (head != null) {
            System.out.println("H: " + head.val);
        } else {
            System.out.println("H: null");
        }
    }

    public void printTail() {
        if (tail != null) {
            System.out.println("T: " + tail.val);
        } else {
            System.out.println("T: null");
        }
    }

    public void printLL() {
        Node node = head;
        while (node != null) {
            System.out.print(node.val + " -> ");
            node = node.next;
        }
        System.out.println("null");

        node = tail;
        System.out.print("null");
        while (node != null) {
            System.out.print(" <- " + node.val);
            node = node.prev;
        }
        System.out.println();
        System.out.println("Size: " + size);
    }
}
