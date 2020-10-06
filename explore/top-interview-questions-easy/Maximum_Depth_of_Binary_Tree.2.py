'''
use built-in function pop(index) in list

# Output Limit Exceeded   # need to comment out all print statements

You are here!
Your runtime beats 96.01 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        Q = [(root, 1)]
        depth = 0
        while Q:
            cur = Q.pop(0)
            print 'pop: ', cur
            depth = cur[1]
            print 'current depth: ', depth
            if cur[0].left:
                print 'append left: ', (cur[0].left, depth + 1)
                Q.append((cur[0].left, depth + 1))
            if cur[0].right:
                print 'append right: ', (cur[0].right, depth + 1)
                Q.append((cur[0].right, depth + 1))
        
        return depth



'''
Run Code Result:
Your input

[3,9,20,null,null,15,7]

Your stdout

pop:  (TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}, 1)
current depth:  1
append left:  (TreeNode{val: 9, left: None, right: None}, 2)
append right:  (TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, 2)
pop:  (TreeNode{val: 9, left: None, right: None}, 2)
current depth:  2
pop:  (TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, 2)
current depth:  2
append left:  (TreeNode{val: 15, left: None, right: None}, 3)
append right:  (TreeNode{val: 7, left: None, right: None}, 3)
pop:  (TreeNode{val: 15, left: None, right: None}, 3)
current depth:  3
pop:  (TreeNode{val: 7, left: None, right: None}, 3)
current depth:  3

Your answer

3

Expected answer

3

'''


'''
Your input

[3,9,20,null,14,15,7, 4, 24]

Your stdout

pop:  (TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: TreeNode{val: 14, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 24, left: None, right: None}}}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}, 1)
current depth:  1
append left:  (TreeNode{val: 9, left: None, right: TreeNode{val: 14, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 24, left: None, right: None}}}, 2)
append right:  (TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, 2)
pop:  (TreeNode{val: 9, left: None, right: TreeNode{val: 14, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 24, left: None, right: None}}}, 2)
current depth:  2
append right:  (TreeNode{val: 14, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 24, left: None, right: None}}, 3)
pop:  (TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, 2)
current depth:  2
append left:  (TreeNode{val: 15, left: None, right: None}, 3)
append right:  (TreeNode{val: 7, left: None, right: None}, 3)
pop:  (TreeNode{val: 14, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 24, left: None, right: None}}, 3)
current depth:  3
append left:  (TreeNode{val: 4, left: None, right: None}, 4)
append right:  (TreeNode{val: 24, left: None, right: None}, 4)
pop:  (TreeNode{val: 15, left: None, right: None}, 3)
current depth:  3
pop:  (TreeNode{val: 7, left: None, right: None}, 3)
current depth:  3
pop:  (TreeNode{val: 4, left: None, right: None}, 4)
current depth:  4
pop:  (TreeNode{val: 24, left: None, right: None}, 4)
current depth:  4

Your answer

4

Expected answer

4
'''