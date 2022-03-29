/*
执行用时：35 ms, 在所有 Java 提交中击败了6.00% 的用户
内存消耗：57.7 MB, 在所有 Java 提交中击败了26.63% 的用户
通过测试用例：86 / 86
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
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack = new Stack<Integer>();
        ListNode cur = head;
        while (cur != null) {
            stack.push(cur.val);
            cur = cur.next;
        }
        while (head != null) {
            if (stack.pop() != head.val)
                return false;
            head = head.next;
        }
        return true;
    }
}
