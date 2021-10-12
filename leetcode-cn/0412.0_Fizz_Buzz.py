'''
执行用时：36 ms, 在所有 Python3 提交中击败了45.86% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了20.41% 的用户
通过测试用例：8 / 8
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            if (i + 1) % 15 == 0:
                ans.append('FizzBuzz')
            elif (i + 1) % 3 == 0:
                ans.append('Fizz')
            elif (i + 1) % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i + 1))
        return ans

