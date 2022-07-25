'''
BFS / deque

执行用时：48 ms, 在所有 Python3 提交中击败了97.21% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了79.89% 的用户
通过测试用例：84 / 84
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = deque([root]) if root else deque()
        while self.q:
            if self.q[0].left and self.q[0].right:
                node = self.q.popleft()
                self.q.append(node.left)
                self.q.append(node.right)
            elif self.q[0].left:
                self.q.append(self.q[0].left)
                break
            else:
                break

    def insert(self, val: int) -> int:
        if not self.root:
            self.root = TreeNode(val)
            self.q.append(self.root)
            return -1
        if self.q[0].left is None:
            self.q[0].left = TreeNode(val)
            self.q.append(self.q[0].left)
            return self.q[0].val
        else:
            node = self.q.popleft()
            node.right = TreeNode(val)     
            self.q.append(node.right)   
            return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
