'''
DFS

执行用时：72 ms, 在所有 Python3 提交中击败了88.17% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了73.66% 的用户
通过测试用例：62 / 62
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        def post_order(node: TreeNode):
            if node:
                post_order(node.left)
                post_order(node.right)
                arr.append(node.val)
        post_order(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))
        def construct(lower: int, upper: int) -> TreeNode:
            if not arr or arr[-1] < lower or arr[-1] > upper:
                return None 
            v = arr.pop()
            node = TreeNode(v)
            node.right = construct(v, upper)
            node.left = construct(lower, v)
            return node 

        return construct(-inf, inf)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


