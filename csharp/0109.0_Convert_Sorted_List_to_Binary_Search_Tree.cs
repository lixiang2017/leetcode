/*
DFS

Runtime: 91 ms, faster than 50.98% of C# online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 42 MB, less than 9.80% of C# online submissions for Convert Sorted List to Binary Search Tree.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public List<int> arr = new List<int>();
    
    public TreeNode constructBST(int l, int r) {
        if (l > r) {
            return null;
        }
        int mid = (l + r) / 2;
        return new TreeNode(arr[mid], constructBST(l, mid - 1), constructBST(mid + 1, r));
    }
    
    public TreeNode SortedListToBST(ListNode head) {
        while (head != null) {
            arr.Add(head.val);
            head = head.next;
        }
        return constructBST(0, arr.Count - 1);        
    }
}
