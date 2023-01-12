'''
simulation + hash table

执行用时：44 ms, 在所有 Python3 提交中击败了20.75% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了20.75% 的用户
通过测试用例：433 / 433
'''
class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i, ch in enumerate(num):
            if c[str(i)] != int(ch):
                return False
        return True
