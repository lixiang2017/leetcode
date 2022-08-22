'''
simulation

执行用时：36 ms, 在所有 Python3 提交中击败了74.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了76.00% 的用户
通过测试用例：73 / 73
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def height(node, h):
            if not node:
                return 0
            h1 = height(node.left, h + 1)
            h2 = height(node.right, h + 1)
            return max(h1, h2) + 1
        
        H = height(root, 0)
        m, n = H, (1 << H) - 1
        res = [[''] * n for _ in range(m)]
        # (node, height, r, c)
        q = deque([(root, 0, 0, (n - 1) // 2)])
        while q:
            node, h, r, c = q.popleft()
            res[r][c] = str(node.val)
            if node.left:
                q.append((node.left, h + 1, r + 1, c - (1 << (H - r - 2))))
            if node.right:
                q.append((node.right, h + 1, r + 1, c + (1 << (H - r - 2))))
        return res 
        

'''
height, r, c follows the question

执行用时：28 ms, 在所有 Python3 提交中击败了95.33% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了72.00% 的用户
通过测试用例：73 / 73
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def height(node, h):
            if not node:
                return 0
            h1 = height(node.left, h + 1)
            h2 = height(node.right, h + 1)
            return max(h1, h2) + 1
        
        H = height(root, 0) - 1
        m, n = H + 1, (1 << (H + 1)) - 1
        res = [[''] * n for _ in range(m)]
        # (node, height, r, c)
        q = deque([(root, 0, 0, (n - 1) // 2)])
        while q:
            node, h, r, c = q.popleft()
            res[r][c] = str(node.val)
            if node.left:
                q.append((node.left, h + 1, r + 1, c - (1 << (H - r - 1))))
            if node.right:
                q.append((node.right, h + 1, r + 1, c + (1 << (H - r - 1))))
        return res 
        

