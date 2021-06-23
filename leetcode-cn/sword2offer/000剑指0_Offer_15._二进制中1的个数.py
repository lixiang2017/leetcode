'''
执行用时：44 ms, 在所有 Python3 提交中击败了46.65% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.24% 的用户
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

'''
执行用时：36 ms, 在所有 Python3 提交中击败了88.19% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了43.86% 的用户
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n - 1) 
            cnt += 1
        return cnt


'''
执行用时：60 ms, 在所有 Python3 提交中击败了9.27% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.24% 的用户
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return 0 if n <= 0 else 1 + self.hammingWeight(n & (n - 1))
                