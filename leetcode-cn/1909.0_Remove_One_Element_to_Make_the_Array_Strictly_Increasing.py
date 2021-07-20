'''
think about all cases
T:O(N),S:O(1)
执行用时：32 ms, 在所有 Python3 提交中击败了97.10% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了32.52% 的用户
'''
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # indices for not strictly increasing pairs
        pairs = []
        N = len(nums)
        for i in range(N - 1):
            if nums[i] >= nums[i + 1]:
                pairs.append([i, i + 1])
                if len(pairs) > 1:
                    return False
        # no need to remove
        if not pairs: return True
        # 
        a, b = pairs[0]
        short = [nums[a], nums[b]]
        if a > 0:
            short = [nums[a - 1]] + short
        if b <= N - 2:
            short.append(nums[b + 1])
        if len(short) <= 3: return True
        # only 4 elements
        if short[0] < short[1] < short[3] or short[0] < short[2] < short[3]:
            return True
        else:
            return False

