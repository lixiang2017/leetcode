'''
sort + two pointers
T: O(NlogN + N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了36.92% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了81.92% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        n = len(nums)
        for i in range(n - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans 
