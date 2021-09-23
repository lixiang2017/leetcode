/*
T: O(2N)
S:O(1)

执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.7 MB, 在所有 C++ 提交中击败了31.94% 的用户
通过测试用例：43 / 43
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
    int getLen(ListNode* node) {
        int l = 0;
        while (node) {
            node = node->next;
            l++;
        }
        return l;
    }
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int l = getLen(head);
        int rmn = l % k;
        l /= k;
        ListNode* p = head;
        ListNode* pre = head;
        vector<ListNode*> ans;
        while (p) {
            ans.push_back(p);
            for (int i = 0; i < l; ++i) {
                pre = p;
                p = p->next;
            }
            if (rmn) {
                rmn--;
                pre = p;
                p = p->next;
            }
            // cut
            pre->next = NULL;
        }

        int empty = k - ans.size();
        for (int i = 0; i < empty; i++) {
            ans.push_back(NULL);
        }
        return ans;
    }
};



