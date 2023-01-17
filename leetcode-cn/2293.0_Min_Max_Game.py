'''
simulation, iteration

执行用时：40 ms, 在所有 Python3 提交中击败了76.55% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了85.52% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            i = 0
            newNums = []
            while 2 * i + 1 < len(nums):
                if i & 1:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                i += 1
            nums = newNums
        return nums[0]

'''
recursive

执行用时：44 ms, 在所有 Python3 提交中击败了48.28% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了45.52% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        def recursive(nums: List[int]) -> int: 
            if len(nums) == 1:
                return nums[0]
            i = 0
            newNums = []
            while 2 * i + 1 < len(nums):
                if i & 1:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                i += 1
            return recursive(newNums)

        return recursive(nums)


'''
执行用时：32 ms, 在所有 Python3 提交中击败了97.93% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了90.34% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = 0
        newNums = []
        while 2 * i + 1 < len(nums):
            if i & 1:
                newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            else:
                newNums.append(min(nums[2 * i], nums[2 * i + 1]))
            i += 1
        return self.minMaxGame(newNums)


'''
执行用时：48 ms, 在所有 Python3 提交中击败了22.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了27.59% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n != 1:
            m = n // 2
            for i in range(m):
                if i & 1:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
            n = m
        return nums[0]

        
