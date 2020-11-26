'''
Success
Details
Runtime: 64 ms, faster than 94.63% of Python online submissions for Subtree of Another Tree.
Memory Usage: 14.7 MB, less than 17.17% of Python online submissions for Subtree of Another Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        str_s = self.preorder_traversal(s)
        str_t = self.preorder_traversal(t)
        print 'str_s: ', str_s
        print 'str_t: ', str_t
        return str_t in str_s
        
    
    def preorder_traversal(self, root):
        if root:
            st = ("*" + str(root.val))
            left = self.preorder_traversal(root.left)
            right = self.preorder_traversal(root.right)
            return st + left + right
        else:
            return '#none'
        
'''
str_s:  *3*4*1#none#none*2#none#none*5#none#none
str_t:  *4*1#none#none*2#none#none
'''        



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(s):
            return '^' + str(s.val) + '#' + convert(s.left) + '*' + convert(s.right) if s else '$'
        
        return convert(t) in convert(s)




'''
Success
Details
Runtime: 52 ms, faster than 99.71% of Python online submissions for Subtree of Another Tree.
Memory Usage: 14.7 MB, less than 33.46% of Python online submissions for Subtree of Another Tree.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s1 = self.preorder(s)
        t1 = self.preorder(t)
        return s1.find(t1) >= 0
    
    def preorder(self, t):
        if t is None:
            return '#'
        
        return 'd' + str(t.val) + ',' + self.preorder(t.left) + '+' + self.preorder(t.right)
    
    
    


