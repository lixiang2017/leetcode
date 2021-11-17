'''
DP
T: O(NlogN + N^2)
S: O(N)

Runtime: 456 ms, faster than 31.07% of Python3 online submissions for Largest Divisible Subset.
Memory Usage: 14.3 MB, less than 86.53% of Python3 online submissions for Largest Divisible Subset.
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # need to sort first
        nums.sort()
        N = len(nums)
        seq = [[nums[i]] for i in range(N)]
        # length for ending with every position, divisible subset
        # length = [1 for i in range(N)]
        ans = [nums[0]]
        for i in range(N - 1):
            for j in range(i + 1, N):    
                if nums[j] % nums[i] == 0:
                    # length[j] = max(length[j], length[i] + 1)
                    if len(seq[i]) + 1 > len(seq[j]):
                        seq[j] = seq[i][:] + [nums[j]]
                        if len(seq[j]) > len(ans):
                            ans = seq[j]
        return ans
                        
