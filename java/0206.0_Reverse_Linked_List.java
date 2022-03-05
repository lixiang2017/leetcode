/*
iteration

执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：41.1 MB, 在所有 Java 提交中击败了24.23% 的用户
通过测试用例：28 / 28
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
    public ListNode reverseList(ListNode head) {
        ListNode another = null, node = head;
        while (node != null) {
            ListNode next_part = node.next;
            node.next = another;
            another = node;
            // move to next part
            node = next_part;
        }
        return another;
    }
}


/*
recursion

执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：41.3 MB, 在所有 Java 提交中击败了8.97% 的用户
通过测试用例：28 / 28
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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode tail = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return tail;
    }
}
