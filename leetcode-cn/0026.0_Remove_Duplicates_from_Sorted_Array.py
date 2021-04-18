'''
approach: Three Pointers
Time: O(N)
Space: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了63.41%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了61.43%的用户
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N

        realPtr = firstPtr = 0
        secondPtr = 1
        while secondPtr < N:
            while secondPtr < N and nums[firstPtr] == nums[secondPtr]:
                secondPtr += 1
            nums[realPtr] = nums[firstPtr]
            realPtr += 1
            firstPtr = secondPtr

        return realPtr


'''
approach: Two Pointers
Time: O(N)
Space: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了79.81%的用户内存消耗：
15.8 MB, 在所有 Python3 提交中击败了67.76%的用户
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        realPtr = movePtr = 0
        while movePtr < N:
            if nums[realPtr] == nums[movePtr]:
                movePtr += 1
            else:
                realPtr += 1
                nums[realPtr] = nums[movePtr]
                movePtr += 1

        return realPtr + 1
