'''
approach: XOR
Time: O(N)
Space: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了83.74%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了82.44%的用户
'''



class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(n - 1):
            start += 2
            ans ^= start
        return ans
