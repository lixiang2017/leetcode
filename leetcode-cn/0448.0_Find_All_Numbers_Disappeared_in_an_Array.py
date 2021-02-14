'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：328 ms, 在所有 Python 提交中击败了74.63%的用户
内存消耗：23.7 MB, 在所有 Python 提交中击败了21.78%的用户
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = defaultdict(int)
        size = len(nums)
        for num in nums:
            seen[num] = 1
        
        disappeared = []
        for i in range(1, size + 1):
            if not seen[i]:
                disappeared.append(i)

        return disappeared




'''
approach: Modify in place, by the use of index
Time: O(N + N) = O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：320 ms, 在所有 Python 提交中击败了83.30%的用户
内存消耗：
20.4 MB, 在所有 Python 提交中击败了43.77%的用户
'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        for num in nums:
            nums[(num - 1) % size] += size

        return [i + 1 for i, num in enumerate(nums) if num <= size]


'''
approach: Modify in place, by the use if index
Time: O(N + N) = O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：364 ms, 在所有 Python 提交中击败了30.87%的用户
内存消耗：20.1 MB, 在所有 Python 提交中击败了72.52%的用户
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        
        disappeared = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared.append(i + 1)

        return disappeared


'''
approach: Modify in place, by the use if index
Time: O(N + N) = O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：344 ms, 在所有 Python 提交中击败了58.30%的用户
内存消耗：20.2 MB, 在所有 Python 提交中击败了62.35%的用户
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        for num in nums:
            if nums[(num - 1) % size] > 0:
                nums[(num - 1) % size] -= size
        
        disappeared = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared.append(i + 1)

        return disappeared

