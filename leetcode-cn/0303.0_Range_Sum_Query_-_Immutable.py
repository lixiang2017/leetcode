'''
approach: Prefix Sum
Time: O(N) for __init__, and O(1) for sumRange(i, j)
Space: O(N)

执行用时：184 ms, 在所有 Python 提交中击败了74.21%的用户
内存消耗：16.8 MB, 在所有 Python 提交中击败了40.08%的用户
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.N = len(nums)
        self.preSum = [0] * self.N 
        if self.N > 0:
            self.preSum[0] = self.nums[0]
            for i in range(1, self.N):
                self.preSum[i] = self.preSum[i - 1] + self.nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.preSum[j] - self.preSum[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



'''
Time: O(1) for __init__, and O(N) for sumRange(i, j)
Space: O(N)

执行用时：588 ms, 在所有 Python 提交中击败了29.76%的用户
内存消耗：16.4 MB, 在所有 Python 提交中击败了96.83%的用户
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i: j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

