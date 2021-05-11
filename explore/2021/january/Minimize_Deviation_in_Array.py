'''
approach: Greedy + SortedList
#  官方提示给的很明确；其实只要保证策略的单向性就能利用贪心算法做出正确的结果

76 / 76 test cases passed.
Status: Accepted
Runtime: 1612 ms
Memory Usage: 23.5 MB
Submitted: 0 minutes ago

You are here!
Your memory usage beats 45.90 % of python submissions.

ref:
https://leetcode-cn.com/problems/minimize-deviation-in-array/solution/you-xu-ji-he-you-xian-dui-lie-xun-huan-chu-li-by-m/
https://leetcode-cn.com/problems/minimize-deviation-in-array/solution/5616shu-zu-de-zui-xiao-pian-yi-liang-wo-shi-dai-ma/
'''

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from sortedcontainers import SortedList
        nums = SortedList(num << 1 if num & 1 else num for num in nums)
        
        diff = nums[-1] - nums[0]
        while not nums[-1] & 1:
            nums.add(nums.pop() >> 1)
            diff = min(diff, nums[-1] - nums[0])
        
        return diff
    