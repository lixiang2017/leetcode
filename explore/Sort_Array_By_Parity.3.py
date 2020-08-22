'''
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
You are here!
Your runtime beats 61.25 % of python submissions.

# in place, no more space
a_even_number & 1 --> 0
a_odd_number  & 1 --> 1
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lenA = len(A)
        even_index = 0

        for i in range(lenA):
            if A[i] & 1 == 0:
                A[even_index], A[i] = A[i], A[even_index]
                even_index += 1
        return A


if __name__ == '__main__':
	A = [3,1,2,4]
	# Output: [2,4,3,1]
	# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
	print Solution().sortArrayByParity(A)