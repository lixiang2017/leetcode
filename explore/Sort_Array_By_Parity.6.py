'''
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
You are here!
Your runtime beats 76.80 % of python submissions.
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(A) - 1
        while start < end:
            if A[start] % 2 > A[end] % 2:
                A[start], A[end] = A[end], A[start]
            if A[start] % 2 == 0: start += 1
            if A[end] % 2 == 1: end -= 1
        return A


if __name__ == '__main__':
    A = [3,1,2,4]
    # Output: [2,4,3,1]
    # The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    print Solution().sortArrayByParity(A)

    A = [0, 2]
    print Solution().sortArrayByParity(A)

    A = [1, 3]
    print Solution().sortArrayByParity(A)    