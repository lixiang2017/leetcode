'''
one pass
T: O(N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了78.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了78.26% 的用户
通过测试用例：122 / 122
'''
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # w cnt
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1

        ans = w 
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            if w < ans:
                ans = w 
            if ans == 0:
                return 0
        return ans 
