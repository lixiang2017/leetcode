'''
执行用时：60 ms, 在所有 Python3 提交中击败了49.86% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了18.93% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        remainder = length = 1
        while True:
            remainder %= k
            if 0 == remainder:
                return length
            elif remainder not in seen:
                seen.add(remainder)
                remainder = remainder * 10 + 1
                length += 1
            else:
                break
        return -1

            
'''
执行用时：56 ms, 在所有 Python3 提交中击败了63.57% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了38.05% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for i in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k 
            if 0 == remainder:
                return i 
        return -1

'''
执行用时：44 ms, 在所有 Python3 提交中击败了95.40% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了78.24% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5:
            return -1
        remainder = 0
        for i in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k 
            if 0 == remainder:
                return i 
                