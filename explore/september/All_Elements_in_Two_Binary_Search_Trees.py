'''
You are here!
Your runtime beats 25.89 % of python submissions.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def traverse(root):
            if not root:
                return []
            l = []
            if root.left:
                l +=  traverse(root.left)
            l.append(root.val)
            if root.right:
                l += traverse(root.right)
            return l
        
        list1 = traverse(root1)
        list2 = traverse(root2)
        
        len1, len2 = len(list1), len(list2)
        i, j = 0, 0
        result = []
        while i < len1 and j < len2:
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
                continue
            elif list1[i] > list2[j]:
                result.append(list2[j])
                j += 1
                continue
            else:
                result += [list1[i]] * 2
                i += 1
                j += 1
        
        if i == len1:
            result += list2[j:]
        if j == len2:
            result += list1[i:]
        
        return result
                
            