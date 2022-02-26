'''
T: O(N^2)
S: O(1)

执行用时：204 ms, 在所有 Python3 提交中击败了30.98% 的用户
内存消耗：26.9 MB, 在所有 Python3 提交中击败了5.05% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        return max([nums[j] - nums[i] for i in range(n - 1) for j in range(i + 1, n) if nums[i] < nums[j]] + [-1])


'''
T: O(N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了68.01% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了46.46% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n, ans, minx = len(nums), -1, nums[0]
        for i in range(n):
            minx = min(minx, nums[i])
            if nums[i] > minx:
                ans = max(ans, nums[i] - minx)
        return ans
