/*
Runtime: 3 ms, faster than 81.58% of Java online submissions for Swapping Nodes in a Linked List.
Memory Usage: 182.8 MB, less than 31.99% of Java online submissions for Swapping Nodes in a Linked List.
*/
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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode n1 = null, n2 = null;
        for (var p=head; p != null; p = p.next) {
            if (n2 != null) {
                n2 = n2.next;
            }
            if (--k == 0) {
                n1 = p;
                n2 = head;
            }
        }
        // swap
        int tmp = n1.val;
        n1.val = n2.val;
        n2.val = tmp;
        return head;
    }
}


/*
Runtime: 4 ms, faster than 51.04% of Java online submissions for Swapping Nodes in a Linked List.
Memory Usage: 188.5 MB, less than 10.61% of Java online submissions for Swapping Nodes in a Linked List.
*/
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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode n1 = null, n2 = null;
        for (var p=head; p != null; p = p.next) {
            n2 = n2 == null ? n2: n2.next;
            if (--k == 0) {
                n1 = p;
                n2 = head;
            }
        }
        // swap
        var tmp = n1.val;
        n1.val = n2.val;
        n2.val = tmp;
        return head;
    }
}


/*
Runtime: 2 ms, faster than 100.00% of Java online submissions for Swapping Nodes in a Linked List.
Memory Usage: 178.8 MB, less than 56.73% of Java online submissions for Swapping Nodes in a Linked List.
*/
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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode n1 = null, n2 = null;
        for (ListNode p=head; p != null; p = p.next) {
            n2 = n2 == null ? n2: n2.next;
            if (--k == 0) {
                n1 = p;
                n2 = head;
            }
        }
        // swap
        int tmp = n1.val;
        n1.val = n2.val;
        n2.val = tmp;
        return head;
    }
}



