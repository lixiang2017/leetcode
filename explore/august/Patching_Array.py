'''
Greedy
Time: O(N)
Space: O(1)

这种构造序列的题目，一般需要找规律。
如何生成序列呢？滚雪球。从最开始的，从小慢慢滚到大。

You are here!
Your runtime beats 68.39 % of python3 submissions.
You are here!
Your memory usage beats 5.70 % of python3 submissions.
'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch, x = 0, 1
        index, N = 0, len(nums)
        while x <= n:
            if index < N and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patch += 1
        return patch
