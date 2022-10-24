'''
max_left + min_right
T: O(2N) = O(N)
S: O(N)

执行用时：288 ms, 在所有 Python3 提交中击败了56.44% 的用户
内存消耗：26.2 MB, 在所有 Python3 提交中击败了17.16% 的用户
通过测试用例：66 / 66
炫耀一下:
'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        min_right = [nums[-1]] * n 
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        max_left = -1
        for i in range(n - 1):
            max_left = max(max_left, nums[i])
            if max_left <= min_right[i + 1]:
                return i + 1
