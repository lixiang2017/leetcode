'''
Success
Details 
Runtime: 40 ms, faster than 67.94% of Python online submissions for Third Maximum Number.
Memory Usage: 12.5 MB, less than 50.00% of Python online submissions for Third Maximum Number.
'''

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


if __name__ == "__main__":
    nums = [3, 2, 1]
    assert Solution().thirdMax(nums) == 1

    nums = [1, 2]
    assert Solution().thirdMax(nums) == 2

    nums = [2, 2, 3, 1]
    assert Solution().thirdMax(nums) == 1

    nums = [5]
    assert Solution().thirdMax(nums) == 5

    nums = [6, 6, 6]
    assert Solution().thirdMax(nums) == 6

    nums = [6, 6, 7]
    assert Solution().thirdMax(nums) == 7
