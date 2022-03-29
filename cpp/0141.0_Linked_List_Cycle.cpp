/*
slow and fast pointer

执行用时：8 ms, 在所有 C++ 提交中击败了93.61% 的用户
内存消耗：8 MB, 在所有 C++ 提交中击败了38.96% 的用户
通过测试用例：21 / 21
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (slow && fast) {
            slow = slow->next;
            if (fast->next) {
                fast = fast->next->next;
            } else {
                break;
            }
            if (slow == fast) return true;
        }
        return false;
    }
};



/*
slow and fast pointer

执行用时：12 ms, 在所有 C++ 提交中击败了37.82% 的用户
内存消耗：7.8 MB, 在所有 C++ 提交中击败了87.22% 的用户
通过测试用例：21 / 21
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (slow && fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};



