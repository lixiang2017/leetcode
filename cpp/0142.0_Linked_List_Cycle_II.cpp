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
