'''
O(n) time with O(1) space

You are here!
Your runtime beats 90.30 % of python submissions.
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
        # segment = []
        start = end = nums[0]
        for i in range(size - 1):
            # segment.append(nums[i])
            end = nums[i]
            if nums[i] + 1 != nums[i + 1]:
                # low, high = segment[0], segment[-1]
                # if low == high:
                #     ranges.append(str(low))
                # else:
                #     ranges.append(str(low) + '->' + str(high))  
                # segment = []
                if start == end:
                    ranges.append(str(start))
                # else:
                elif end > start:
                    ranges.append(str(start) + '->' + str(end))
                
                start = nums[i + 1]
            else:
                continue
                
        return ranges








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
        start = end = nums[0]
        for i in range(size - 1):
            end = nums[i]
            if nums[i] + 1 != nums[i + 1]:
                if start == end:
                    ranges.append(str(start))
                elif end > start:
                    ranges.append(str(start) + '->' + str(end))
                
                start = nums[i + 1]
            else:
                continue
                
        return ranges
