'''
Author: lixiang
Beats: 92.69%
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        # 0  l-k l-k l
        nums[0 : l-k] = reversed(nums[0 : l-k])
        nums[l-k : l] = reversed(nums[l-k : l])
        nums.reverse()
     #   return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    print(Solution().rotate(nums, k))

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    print(Solution().rotate(nums, k))

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().rotate(nums, k))

    nums = [-1,-100,3,99]
    k = 1
    print(Solution().rotate(nums, k))

    nums = [-1, -100, 3, 99]
    k = 2
    print(Solution().rotate(nums, k))