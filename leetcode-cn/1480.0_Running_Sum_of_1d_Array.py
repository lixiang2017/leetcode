'''
执行用时：44 ms, 在所有 Python3 提交中击败了51.48% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.25% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)

'''
执行用时：36 ms, 在所有 Python3 提交中击败了88.92% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.98% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)




'''
执行用时：36 ms, 在所有 Python3 提交中击败了88.92% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.25% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        缓存 = 0
        答案 = []
        for num in nums:
            缓存 += num
            答案.append(缓存)
        return 答案
