'''
Success!
Your code took 49 milliseconds — faster than 58.00% in Python
'''
class Solution:
    def solve(self, nums):
        nums.sort()
        i, n, part, _sum = 0, len(nums), 0, sum(nums)
        if _sum & 1:
            return False
        while i < n and part < _sum // 2:
            part += nums[i]
            i += 1
        return i < n and part == _sum // 2 and nums[i - 1] < nums[i]

'''
Testcase
nums = [1, 3, 3, 4, 4]
Your result
True
Expected
False
'''
