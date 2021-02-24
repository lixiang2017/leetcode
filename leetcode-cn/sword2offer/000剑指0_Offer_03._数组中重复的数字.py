'''
approach: Hash Table
Time: O(N)
Space: O(N)

执行用时：72 ms, 在所有 Python 提交中击败了15.41%的用户
内存消耗：23.8 MB, 在所有 Python 提交中击败了5.00%的用户
'''

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        for num, cnt in Counter(nums).iteritems():
            if cnt >= 2:
                return num


'''
approach: Swap in place
Time: O(N)
Space: O(1)
执行用时：32 ms, 在所有 Python 提交中击败了78.83%的用户
内存消耗：19.7 MB, 在所有 Python 提交中击败了77.26%的用户
'''

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]: 
                    return nums[i]
                # not equal, swap
                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp

        return -1
