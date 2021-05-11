'''
approach: Math
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 100.00 % of python submissions.
You are here!
Your memory usage beats 40.00 % of python submissions.
'''


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, element in enumerate(A):
            if abs(element - i) > 1:
                return False
        return True


'''
approach: Math
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 82.50 % of python submissions.
'''

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(element - i) <= 1 for i, element in enumerate(A))


'''
approach: Remember the minimum value from right to left
Time: O(N)
Space :O(1)

You are here!
Your runtime beats 27.50 % of python submissions.
ref:
https://leetcode-cn.com/problems/global-and-local-inversions/solution/quan-ju-dao-zhi-yu-ju-bu-dao-zhi-by-leetcode/
'''

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        floor = N
        for i in range(N - 1, -1, -1):
            floor = min(A[i], floor)
            if i >= 2 and A[i - 2] > floor:
                return False
        return True




'''
Brute Force
Time: O(N^2)
Space: O(1)

160 / 208 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
'''

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        for i in range(N):
            for j in range(i + 2, N):
                if A[i] > A[j]:
                    return False
        return True

'''
160 / 208 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
'''
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all( x < A[j]
            for i, x in enumerate(A)
            for j in range(i + 2, len(A)))







        