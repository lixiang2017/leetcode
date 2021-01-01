'''
You are here!
Your runtime beats 69.52 % of python submissions.
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges = []
        nums.append(nums[-1] + 2)
        size = len(nums)
        segment = []
        for i in range(size - 1):
            segment.append(nums[i])
            if nums[i] + 1 != nums[i + 1]:
                low, high = segment[0], segment[-1]
                if low == high:
                    ranges.append(str(low))
                else:
                    ranges.append(str(low) + '->' + str(high))
                    
                segment = []
            else:
                continue
                
        return ranges