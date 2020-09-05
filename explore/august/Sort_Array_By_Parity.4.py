'''
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
You are here!
Your runtime beats 17.87 % of python submissions.
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            while (A[i] & 1 == 0 and i < j):
                i += 1
            while (A[j] & 1 == 1 and i < j):
                j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

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