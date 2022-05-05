'''
约瑟夫环问题
simulation

执行用时：36 ms, 在所有 Python3 提交中击败了87.75% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.42% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = list(range(1, n + 1))
        i = 0
        while len(q) > 1:
            i = (i + k - 1) % len(q)
            del q[i]
        return q[0]


'''
iteration

执行用时：40 ms, 在所有 Python3 提交中击败了67.40% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了81.62% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        for l in range(2, n + 1):
            i = (i + k) % l 
        return i + 1


'''
recursion

执行用时：32 ms, 在所有 Python3 提交中击败了97.16% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了6.13% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n <= 1:
            return n 
        ans = (self.findTheWinner(n - 1, k) + k) % n 
        return ans if ans != 0 else n 
