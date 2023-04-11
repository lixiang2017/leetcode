'''
执行用时：56 ms, 在所有 Python3 提交中击败了7.55% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.49% 的用户
通过测试用例：116 / 116
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 1 2 3
        # ds = ['N', 'W', 'S', 'E']
        # x, y, d = 0, 0, 0

        def try_round(x, y, d, time):
            max_dist = 0
            for _ in range(time):
                for ch in instructions:
                    if ch == 'G':
                        if d == 0:
                            y += 1
                        elif d == 1:
                            x -= 1
                        elif d == 2:
                            y -= 1
                        elif d == 3:
                            x += 1
                    elif ch == 'L':
                        d += 1
                        d %= 4
                    else:
                        d -= 1
                        d %= 4
                    max_dist = max(max_dist, x * x + y * y)
            return max_dist
                
        m4 = try_round(0, 0, 0, 4)
        m8 = try_round(0, 0, 0, 8)
        return m4 == m8


'''
执行用时：40 ms, 在所有 Python3 提交中击败了42.45% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了70.75% 的用户
通过测试用例：116 / 116
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = d = 0
        for _ in range(4):
            for ch in instructions:
                if ch == 'G':
                    if d == 0:
                        y += 1
                    elif d == 1:
                        x -= 1
                    elif d == 2:
                        y -= 1
                    elif d == 3:
                        x += 1
                elif ch == 'L':
                    d += 1
                    d %= 4
                else:
                    d -= 1
                    d %= 4
        return x == 0 and y == 0



'''
only one round

执行用时：44 ms, 在所有 Python3 提交中击败了23.58% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.21% 的用户
通过测试用例：116 / 116
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = d = 0
        for ch in instructions:
            if ch == 'G':
                if d == 0:
                    y += 1
                elif d == 1:
                    x -= 1
                elif d == 2:
                    y -= 1
                elif d == 3:
                    x += 1
            elif ch == 'L':
                d += 1
                d %= 4
            else:
                d -= 1
                d %= 4
        return x == 0 and y == 0 or d != 0
