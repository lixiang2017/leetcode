'''
执行用时：244 ms, 在所有 Python3 提交中击败了11.30% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了59.59% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(reduce(max, n)), 1) 

'''
均是正数

执行用时：176 ms, 在所有 Python3 提交中击败了28.42% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了68.84% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(reduce(max, n))


'''
执行用时：224 ms, 在所有 Python3 提交中击败了11.99% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了30.82% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        m = '1'
        for ch in n:
            m = max(m, ch)
            if m == '9':
                return 9
        return int(m)

