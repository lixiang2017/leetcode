'''
???
Submission Detail
10 / 27 test cases passed.
    Status: Wrong Answer
    
Submitted: 0 minutes ago
Input: [0,null,1]
Output: 3
Expected: 1
'''

'''
Run Code Status: Finished
Run Code Result:
Your input

[0,null,1]

Your answer

1

Expected answer

1
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    min_memo = {}
    max_memo = {}
    
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxdiff = 0
        minimum = self.findMin(root)
        maximum = self.findMax(root)
        root_diff = max(abs(root.val - minimum) if minimum != sys.maxint else 0, abs(root.val - maximum) if maximum else 0)
        
        left_diff = self.maxAncestorDiff(root.left)
        right_diff = self.maxAncestorDiff(root.right)
        maxdiff = max(root_diff, left_diff, right_diff)
        # print 'node: ', root.val, 'diff: ', root_diff, left_diff, right_diff
        return maxdiff
        
    def findMin(self, root):
        # find minimum value in substrees, both left and right
        if not root or (not root.left and not root.right):
            return sys.maxint
        
        if root.val in self.min_memo:
            return self.min_memo[root.val]
        
        minimum = sys.maxint
        if root.left:
            minimum= min(minimum, root.left.val)
            minimum = min(minimum, self.findMin(root.left))
        if root.right:
            minimum = min(minimum, root.right.val)
            minimum = min(minimum, self.findMin(root.right))

        # to memorize
        self.min_memo[root.val] = minimum
        # print 'node: ', root.val, 'minimum: ', minimum       
        return minimum

    def findMax(self, root):
        # to find maximum value in substrees, both left and right
        if not root or (not root.left and not root.right):
            return None
        
        if root.val in self.max_memo:
            return self.max_memo[root.val]
        
        maximum = -sys.maxint
        if root.left:
            maximum = max(maximum, root.left.val)
            maximum = max(maximum, self.findMax(root.left))
            
        if root.right:
            maximum = max(maximum, root.right.val)
            maximum = max(maximum, self.findMax(root.right))
            
        # to memorize
        self.max_memo[root.val] = maximum
        # print 'node: ', root.val, 'maximum: ', maximum
        return maximum

'''
Run Code Status: Finished
Run Code Result:
Your input

[8,3,10,1,6,null,14,null,null,4,7,13]

Your stdout

node:  6 minimum:  4
node:  3 minimum:  1
node:  14 minimum:  13
node:  10 minimum:  13
node:  8 minimum:  1
node:  6 maximum:  7
node:  3 maximum:  7
node:  14 maximum:  13
node:  10 maximum:  14
node:  8 maximum:  14
node:  6 minimum:  4
node:  3 minimum:  1
node:  6 maximum:  7
node:  3 maximum:  7
node:  1 diff:  0 0 0
node:  6 minimum:  4
node:  6 maximum:  7
node:  4 diff:  0 0 0
node:  7 diff:  0 0 0
node:  6 diff:  2 0 0
node:  3 diff:  4 0 2
node:  14 minimum:  13
node:  10 minimum:  13
node:  14 maximum:  13
node:  10 maximum:  14
node:  14 minimum:  13
node:  14 maximum:  13
node:  13 diff:  0 0 0
node:  14 diff:  1 0 0
node:  10 diff:  4 0 1
node:  8 diff:  7 4 4

Your answer

7

Expected answer

7
'''


'''
Submission Result: Time Limit Exceeded 
'''


'''
[0,null,1]
'''

'''
In [4]: min(3, None)

In [5]: print min(3, None)
None

In [7]: max(5, None)
Out[7]: 5

'''


