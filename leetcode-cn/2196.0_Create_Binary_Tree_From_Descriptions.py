# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_node = {}
        p = {}

        def new_node(val):
            if val in val_node:
                return val_node[val]
            n = TreeNode(val)
            val_node[val] = n
            return n

        for parent, child, is_left in descriptions:
            p_node = new_node(parent)
            c_node = new_node(child)
            if is_left:
                p_node.left = c_node
            else:
                p_node.right = c_node
            p[child] = parent

        x = descriptions[0][0]
        while x in p:
            x = p[x]
        return val_node[x]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # val -> TreeNode
        root = 0
        for x, y, is_left in descriptions:
            if x not in nodes:
                nodes[x] = TreeNode(x)
                root ^= x
            if y not in nodes:
                nodes[y] = TreeNode(y)
                root ^= y
            if is_left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            root ^= y
        return nodes[root]