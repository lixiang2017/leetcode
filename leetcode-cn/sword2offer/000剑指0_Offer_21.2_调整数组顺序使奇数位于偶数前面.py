'''
approach: Two Pointers (Fast & Slow)
# 快慢双指针
Time: O(N)
Space: O(1)

ref:
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/ti-jie-shou-wei-shuang-zhi-zhen-kuai-man-shuang-zh/

执行结果：
通过
显示详情
执行用时：36 ms, 在所有 Python 提交中击败了80.61%的用户
内存消耗：17.9 MB, 在所有 Python 提交中击败了99.39%的用户
'''

class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        slow = fast = 0
        while slow < size and fast < size:
            if nums[fast] & 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
            else:
                fast += 1
        
        return nums
