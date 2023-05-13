'''
mask

执行用时：60 ms, 在所有 Python3 提交中击败了58.45% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了9.46% 的用户
通过测试用例：337 / 337
'''
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mask = [0] * 1001
        for x in nums:
            if x < 0:
                mask[-x] |= 1
            else:
                mask[x] |= 2
        for x in range(1000, 0, -1):
            if mask[x] == 3:
                return x
        return -1

'''
执行用时：64 ms, 在所有 Python3 提交中击败了52.03% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了9.12% 的用户
通过测试用例：337 / 337
'''
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        seen = set(nums)
        for x in nums:
            if x > 0 and -x in seen:
                ans = max(ans, x)
        return ans


'''
执行用时：52 ms, 在所有 Python3 提交中击败了77.70% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了9.80% 的用户
通过测试用例：337 / 337
'''
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(1000, 0, -1):
            if i in seen and -i in seen:
                return i
        return -1

'''
sort + two pointers

执行用时：52 ms, 在所有 Python3 提交中击败了77.70% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了8.78% 的用户
通过测试用例：337 / 337
'''
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == 0:
                return nums[j]
            elif s < 0:
                i += 1
            else:
                j -= 1
        return -1
