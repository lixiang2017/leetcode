'''
Two Pointers
T: O(N^2)
S: O(1)
每一次 r 都从 l+1开始扫描，所以复杂度比较高。
l 找到不符合的，r去寻找符合的。

61 / 61 test cases passed.
    Status: Accepted
Runtime: 516 ms
Memory Usage: 16.6 MB
    
Submitted: 0 minutes ago

You are here!
Your memory usage beats 42.23 % of python3 submissions.
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = r = 0
        while l < len(nums):
            while l < len(nums) and l & 1 == nums[l] & 1:
                l += 1
            if l >= len(nums):
                break
            r = l + 1
            while r < len(nums) and l & 1 != nums[r] & 1:
                r += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            
        return nums

'''
Two Pointers
T: O(N)
S: O(1)

i: even
j: odd
i只关注偶数下标，j只关注奇数下标。i 与 j 的大小关系随时会动态变化。可能i > j, 也可能i < j。

You are here!
Your runtime beats 54.85 % of python3 submissions.
You are here!
Your memory usage beats 73.54 % of python3 submissions.
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i, j = 0, 1
        while i < N and j < N:
            if nums[i] & 1:
                while j < N and nums[j] & 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
            i += 2
        return nums


'''
Two Pointers
T: O(N)
S: O(1)

第一种情况的优化。r一直向前，不回头。需要限制 l 与 r的奇偶性。

You are here!
Your runtime beats 30.34 % of python3 submissions.
You are here!
Your memory usage beats 88.11 % of python3 submissions
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = r = 0
        while l < len(nums):
            while l < len(nums) and l & 1 == nums[l] & 1:
                l += 1
            if l >= len(nums):
                break
            if r == 0 or r == l:
                r = l + 1

            while r < len(nums) and ((l & 1 != nums[r] & 1) or (r & 1 == l & 1)):
                r += 1
            if r >= len(nums):
                break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

        return nums




