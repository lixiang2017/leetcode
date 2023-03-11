/*
Runtime: 4 ms, faster than 95.65% of C++ online submissions for Linked List Cycle II.
Memory Usage: 7.7 MB, less than 68.68% of C++ online submissions for Linked List Cycle II.
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
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head, *fast = head;
        while (true) {
            if (fast == NULL || fast->next == NULL) {
                return NULL;
            }
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                break;
            }
        }
        
        fast = head;
        while (fast != slow) {
            fast = fast->next;
            slow = slow->next;
        }
        return slow;       
    }
};



/*
o(n)算法，应该是最快的。 堆的地址从低到高，LeetCode的链表内存是顺序申请的，如果有环，head->next一定小于或等于head，哈哈哈哈哈

执行用时：4 ms, 在所有 C++ 提交中击败了98.31% 的用户
内存消耗：7.5 MB, 在所有 C++ 提交中击败了29.06% 的用户
通过测试用例：17 / 17
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
    ListNode *detectCycle(ListNode *head) {
        while (head) {
            if (!less<ListNode *>()(head, head->next)) {
                return head->next;
            }
            head = head->next;
        }
        return nullptr;    
    }
};

