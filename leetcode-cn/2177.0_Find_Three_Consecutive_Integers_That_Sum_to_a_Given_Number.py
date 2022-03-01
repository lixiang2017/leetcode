'''
执行用时：48 ms, 在所有 Python3 提交中击败了10.18% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.61% 的用户
通过测试用例：379 / 379
'''
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        else:
            x = num // 3
            return [x - 1, x, x + 1]
            
            