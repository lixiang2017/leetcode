'''
BFS
T: O(2N)
S: O(logN)

Runtime: 77 ms, faster than 56.40% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.6 MB, less than 46.07% of Python3 online submissions for Average of Levels in Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = [root] if root else []
        while q:
            total = sum(node.val for node in q) / len(q)
            ans.append(total)
            q = [child for node in q for child in [node.left, node.right] if child]
        return ans 



'''
执行用时：52 ms, 在所有 Python3 提交中击败了82.68% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了79.91% 的用户
通过测试用例：66 / 66
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = [root] if root else []
        while q:
            next_q = []
            s = 0
            for node in q:
                s += node.val 
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            ans.append(s / len(q))
            q = next_q
        return ans

