#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:  # i > 0  !!!
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1

        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    sln = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    sln_set = (
        (-1, 0, 1),
        (-1, -1, 2)
    )
    print Solution().threeSum(nums)

    nums = [0, 0, 0]
    res = [[0, 0, 0]]
    print Solution().threeSum(nums)

    nums = [-2, 0, 0, 2, 2]
    res = [[-2,0,2]]
    print Solution().threeSum(nums)

# @lc code=end
