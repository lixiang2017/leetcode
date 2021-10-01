'''
ref:
https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/solution/bitmask-zhuang-ya-python-by-yzboostfores-d2sg/

Backtracking

You are here!
Your runtime beats 31.08 % of python3 submissions.
You are here!
Your memory usage beats 29.57 % of python3 submissions.
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        n = len(nums)
        visited = [False] * n
        if k > n or sum(nums) % k:
            return False
        target = sum(nums) // k
        
        def recur(nums, curr, curr_sum, visited, K):
            if K == 0:
                return True
            if curr_sum == target:
                return recur(nums, 0, 0, visited, K - 1)  # from beginning 0-idx
            for i in range(curr, n):
                if visited[i]:
                    continue
                visited[i] = True
                curr_sum += nums[i]
                if recur(nums, i, curr_sum, visited, K):
                    return True
                curr_sum -= nums[i]
                visited[i] = False
            return False
        
        return recur(nums, 0, 0, visited, k)


'''
BitMask

You are here!
Your runtime beats 30.68 % of python3 submissions.
You are here!
Your memory usage beats 91.88 % of python3 submissions.
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        n = len(nums)
        if k > n or sum(nums) % k:
            return False
        target = sum(nums) // k
        
        def recur(nums, curr, curr_sum, state, K):
            if K == 0:
                return True
            if curr_sum == target:
                return recur(nums, 0, 0, state, K - 1)  # from beginning 0-idx
            for i in range(curr, n):
                if state & (1 << i):
                    continue
                if recur(nums, i, curr_sum + nums[i], state | (1 << i), K):
                    return True
            return False
        
        return recur(nums, 0, 0, 0, k)

