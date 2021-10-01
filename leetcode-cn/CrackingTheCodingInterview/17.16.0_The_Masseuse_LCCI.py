'''
DP
T: O(N)
S: O(1)

执行用时：24 ms, 在所有 Python3 提交中击败了96.39% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了78.31% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def massage(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for x in nums:
            zero = dp1
            one = dp0 + x
            dp0 = max(dp0, zero)
            dp1 = max(dp1, one)
        return max(dp0, dp1)



'''
DP
T: O(N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了8.95% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.07% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def massage(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for x in nums:
            dp0, dp1 = max(dp0, dp1), max(dp1, dp0 + x)
        return max(dp0, dp1)


'''
执行用时：24 ms, 在所有 Python3 提交中击败了96.39% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了58.86% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def massage(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for x in nums:
            dp0, dp1 = max(dp0, dp1), dp0 + x
        return max(dp0, dp1)
        