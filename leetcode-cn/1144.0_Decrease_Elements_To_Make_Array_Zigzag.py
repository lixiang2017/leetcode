'''
执行用时：40 ms, 在所有 Python3 提交中击败了46.34% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了51.22% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        # 0 -> 1, increase
        t1 = 0 if nums[1] > nums[0] else nums[0] - (nums[1] - 1)
        for i in range(1, n - 1, 2):
            right = nums[i] - 1
            if i + 2 < n:
                right = min(right, nums[i + 2] - 1)
            if nums[i + 1] > right:
                t1 += nums[i + 1] - right
        
        # 0 -> 1, decrease
        t2 = 0
        for i in range(0, n, 2):
            right = nums[i] - 1
            if i + 2 < n:
                right = min(right, nums[i + 2] - 1)
            if i + 1 < n and nums[i + 1] > right:
                t2 += nums[i + 1] - right           

        return min(t1, t2)

