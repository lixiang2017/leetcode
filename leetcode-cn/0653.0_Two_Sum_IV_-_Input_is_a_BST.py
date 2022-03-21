'''
inorder + two pointers
T: O(2N)
S: O(logN + N)

执行用时：880 ms, 在所有 Python3 提交中击败了5.07% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了40.50% 的用户
通过测试用例：422 / 422
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node: Optional[TreeNode]):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        nums = list(inorder(root))
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                return True
            elif s < k:
                i += 1
            else:
                j -= 1
        return False


'''
hash set + inorder
T: O(N)
S: O(N + logN)

执行用时：80 ms, 在所有 Python3 提交中击败了56.34% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了53.01% 的用户
通过测试用例：422 / 422
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal seen 
            if not node:
                return False
            if k - node.val in seen:
                return True 
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)



