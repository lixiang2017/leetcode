'''
DFS, post_order

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


'''
DFS, pre_order

执行用时：72 ms, 在所有 Python3 提交中击败了83.58% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了59.37% 的用户
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
        nums = []
        def pre_order(node: TreeNode):
            if node:
                nums.append(node.val)
                pre_order(node.left)
                pre_order(node.right)
        pre_order(root)
        return ' '.join(map(str, nums))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nums = deque(map(int, data.split()))

        def construct(lower: int, upper: int) -> TreeNode:
            if not nums or nums[0] < lower or nums[0] > upper:
                return None 
            v = nums.popleft()
            node = TreeNode(v)
            node.left = construct(lower, v)
            node.right = construct(v, upper)
            return node 
     
        return construct(-inf, inf)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

'''
# environment in leetcode.cn
print('inf ', inf)
print('-inf', -inf)
print('float inf ', float('inf'))
print('float -inf', float('-inf'))
print(inf == float('inf'))
print(-inf == float('-inf'))
# output
inf  inf
-inf -inf
float inf  inf
float -inf -inf
True
True
'''



