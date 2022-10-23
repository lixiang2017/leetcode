'''
xor, 把数字按照 lowbit 分成两类
T: O(5 * N)
S: O(1)

Runtime: 229 ms, faster than 86.00% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.3 MB, less than 96.23% of Python3 online submissions for Set Mismatch.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = xor0 = xor1 = 0
        n = len(nums)
        xor = reduce(operator.xor, chain(nums, range(1, n + 1)))
        lowbit = xor & (-xor)
        for x in chain(nums, range(1, n + 1)):
            if x & lowbit:
                xor1 ^= x 
            else:
                xor0 ^= x 
        for x in nums:
            if x == xor0:
                return [xor0, xor1]
        return [xor1, xor0]


'''
Runtime: 259 ms, faster than 80.13% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.5 MB, less than 69.79% of Python3 online submissions for Set Mismatch.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        Assume m is the missing and d is the duplicate element
        diff = m - d 
        squareDiff = m^2 - d^2
        sum = m + d = squareDiff / diff = (m + d)(m - d)/(m - d)
        now m = (sum + diff) / 2
            d = (sum - diff) / 2
        '''
        diff = squareDiff = 0
        for i, x in enumerate(nums):
            '''
            The order doesnot matter. keep adding the 1 to n and simultaneously subtracting corresponding array element.
            Using i+1 to get 1 to n since i is the index number which is zero based.
            '''
            diff += (i + 1) - x 
            # squareDiff is also calculated in the same way as diff is calculated.
            squareDiff += (i+ 1) * (i + 1) - x * x
        _sum = squareDiff // diff 
        return [(_sum - diff) // 2, (_sum + diff) // 2]
