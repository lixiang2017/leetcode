/*
执行用时：0 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：5.7 MB, 在所有 C 提交中击败了73.08% 的用户
通过测试用例：36 / 36
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* slow = head, * fast = head;
    while (fast != NULL && (fast->next != NULL)) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

