'''
前缀最大值+后缀最小值
premax + postmin
T: O(2N)
S: O(N)

比赛时误以为AC了，其实是写错了，没通过。

执行用时：316 ms, 在所有 Python3 提交中击败了70.26%的用户
内存消耗：25 MB, 在所有 Python3 提交中击败了79.64%的用户
通过测试用例：
62 / 62
'''
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        N = len(nums)
        b = 0
        premax = nums[0]
        postmin = [nums[-1]] * N
        for i in range(N - 2, -1, -1):
            postmin[i] = min(postmin[i+1], nums[i])
        
        for i in range(1, N - 1):
            premax = max(premax, nums[i - 1])
        
            if premax < nums[i] < postmin[i + 1]:
                b += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                b += 1
        
        return b