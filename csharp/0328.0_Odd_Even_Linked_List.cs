/*
Runtime: 147 ms, faster than 43.94% of C# online submissions for Odd Even Linked List.
Memory Usage: 38.3 MB, less than 52.27% of C# online submissions for Odd Even Linked List.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode OddEvenList(ListNode head) {
        var odd = new ListNode();
        var even = new ListNode();
        var o = odd;
        var e = even;
        while (head is not null) {
            o.next = head;
            o = o.next;
            head = head.next;
            if (head is not null) {
                e.next = head;
                e = e.next;
                head = head.next;
            } else {
                break;
            }
        }
        o.next = even.next;
        e.next = null;
        return odd.next;
    }
}
