'''
DP
T: O(3N)
S: O(N)

执行用时：408 ms, 在所有 Python3 提交中击败了19.35% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了25.00% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # R . . L
        # RRRR....RRRRR...RRRR...
        n = len(dominoes)
        f = 0
        force = [0] * n 
        for i, d in enumerate(dominoes):
            if d == 'L':
                f = 0 
            elif d == 'R':
                f = n 
            else:
                f = max(f - 1, 0)
            force[i] += f
 
        j = n - 1
        f = 0
        while j >= 0:
            d = dominoes[j] 
            if d == 'L':
                f = n
            elif d == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[j] -= f    

            j -= 1

        return ''.join('R' if f > 0 else 'L' if f < 0 else '.' for f in force)


