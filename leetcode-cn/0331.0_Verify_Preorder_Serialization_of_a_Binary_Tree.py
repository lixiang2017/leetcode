'''
approach: Stack

ref:
https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/
https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/


执行用时：36 ms, 在所有 Python 提交中击败了17.54%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []

        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')

        return 1 == len(stack) and stack[-1] == '#'



'''
approach: Graph(Outdegree + Indegree)
Time: O(N)
Space: O(1)

In a binary tree, if we consider null as leaves, then
	all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
	all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
Suppose we try to build this tree. During building, we record the difference between out degree and in degree 
diff = outdegree - indegree. 
When the next node comes, we then decrease diff by 1, because the node provides an in degree. 
If the node is not null, we increase diff by2, because it provides two out degrees. 
If a serialization is correct, diff should never be negative and diff will be zero when finished.


ref:
https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/

执行用时：20 ms, 在所有 Python 提交中击败了78.95%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了49.12%的用户
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        diff = 1
        for node in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2

        return 0 == diff

