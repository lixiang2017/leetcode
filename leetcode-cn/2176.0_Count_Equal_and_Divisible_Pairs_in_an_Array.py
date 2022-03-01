'''
brute force
T: O(N^2)
S: O(1)
'''
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    ans += 1
        return ans 
        