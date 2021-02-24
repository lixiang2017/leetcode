'''
approach: Bit Manipulation(XOR by Groups)
Time: O(N + N) = O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：28 ms, 在所有 Python 提交中击败了90.88%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了37.50%的用户
'''

class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultExclusiveOR = 0
        resultExclusiveOR = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while (div & resultExclusiveOR) == 0:
            div <<= 1
        a = b = 0
        for num in nums:
            if div & num:
                a ^= num
            else:
                b ^= num
        return [a, b]


'''
approach: Bit Manipulation(XOR by Groups)
Time: O(N + N) = O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：40 ms, 在所有 Python 提交中击败了39.19%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了56.42%的用户
'''

class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultExclusiveOR = functools.reduce(lambda x, y: x ^ y, nums)
        # div = 1
        # while (div & resultExclusiveOR) == 0:
        #   div <<= 1
        lowbit = resultExclusiveOR & -resultExclusiveOR

        a = b = 0
        for num in nums:
            if lowbit & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
