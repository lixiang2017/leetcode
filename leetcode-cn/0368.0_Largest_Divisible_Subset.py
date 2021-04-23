'''
approach: DP
Time: O(N^2)
Space: O(N)

ref:
https://leetcode-cn.com/problems/largest-divisible-subset/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-0a3jc/

执行用时：340 ms, 在所有 Python3 提交中击败了83.99%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了98.95%的用户
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        f, g = [0] * N, [0] * N
        for i in range(N):
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j] + 1 > length:
                        length = f[j] + 1
                        prev = j
            f[i] = length
            g[i] = prev
        
        max_len = idx = 0
        for i in range(N):
            if f[i] > max_len:
                max_len = f[i]
                idx = i

        largest = []
        while len(largest) != max_len:
            largest.append(nums[idx])
            idx = g[idx]

        return largest
