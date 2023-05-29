'''
执行用时：76 ms, 在所有 Python3 提交中击败了47.30% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了28.22% 的用户
通过测试用例：181 / 181
'''
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = cnt = 0
        for x in nums:
            if x % 6 == 0:
                total += x 
                cnt += 1
        return 0 if cnt == 0 else total // cnt 

'''
执行用时：80 ms, 在所有 Python3 提交中击败了40.66% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了25.31% 的用户
通过测试用例：181 / 181
'''
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        return 0 if len(targets := [x for x in nums if x % 6 == 0]) == 0 else sum(targets) // len(targets)

