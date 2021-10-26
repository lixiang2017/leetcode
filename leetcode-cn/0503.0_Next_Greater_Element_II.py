'''
approach: Brute Force + Two Pointers
Time ;O(N ^ 2)
Space ;O(N)

执行用时：4920 ms, 在所有 Python 提交中击败了5.50%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        greater = []

        i = 0
        while i < N:
            j = (i + 1) % N
            visitedCount = 0
            while nums[j] <= nums[i] and visitedCount < N:
                j = (j + 1) % N
                visitedCount += 1

            if visitedCount == N:
                greater.append(-1)
            else:
                greater.append(nums[j])

            i += 1

        return greater



'''
wrong answer!
There may be duplicate elements in nums, so we CANNOT keep num in stack.

输入
[100,1,11,1,120,111,123,1,-1,-100]
输出
[120,120,120,120,123,123,-1,120,100,100]
预期结果
[120,11,120,120,123,123,-1,100,100,100]
stdout
{1: 11, 100: -1, 11: -1, 111: -1, 120: -1, 123: -1, -100: -1, -1: -1}
{1: 120, 100: -1, 11: -1, 111: -1, 120: -1, 123: -1, -100: -1, -1: -1}
{1: 120, 100: -1, 11: 120, 111: -1, 120: -1, 123: -1, -100: -1, -1: -1}
{1: 120, 100: 120, 11: 120, 111: -1, 120: -1, 123: -1, -100: -1, -1: -1}
{1: 120, 100: 120, 11: 120, 111: 123, 120: -1, 123: -1, -100: -1, -1: -1}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: -1, -1: -1}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: -1}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 100, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 11, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
{1: 120, 100: 120, 11: 120, 111: 123, 120: 123, 123: -1, -100: 100, -1: 100}
'''
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        hashMap = {num: -1 for num in nums}
        stack = []
        for i in range(2 * N):
            while stack and nums[i % N] > stack[-1]:
                hashMap[stack.pop()] = nums[i % N]
                print hashMap
            stack.append(nums[i % N])

        return [hashMap[num] for num in nums]





'''
approach: Mono Stack, keep index in stack
Time: O(2 * N) = O(N)
Space: O(N)

执行用时：196 ms, 在所有 Python 提交中击败了71.50%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了21.00%的用户
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        hashMap = [-1] * N
        stack = []
        for i in range(2 * N):
            while stack and nums[i % N] > nums[stack[-1]]:
                hashMap[stack.pop()] = nums[i % N]
            stack.append(i % N)

        return hashMap


'''
monotonic stack

执行用时：80 ms, 在所有 Python3 提交中击败了69.10% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了71.99% 的用户
通过测试用例：223 / 223
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        greater = [-1] * N 
        stack = []
        for i in range(2 * N):
            while stack and nums[stack[-1]] < nums[i % N]:
                greater[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return greater


