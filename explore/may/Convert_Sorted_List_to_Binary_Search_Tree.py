'''
approach: DFS
Time: O(N + N) = O(N)
Space: O(N + N) = O(N)

You are here!
Your runtime beats 56.85 % of python3 submissions.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def dfs(left, right):
            #
            if left > right:
                return
            
            mid = (right - left) // 2 + left
            node = TreeNode(val=nums[mid])
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            return node
         
        N = len(nums)
        return dfs(0, N - 1)
