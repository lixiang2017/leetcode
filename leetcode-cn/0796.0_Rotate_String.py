'''
执行用时：36 ms, 在所有 Python3 提交中击败了55.06% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.29% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        sn, gn = len(s), len(goal)
        if sn != gn:
            return False
        for i in range(sn):
            if s[i: ] + s[: i] == goal:
                return True
        return False

'''
执行用时：44 ms, 在所有 Python3 提交中击败了9.39% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了69.65% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s 
        