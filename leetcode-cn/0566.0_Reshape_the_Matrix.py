'''
Time: O(M * N * 2) = O(M * N)
Space: O(M * N)

执行结果：
通过
显示详情
执行用时：68 ms, 在所有 Python 提交中击败了98.01%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了41.06%的用户
'''

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        
        reshaped = []
        original = []
        for num in nums:
            original.extend(num)

        i = 0
        while i < m * n:
            current_row = original[i: i + c]
            reshaped.append(current_row)
            i += c

        return reshaped


'''
执行结果：
通过
显示详情
执行用时：84 ms, 在所有 Python 提交中击败了52.32%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了38.41%的用户
'''


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        reshaped = [[0] * c for _ in range(r)]
        for i in range(m * n):
            reshaped[i / c][i % c] = nums[i / n][i % n]

        return reshaped


'''
执行结果：
通过
显示详情
执行用时：76 ms, 在所有 Python 提交中击败了83.44%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了33.11%的用户
'''


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        reshaped = [[0] * c for _ in range(r)]
        for i in range(m * n):
            reshaped[i // c][i % c] = nums[i // n][i % n]   # / to //

        return reshaped
