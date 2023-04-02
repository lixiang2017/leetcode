'''
执行用时：36 ms, 在所有 Python3 提交中击败了82.52% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.75% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans, s = 0, set()
        for x in nums:
            if x - diff in s and x - diff - diff in s:
                ans += 1
            s.add(x)
        return ans 

'''
执行用时：36 ms, 在所有 Python3 提交中击败了82.52% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了8.88% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        ans = 0
        for x in nums:
            if x + diff in s and x + diff + diff in s:
                ans += 1
        return ans 

