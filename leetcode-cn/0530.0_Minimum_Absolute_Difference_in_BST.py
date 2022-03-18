'''
DFS
T: O(N)
S: O(N)

执行用时：72 ms, 在所有 Python3 提交中击败了8.00% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了27.08% 的用户
通过测试用例：188 / 188
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        ans = nums[-1] - nums[0]
        n = len(nums)
        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                ans = min(ans, abs(nums[i + 1] - nums[i]))
                
        return ans 


'''
执行用时：64 ms, 在所有 Python3 提交中击败了22.66% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了65.28% 的用户
通过测试用例：188 / 188
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans, pre_node = float('inf'), None

        def getMin(node: TreeNode):
            if not node:
                return 
            
            getMin(node.left)
            nonlocal ans, pre_node
            if pre_node:
                ans = min(ans, node.val - pre_node.val)
            pre_node = node 
            getMin(node.right)
        
        getMin(root)
        return ans 

'''
执行用时：64 ms, 在所有 Python3 提交中击败了22.66% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了66.79% 的用户
通过测试用例：188 / 188
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        from itertools import tee 
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        pre, cur = tee(inorder(root))
        next(cur, None)
        return min(b - a for a, b in zip(pre, cur))



