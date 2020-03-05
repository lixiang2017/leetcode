'''
Success
Details 
Runtime: 980 ms, faster than 17.63% of Python online submissions for Range Sum Query - Immutable.
Memory Usage: 15.2 MB, less than 92.31% of Python online submissions for Range Sum Query - Immutable.
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
        return sum(self.nums[i:j + 1])
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)

    i, j = 0, 2
    assert obj.sumRange(i, j) == 1

    i, j = 2, 5
    assert obj.sumRange(i, j) == -1

    i, j = 0, 5
    assert obj.sumRange(i, j) == -3