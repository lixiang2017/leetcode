'''
two pointers
sorted first
i [0 -> len-2]
j [i+1 -> len-1 and difference great than k]
# ensure distinct
if num[i] == num[i-1]: continue
if nums[j] == nums[j-1]: continue
# Success
Details 
Runtime: 336 ms, faster than 11.19% of Python online submissions for K-diff Pairs in an Array.
Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for K-diff Pairs in an Array.
'''

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        l = len(nums)
        for i in range(0, l - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            while (j < l and nums[j] - nums[i] <= k):
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if nums[j] - nums[i] == k:
                    count += 1
                j += 1

        return count            


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5]
    k = 2
    assert Solution().findPairs(nums, k) == 2

    nums = [1, 2, 3, 4, 5]
    k = 1
    assert Solution().findPairs(nums, k) == 4

    nums = [1, 3, 1, 5, 4]
    k = 0
    assert Solution().findPairs(nums, k) == 1

    nums = [5, 5, 5, 5, 5]
    k = 0
    assert Solution().findPairs(nums, k) == 1

    nums = [6, 6, 6, 7, 7]
    k = 0
    assert Solution().findPairs(nums, k) == 2  
