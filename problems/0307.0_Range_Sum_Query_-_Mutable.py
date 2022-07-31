'''
分块处理/ sqrt decomposition
__init__
T: O(N)
S: O(N + sqrt(N))

update
T: O(1)
S: O(1)

sumRange
T: O(sqrt(N) + sqrt(N))
S: O(1)

Runtime: 2437 ms, faster than 73.46% of Python3 online submissions for Range Sum Query - Mutable.
Memory Usage: 31.3 MB, less than 66.19% of Python3 online submissions for Range Sum Query - Mutable.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.block_cnt = int(sqrt(self.n - 1)) + 1
        self.block_size = self.block_cnt
        self.block_sum = [0] * self.block_cnt 
        for i, num in enumerate(nums):
            r, c = divmod(i, self.block_size)
            self.block_sum[r] += num

    def update(self, index: int, val: int) -> None:
        r, c = divmod(index, self.block_size)
        self.block_sum[r] += -self.nums[index] + val 
        self.nums[index] = val 

    def sumRange(self, left: int, right: int) -> int:
        r1, c1 = divmod(left, self.block_size)
        r2, c2 = divmod(right, self.block_size)
        if r1 == r2:
            return sum(self.nums[left: right + 1])
        s1 = sum(self.nums[left: (r1 + 1) * self.block_size])
        s2 = sum(self.block_sum[r1 + 1: r2])
        s3 = sum(self.nums[r2 * self.block_size: right + 1])
        return s1 + s2 + s3 
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
