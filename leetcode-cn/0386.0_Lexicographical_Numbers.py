'''
执行用时：52 ms, 在所有 Python3 提交中击败了90.64% 的用户
内存消耗：21.4 MB, 在所有 Python3 提交中击败了17.31% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)


'''
执行用时：40 ms, 在所有 Python3 提交中击败了99.49% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了93.21% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        x = 1
        for _ in range(n):
            ans.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                while x % 10 == 9 or x + 1 > n:
                    x //= 10
                x += 1
                
        return ans 


'''
执行用时：48 ms, 在所有 Python3 提交中击败了94.87% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了96.79% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        x = 1
        for i in range(n):
            ans[i] = x
            if x * 10 <= n:
                x *= 10
            else:
                while x % 10 == 9 or x + 1 > n:
                    x //= 10
                x += 1

        return ans 

