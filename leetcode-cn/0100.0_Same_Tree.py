'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了11.73% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了25.24% 的用户
通过测试用例：60 / 60
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (not p and q) or (p and q and p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
BFS

执行用时：44 ms, 在所有 Python3 提交中击败了11.73% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了49.60% 的用户
通过测试用例：60 / 60
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        que = deque([(p, q)])
        while que:
            pp, qq = que.popleft()
            if not pp and not qq:
                continue
            if (pp and not qq) or (not pp and qq) or (pp and qq and pp.val != qq.val):
                return False 
            if (pp.left or qq.left):
                que.append((pp.left, qq.left))
            if (pp.right or qq.right):
                que.append((pp.right, qq.right))
        return True


