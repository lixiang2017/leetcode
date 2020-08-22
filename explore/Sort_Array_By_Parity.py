'''
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
You are here!
Your runtime beats 96.99 % of python submissions.
'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        for a in A:
        	if a % 2 == 0:
        		ans.append(a)
        for a in A:
        	if a % 2 == 1:
        		ans.append(a)
        return ans


if __name__ == '__main__':
	A = [3,1,2,4]
	# Output: [2,4,3,1]
	# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
	print Solution().sortArrayByParity(A)