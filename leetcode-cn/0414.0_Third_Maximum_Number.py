'''
approach: One Pass
Time: O(N)
Space: O(1)
执行用时：20 ms, 在所有 Python 提交中击败了77.03%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败74.64%的用户
'''


import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = -sys.maxint
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif second < num < first:
                third = second
                second = num
            elif third < num < second:
                third = num
        return third if third != -sys.maxint else first



import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one =  two = three = -sys.maxint
        
        for i in nums:
            if i > one:
                one, two, three = i, one, two
            elif i < one and i > two:
                two, three = i, two
            elif i < two and i > three:
                three = i
            
        return three if three != -sys.maxint else one


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)




'''
执行用时：28 ms, 在所有 Python3 提交中击败了93.74% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了82.00% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for x in nums:
            if x > first:
                first, second, third = x, first, second
            elif first > x > second:
                second, third = x, second
            elif second > x > third:
                third = x
        # print(first, second, third)
        return [first, third][third != float('-inf')]
        