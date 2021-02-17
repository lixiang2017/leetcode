'''
approach: DFS / Recursion

# 递归是操作系统帮我们维护栈，而迭代是我们自己自定义栈。就这个区别。感觉有点像协程和进程的关系。
ref:
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/ncha-shu-de-qian-xu-bian-li-by-leetcode/

Success
Details 
Runtime: 48 ms, faster than 48.63% of Python online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.5 MB, less than 47.79% of Python online submissions for N-ary Tree Preorder Traversal.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return None
        traversal = [root.val]
        for child in root.children:
            traversal += self.preorder(child)
            
        return traversal    


'''
approach: Iteration / BFS
Time: O(M), where M is the number of nodes.
Space: O(M), where M is the number of nodes.

Runtime: 40 ms, faster than 87.58% of Python online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.4 MB, less than 47.79% of Python online submissions for N-ary Tree Preorder Traversal.
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            stack.extend(node.children[:: -1])
        
        return traversal
    
