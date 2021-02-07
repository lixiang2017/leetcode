'''
approach: Greedy

ref:
https://leetcode-cn.com/problems/non-decreasing-array/solution/fei-di-jian-shu-lie-by-leetcode-solution-zdsm/
https://leetcode-cn.com/problems/non-decreasing-array/solution/3-zhang-dong-tu-bang-zhu-ni-li-jie-zhe-d-06gi/

I think it's not a easy question, and I don't when to make modifications and how to.
Time: O(N)
Space:O(1)

执行结果：
通过
显示详情
执行用时：32 ms, 在所有 Python 提交中击败了71.77%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了47.37%的用户
'''


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        left = 0
        modification = 0
        while left < size - 1:
            if nums[left] > nums[left + 1]:
                modification += 1
                if modification > 1:
                    return False

                if left > 0 and nums[left + 1] < nums[left - 1]:
                    nums[left + 1] = nums[left]

            left += 1
        return True


'''
Just one more check and modificaition if you find a decreasing subarray.
Don't be afraid, just do it!

approach: Greedy
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：36 ms, 在所有 Python 提交中击败了55.24%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了62.75%的用户
'''


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        modification = 0
        for i in range(1, size):
            if nums[i] < nums[i - 1]:
                modification += 1
                if modification > 1:
                    return False
                # modify
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        return True
