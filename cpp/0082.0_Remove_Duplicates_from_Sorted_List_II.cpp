/*
执行用时：16 ms, 在所有 C++ 提交中击败了20.70% 的用户
内存消耗：11.5 MB, 在所有 C++ 提交中击败了5.00% 的用户
通过测试用例：166 / 166
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
    ListNode* deleteDuplicates(ListNode* head) {
        map<int, int> val2cnt;
        ListNode *p = head;
        while (p != nullptr) {
            val2cnt[p->val] += 1;
            p = p->next;
        }
        ListNode *L = new ListNode;
        ListNode *pt = L;
        for (auto &&it: val2cnt) {
            if (it.second == 1) {
                ListNode *t = new ListNode(it.first);
                pt->next = t;
                pt = pt->next;
            }
        }
        return L->next;
    }
};
