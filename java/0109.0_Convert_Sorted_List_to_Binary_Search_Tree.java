/*
DFS

Runtime: 1 ms, faster than 40.56% of Java online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 44.2 MB, less than 13.81% of Java online submissions for Convert Sorted List to Binary Search Tree.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> arr = new ArrayList<Integer>();
    
    public TreeNode constructBST(int l, int r) {
        if (l > r) {
            return null;
        }
        int mid = (l + r) / 2;
        TreeNode node = new TreeNode(arr.get(mid));
        node.left = constructBST(l, mid - 1);
        node.right = constructBST(mid + 1, r);
        return node;
    }
    
    public TreeNode sortedListToBST(ListNode head) {    
        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }
        return constructBST(0, arr.size() - 1);
    }
}


/*
DSF

Runtime: 1 ms, faster than 40.56% of Java online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 44.1 MB, less than 15.03% of Java online submissions for Convert Sorted List to Binary Search Tree.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> arr = new ArrayList<Integer>();
    
    public TreeNode constructBST(int l, int r) {
        if (l > r) {
            return null;
        }
        int mid = (l + r) / 2;
        return new TreeNode(arr.get(mid), constructBST(l, mid - 1), constructBST(mid + 1, r));
    }
    
    public TreeNode sortedListToBST(ListNode head) {    
        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }
        return constructBST(0, arr.size() - 1);
    }
}

