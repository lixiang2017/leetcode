'''
Brute Force
Time: O(N^3) = 10^9
Space: O(1)
219 / 233 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        for i in range(2, N):
            for j in range(1, i):
                for k in range(j):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        total += 1
        return total

'''
Sort + Two Pointers + Greedy
Time: O(N^2)
Space: O(logN) for sort

You are here!
Your runtime beats 41.29 % of python3 submissions.
You are here!
Your memory usage beats 30.59 % of python3 submissions.
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        total = 0
        for i in range(N - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, N - 1):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                total += k - j - 1
        return total

'''
Input: [0,0,0]
Output: -1
Expected: 0

Input: [0,1,0,1]
Output: -1
Expected: 0
'''
