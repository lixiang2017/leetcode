'''
hash set

执行用时：40 ms, 在所有 Python3 提交中击败了46.36% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了39.55% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        x = y = 0
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'S':
                y -= 1
            else:
                x -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
