'''
Success
Details
Runtime: 60 ms, faster than 6.92% of Python online submissions for Path Sum.
Memory Usage: 17 MB, less than 54.26% of Python online submissions for Path Sum.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum

        def dfs(node, current_sum):     
            if not node:
                return False
            print 'node.val: ', node.val, 'current_sum:', current_sum, 'sum: ',sum
            current_sum += node.val  #  !!!
            if not node.left and not node.right and current_sum == sum:
                return True
            
            l = r = False
            l = dfs(node.left, current_sum)
            r = dfs(node.right, current_sum)
            return l or r
            
        return dfs(root, 0) 


'''
BFS
T: O(N)
S: O(logN)

Runtime: 87 ms, faster than 30.82% of Python3 online submissions for Path Sum.
Memory Usage: 15.3 MB, less than 16.13% of Python3 online submissions for Path Sum.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = deque([(root, root.val)]) if root else []
        while q:
            node, _sum = q.popleft()
            if not node.left and not node.right and _sum == targetSum:
                return True 
            if node.left:
                q.append((node.left, _sum + node.left.val))
            if node.right:
                q.append((node.right, _sum + node.right.val))
        return False 


'''
DFS

Runtime: 46 ms, faster than 92.09% of Python3 online submissions for Path Sum.
Memory Usage: 14.9 MB, less than 91.98% of Python3 online submissions for Path Sum.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right and cur_sum == targetSum:
                return True
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        
        return dfs(root, 0)
