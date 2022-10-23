'''
Hash Table,T:O(2N),S:O(N)

执行用时：104 ms, 在所有 Python3 提交中击败了13.85% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了19.81% 的用户
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        freq = defaultdict(int)
        # find dup
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                ans.append(num)
        # find missing
        for i in range(1, len(nums) + 1):
            if i not in freq:
                ans.append(i)
                break
        return ans

'''
xor, 把数字按照 lowbit 分成两类
T: O(5 * N)
S: O(1)


执行用时：68 ms, 在所有 Python3 提交中击败了41.82% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了90.54% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor0 = xor1 = 0
        n = len(nums)
        xor = reduce(operator.xor, chain(nums, range(1, n + 1)))
        lowbit = xor & -xor
        for x in chain(nums, range(1, n + 1)):
            if x & lowbit:
                xor1 ^= x 
            else:
                xor0 ^= x 
        for x in nums:
            if x == xor1:
                return [xor1, xor0]
        return [xor0, xor1]            


'''
执行用时：60 ms, 在所有 Python3 提交中击败了60.17% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了92.72% 的用户
通过测试用例：49 / 49
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

