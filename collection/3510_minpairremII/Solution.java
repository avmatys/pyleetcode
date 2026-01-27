import java.util.*;

class Node {
    long val;
    int idx;
    Node next;
    Node prev;

    public Node(long val, int idx) {
        this.val = val;
        this.idx = idx;
        this.next = null;
        this.prev = null;
    }
}

class DoubleLinkedList implements Iterable<Node> {
    Node head = null;
    Node tail = null;
    int currIdx = 0;

    public Node add(long val) {
        Node node = new Node(val, currIdx++);
        if (head == null) {
            head = tail = node;
        } else {
            node.prev = tail;
            tail.next = node;
            tail = node;
        }
        return node;
    }

    public void mergeNext(Node node) {
        if (node.next == null) 
            return;
        Node tmp = node.next;
        node.val += node.next.val;
        node.next = node.next.next;
        if (node.next != null) {
            node.next.prev = node;
        } else {
            tail = node;
        }
        tmp.next = null;
        tmp.prev = null;
    }

    @Override
    public Iterator<Node> iterator() {
        return new Iterator<Node>() {
            Node curr = head;
            @Override
            public boolean hasNext() {
                return curr != null;
            }
            @Override
            public Node next() {
                Node temp = curr;
                curr = curr.next;
                return temp;
            }
        };
    }
}

class Entry implements Comparable<Entry> {
    Node node1;
    Node node2;
    long nodeSum;

    public Entry(Node node1, Node node2) {
        this.node1 = node1;
        this.node2 = node2;
        this.nodeSum = node1.val + node2.val;
    }

    @Override
    public int compareTo(Entry other) {
        if (this.nodeSum != other.nodeSum) {
            return Long.compare(this.nodeSum, other.nodeSum);
        }
        return Integer.compare(this.node1.idx, other.node1.idx);
    }
}

class Solution {

    private int delta(Node n1, Node n2) {
        return n1 != null && n2 != null && n1.val > n2.val ? 1 : 0; 
    }

    public int minimumPairRemoval(int[] nums) {
        DoubleLinkedList nodeList = new DoubleLinkedList();
        for (int i = 0; i < nums.length; i++) 
            nodeList.add((long) nums[i]);

        PriorityQueue<Entry> pq = new PriorityQueue<>();
        int issues = 0;
        for (Node node : nodeList) {
            if (node.next == null) 
                break;
            pq.offer(new Entry(node, node.next));
            issues += delta(node, node.next);
        }

        int count = 0;
        while (issues != 0) {
            Entry min = null;
            while (!pq.isEmpty() && min == null) {
                Entry top = pq.poll();
                Node n1 = top.node1, n2 = top.node2;
                if (n1.next != n2 || n1.val + n2.val != top.nodeSum) 
                    continue;
                min = top;
            }
            if (min == null) 
                return -1;

            Node n1 = min.node1, n2 = min.node2;
            issues -= delta(n1.prev, n1) + delta(n1, n2) + delta(n2, n2.next);
            nodeList.mergeNext(n1);
            issues += delta(n1.prev, n1) + delta(n1, n1.next);
            count++;
           
            if (n1.prev != null) 
                pq.offer(new Entry(n1.prev, n1));
            if (n1.next != null) 
                pq.offer(new Entry(n1, n1.next));
        }
        return count;
    }
}
