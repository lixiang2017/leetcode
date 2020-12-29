'''
approach: DFS + bitwise


You are here!
Your runtime beats 90.91 % of python submissions.
You are here!
Your memory usage beats 46.75 % of python submissions.

ref:
https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solution/wei-yun-suan-ji-lu-zhuang-tai-by-derek-6-ogzn/
https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solution/wei-yun-suan-jie-fa-by-dnanki/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def dfs(record, node):
            if node:
                record ^= (1 << node.val)
                if not (node.left or node.right):  # reach leaf node
                    if bin(record).count('1') < 2:
                        self.ans += 1
                    return
                dfs(record, node.left)
                dfs(record, node.right)
        
        dfs(0, root)
        return self.ans
