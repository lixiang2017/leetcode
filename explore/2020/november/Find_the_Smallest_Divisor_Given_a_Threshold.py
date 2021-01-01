'''
You are here!
Your runtime beats 5.75 % of python submissions.
'''


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low, high = 1, max(nums)
        
        def check(divisor, nums, threshold):
            sum_division = 0
            for num in nums:
                quotient, remainder = divmod(num, divisor)
                if remainder:
                    quotient += 1
                sum_division += quotient
                
                if sum_division > threshold:
                    return False
            return True
        
        # binary search
        while low <= high:
            mid = (low + high) / 2
            # print 'low mid high', low, mid, high
            if check(mid, nums, threshold):  # go to search lower
                high = mid - 1
            else:
                low = mid + 1
        
        return high + 1
        