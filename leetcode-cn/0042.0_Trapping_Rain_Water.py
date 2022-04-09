'''
DP
Time: O(3N) = O(N)
Space: O(2N) = O(N)

执行用时：72 ms, 在所有 Python3 提交中击败了10.73% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了15.39% 的用户
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right = [0] * N, [0] * N
        left_max = right_max = 0
        for i in range(N):
            left[i] = left_max = max(left_max, height[i])
        for i in range(N - 1, -1, -1):
            right[i] = right_max = max(right_max, height[i])
        
        water = 0
        for i in range(N):
            water += min(left[i], right[i]) - height[i]
        return water

'''
approach: DP
Time: O(3N) = O(N)
Space: O(2N) = O(N)
执行用时：56 ms, 在所有 Python3 提交中击败了31.00% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了20.16% 的用户
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N < 3:
            return 0
        left, right = [0] * N, [0] * N
        left[0] = height[0]
        right[N - 1] = height[N - 1]
        for i in range(1, N):
            left[i] = max(left[i - 1], height[i])
        for i in range(N - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        water = 0
        for i in range(N):
            water += min(left[i], right[i]) - height[i]
        return water

'''
two passes
from right to left, from left to right
T: O(2N)
S: O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了45.73% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了64.58% 的用户
通过测试用例：321 / 321
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right = [height[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        left = height[0]
        ans = 0
        for i in range(1, n - 1):
            left = max(left, height[i])
            ans += min(left, right[i]) - height[i]
        return ans 


