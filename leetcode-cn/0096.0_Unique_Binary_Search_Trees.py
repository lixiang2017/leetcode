'''
执行用时：48 ms, 在所有 Python3 提交中击败了6.03% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了11.82% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        #      0  1  2
        dp =  [1, 1, 2] + [0] * 17
        for i in range(3, n + 1):
            for j in range(i):
                # 0...j-1 j j+1...i-1
                left = j
                right = i - 1 - j
                dp[i] += dp[left] * dp[right]

        return dp[n]
        