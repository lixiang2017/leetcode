'''
DFS

Runtime: 392 ms, faster than 34.97% of Python3 online submissions for Path Sum III.
Memory Usage: 35.4 MB, less than 5.93% of Python3 online submissions for Path Sum III.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        
        def dfs(node: Optional[TreeNode], sum_list) -> None:
            nonlocal ans
            if not node:
                return
            new_list = []
            for old in sum_list:
                if old + node.val == targetSum:
                    ans += 1
                new_list.append(old + node.val)
            # only node.val
            if node.val == targetSum:
                ans += 1
            new_list.append(node.val)
            dfs(node.left, new_list)
            dfs(node.right, new_list)
        
        dfs(root, [])
        return ans
    

'''
BFS
Runtime: 360 ms, faster than 36.52% of Python3 online submissions for Path Sum III.
Memory Usage: 14.9 MB, less than 97.74% of Python3 online submissions for Path Sum III.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        ans = 0
        q = deque([(root, [])])
        while q:
            node, pre_vals = q.popleft()
            next_vals = []
            for pre in pre_vals:
                if pre + node.val == targetSum:
                    ans += 1
                next_vals.append(pre + node.val)
            if node.val == targetSum:
                ans += 1
            next_vals.append(node.val)
            
            if node.left:
                q.append((node.left, next_vals))
            if node.right:
                q.append((node.right, next_vals))
                
        return ans
    

'''
BFS

Runtime: 416 ms, faster than 34.37% of Python3 online submissions for Path Sum III.
Memory Usage: 14.7 MB, less than 99.43% of Python3 online submissions for Path Sum III.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        ans = 0
        q = deque([(root, [])])
        while q:
            node, pre_vals = q.popleft()
            for i, pre in enumerate(pre_vals):
                if pre + node.val == targetSum:
                    ans += 1
                pre_vals[i] += node.val
            if node.val == targetSum:
                ans += 1
            pre_vals.append(node.val)
            
            if node.left:
                q.append((node.left, pre_vals[:]))
            if node.right:
                q.append((node.right, pre_vals[:]))
                
        return ans
    
