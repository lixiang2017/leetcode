'''
math

执行用时：32 ms, 在所有 Python3 提交中击败了97.75% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了67.42% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ## pattern: aaa...aa?zz....z
        #            x          y = n - 1 - x
        # x * 1 + ? + (n - x - 1) * 26 = k
        # (26 * (n - 1) - k + ?) // 25 = x
        if 26 * n == k:
            return 'z' * n 
            
        t = 26 * (n - 1) - k
        a, r = divmod(t, 25) 
        x = a + 1
        y = n - 1 - x 
        question = 25 - r 
        return 'a' * x + chr(question + ord('a') - 1) + 'z' * y


