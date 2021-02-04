'''
approach: Brute Force
Time: O(N * klogk)
Space: O(k)

执行结果：
通过
显示详情
执行用时：6120 ms, 在所有 Python 提交中击败了16.28%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了48.84%的用户
'''


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        median = []
        size = len(nums)
        left, right = 0, k
        odd = True if k & 1 else False

        while right <= size:
            segment = nums[left: right]
            segment.sort()
            if odd:
                med = segment[k / 2]
            else:
                med = (segment[k / 2 - 1] + segment[k / 2]) / 2.0
            median.append(med)

            left += 1
            right += 1
        return median
