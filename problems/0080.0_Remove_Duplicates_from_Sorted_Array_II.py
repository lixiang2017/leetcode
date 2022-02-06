'''
two pointers
T: O(N)
S: O(1)

Runtime: 68 ms, faster than 52.15% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.9 MB, less than 96.82% of Python3 online submissions for Remove Duplicates from Sorted Array II.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = cnt = 0
        pre = float('-inf')
        for j, x in enumerate(nums):
            if x != pre:
                # move
                nums[i] = x
                i += 1
                # set
                cnt = 1
            else:
                cnt += 1
                if cnt <= 2:
                    nums[i] = x
                    i += 1
            pre = x

        return i
    
'''
two pointers
T: O(N)
S: O(1)

Runtime: 56 ms, faster than 79.16% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14 MB, less than 89.34% of Python3 online submissions for Remove Duplicates from Sorted Array II.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = cnt = 0
        pre = float('-inf')
        for x in nums:
            if x != pre:
                # move
                nums[i] = x
                i += 1
                # set
                cnt = 1
            else:
                cnt += 1
                if cnt <= 2:
                    nums[i] = x
                    i += 1
            pre = x

        return i
    
