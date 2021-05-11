'''
approach: DP
Time: O(N^2)
Space: O(N)

ref:
https://leetcode-cn.com/problems/binary-trees-with-factors/solution/dai-yin-zi-de-er-cha-shu-by-leetcode/


You are here!
Your memory usage beats 66.67 % of python submissions.
'''


class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        N = len(arr)
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in xrange(i):
                if x % arr[j] == 0: # A[j] will be left child
                    right = x / arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD
        