'''
执行用时：36 ms, 在所有 Python3 提交中击败了63.08% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.73% 的用户
通过测试用例：42 / 42
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n-1)//2, 0)) + list(range(1, n//2 + 1)) + ([0] if n % 2 else [])

'''
执行用时：36 ms, 在所有 Python3 提交中击败了63.08% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了75.87% 的用户
通过测试用例：42 / 42
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # (1 - n, n, 2)   
        # n=6,  -5, -3, -1, 1, 3, 5 
        # n=5,  -4, -2, 0, 2, 4
        # n=1,  0
        return list(range(1 - n, n, 2))

