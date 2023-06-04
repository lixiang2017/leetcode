'''
执行用时：40 ms, 在所有 Python3 提交中击败了52.34% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了32.71% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        distinct = set()
        while i < j:
            distinct.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(distinct)

'''
执行用时：28 ms, 在所有 Python3 提交中击败了96.73% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了19.16% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return len(set(nums[i] + nums[n - i - 1] for i in range(n // 2)))

