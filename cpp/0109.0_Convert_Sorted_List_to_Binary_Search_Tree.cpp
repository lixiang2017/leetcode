/*
Runtime: 25 ms, faster than 80.67% of C++ online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 28.5 MB, less than 47.40% of C++ online submissions for Convert Sorted List to Binary Search Tree.
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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    vector<int> arr;
    
public:
    TreeNode* constructBST(int l, int r) {
        if (l > r) {
            return nullptr;
        }
        int mid = (l + r) / 2;
        return new TreeNode(arr[mid], constructBST(l, mid - 1), constructBST(mid + 1, r));
    }
    
    TreeNode* sortedListToBST(ListNode* head) {
        while (head != nullptr) {
            arr.push_back(head->val);
            head = head->next;
        }
        return constructBST(0, arr.size() - 1);        
    }
};
