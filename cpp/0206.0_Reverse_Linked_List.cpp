/*
iteration

执行用时：4 ms, 在所有 C++ 提交中击败了94.50% 的用户
内存消耗：8.1 MB, 在所有 C++ 提交中击败了53.96% 的用户
通过测试用例：28 / 28
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
    ListNode* reverseList(ListNode* head) {
        ListNode* another = nullptr, *node = head;
        while (node) {
            ListNode* next_part = node->next;
            node->next = another;
            another = node;
            node = next_part;
        }
        return another;
    }
};


/*
recursion

执行用时：4 ms, 在所有 C++ 提交中击败了94.50% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了6.89% 的用户
通过测试用例：28 / 28
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
    ListNode* reverseList(ListNode* head) {
        if (!head or !head->next) {
            return head;
        }
        ListNode* tail = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return tail;
    }
};

