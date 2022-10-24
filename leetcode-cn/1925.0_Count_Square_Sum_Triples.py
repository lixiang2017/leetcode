'''
hash set 

执行用时：184 ms, 在所有 Python3 提交中击败了84.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.06% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def countTriples(self, n: int) -> int:
        square = {i * i for i in range(1, n + 1)}
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i * i + j * j in square:
                    ans += 1
        return ans 


'''
执行用时：296 ms, 在所有 Python3 提交中击败了75.55% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了25.18% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def countTriples(self, n: int) -> int:
        square = {i * i for i in range(1, n + 1)}
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                _sum = i * i + j * j
                if _sum > (n + 1) * (n + 1):
                    break
                if _sum in square:
                    ans += 1
        return ans 
