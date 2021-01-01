'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/
You are here!
Your runtime beats 80.00 % of python submissions.
'''


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # ans = set(range(1, 10))
        ans = {x for x in xrange(1, 10)}
        for _ in xrange(N - 1):
        	ans2 = set()
        	for a in ans:
        		d = a % 10
        		if d - K >= 0:
        			ans2.add(a * 10 + d - K)
        		if d + K <= 9:
        			ans2.add(a * 10 + d + K)
        	ans = ans2

        if N == 1:
        	ans.add(0)
        return list(ans)


if __name__ == '__main__':
	N = 3
	K = 7
	Output = [181,292,707,818,929]
	ans = Solution().numsSameConsecDiff(N, K)
	# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
	print ans
	assert sorted(ans) == sorted(Output)

	N = 2
	K = 1
	Output = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
	ans = Solution().numsSameConsecDiff(N, K)
	print ans
	assert sorted(ans) == sorted(Output)

	N = 9
	K = 1
	ans = Solution().numsSameConsecDiff(N, K)
	print ans	