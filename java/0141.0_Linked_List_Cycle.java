/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：42.9 MB, 在所有 Java 提交中击败了5.14% 的用户
通过测试用例：21 / 21
*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (true) {
            try {
                slow = slow.next;
                fast = fast.next.next;
            } catch (Exception e) {
                return false;
            }
            if (slow == fast)
                return true;
        }      
    }
}
