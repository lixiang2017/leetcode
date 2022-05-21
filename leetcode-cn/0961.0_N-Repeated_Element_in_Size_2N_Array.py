'''
bit manipulation

执行用时：40 ms, 在所有 Python3 提交中击败了88.68% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了89.84% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        b = 0
        for x in nums:
            if b >> x & 1:
                return x 
            b |= 1 << x

'''
hash set

执行用时：36 ms, 在所有 Python3 提交中击败了97.00% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了37.18% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen =  set()
        for x in nums:
            if x in seen:
                return x 
            seen.add(x)
