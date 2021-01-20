'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：48 ms, 在所有 Python 提交中击败了93.65% 的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了80.32% 的用户
'''



class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max1 = max2 = max3 = -sys.maxint
        # min1 = min2 = sys.maxint
        max1 = max2 = max3 = -1001
        min1 = min2 = 1001        
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        maximum = max(min1 * min2 * max1, max1 * max2 * max3)
        return maximum
