'''
DP
Time: O(3N) = O(N)
Space: O(3N) = O(N)
执行用时：64 ms, 在所有 Python3 提交中击败了94.61% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了23.32% 的用户
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right, ans = [1] * N, [1] * N, [1] * N
        for i in range(1, N):
            left[i] = left[i - 1] * nums[i - 1]
        for i in reversed(range(N - 1)):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(N):
            ans[i] = left[i] * right[i]
        return ans


'''
DP
Time: O(2N) = O(N)
Space: O(1)
执行用时：72 ms, 在所有 Python3 提交中击败了81.03% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了50.11% 的用户
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1] * N
        for i in range(1, N):
            ans[i] = ans[i - 1] * nums[i - 1]
        R = 1
        for i in reversed(range(N - 1)):
            R *= nums[i + 1]
            ans[i] *= R
        return ans
