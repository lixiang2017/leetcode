'''
Prefix Sum
T: O(N^2)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了91.97% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.21% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        presum = [0] + list(itertools.accumulate(arr))
        N = len(arr)
        total = 0
        # length
        for L in range(1, N + 1, 2):
            for i in range(N + 1):
                if i + L <= N:
                    total += presum[i + L] - presum[i]
        return total



'''
range(N + 1 - L)

执行用时：40 ms, 在所有 Python3 提交中击败了85.62% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.21% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        presum = [0] + list(itertools.accumulate(arr))
        N = len(arr)
        total = 0
        # length
        for L in range(1, N + 1, 2):
            for i in range(N + 1 - L):
                total += presum[i + L] - presum[i]
        return total
