'''
approach: Two Pointers / Three Pointers
Time: O(N)
Space: O(1)

执行用时：32 ms, 在所有 Python 提交中击败了14.88%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.12%的用户
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        realIdx = firstIdx = secondIdx = dup = 0
        while secondIdx < N:
            while secondIdx < N and nums[firstIdx] == nums[secondIdx]:
                dup += 1
                secondIdx += 1
            if dup > 2:
                nums[realIdx: realIdx + 2] = nums[firstIdx: firstIdx + 2]
                realIdx += 2
            else:
                nums[realIdx: realIdx + secondIdx - firstIdx] = nums[firstIdx: secondIdx]
                realIdx += (secondIdx - firstIdx)
            dup = 0
            firstIdx = secondIdx
        
        return realIdx
