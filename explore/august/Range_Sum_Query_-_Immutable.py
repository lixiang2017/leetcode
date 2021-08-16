'''
You are here!
Your runtime beats 62.86 % of python3 submissions.
You are here!
Your memory usage beats 21.76 % of python3 submissions.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



'''
You are here!
Your runtime beats 97.72 % of python3 submissions.
You are here!
Your memory usage beats 21.76 % of python3 submissions.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.sum[right]
        else:
            return self.sum[right] - self.sum[left - 1]

        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
