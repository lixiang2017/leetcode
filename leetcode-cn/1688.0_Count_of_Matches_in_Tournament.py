'''
执行用时：48 ms, 在所有 Python3 提交中击败了8.97% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了9.73% 的用户
通过测试用例：200 / 200
'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += (n // 2)
            if n % 2 == 0:
                n //= 2
            else:
                n //= 2
                n += 1

        return ans


'''
执行用时：40 ms, 在所有 Python3 提交中击败了8.97% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.89% 的用户
通过测试用例：200 / 200
'''
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
        