/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：6.8 MB, 在所有 C++ 提交中击败了86.91% 的用户
通过测试用例：36 / 36
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head, * fast = head;
        while (fast != NULL && (fast->next != NULL)) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
