'''
approach: BFS, only one pass
Time: O(N), where N is the number of nodes.
Space: O(W), where W is the width of the given binary tree.

You are here!
Your runtime beats 34.15 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        q = [(root, 1)]
        current_sum = 0
        current_level = 1
        
        while q:
            # node, level = q.pop()  # will be wrong, will pop from the tail
            node, level = q.pop(0)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            
            if current_level == level:
                current_sum += node.val
            else:
                current_sum = node.val
                current_level = level
                
        return current_sum

'''
Run Code Status: Invalid Testcase
×
Run Code Result:
Your input
[1,2,3,4,5,null,6,7,null,null,null,null,8]
[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
[1]
[]   # Invalid Testcase
Your answer
expected 'root' to have 1 <= size <= 10000 but got 0
'''

'''
approach: BFS
You are here!
Your runtime beats 92.62 % of python submissions.
You are here!
Your memory usage beats 78.14 % of python submissions.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([root])
        ans = 0
        while q:
            n = len(q)
            ans = 0
            for i in range(n):
                node = q.popleft()
                ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
    



'''
approach: BFS

You are here!
Your runtime beats 84.15 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        prev = None
        
        while queue:
            prev = queue
            queue = [kid for node in queue for kid in (node.left, node.right) if kid is not None]
        
        val = 0
        for node in prev:
            val += node.val
        return val


'''
You are here!
Your runtime beats 60.66 % of python submissions.
You are here!
Your memory usage beats 55.19 % of python submissions.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        ans = 0
        while q:
            ans = sum(node.val for node in q)
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return ans
    




'''
approach: DFS
Time: O(N), where N is the number of nodes.
Space: O(10000) or O(H), where we keep sum for every level and H is the height of the tree.

You are here!
Your runtime beats 34.15 % of python submissions.
You are here!
Your memory usage beats 92.90 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = [0] * (10000 + 3)
        self.maxDepth = 0
        def findDepth(node, depth):
            self.maxDepth = max(self.maxDepth, depth)
            
            sums[depth] += node.val
            if node.left:
                findDepth(node.left, depth + 1)
            if node.right:
                findDepth(node.right, depth + 1)
        
        findDepth(root, 1)
        return sums[self.maxDepth]





