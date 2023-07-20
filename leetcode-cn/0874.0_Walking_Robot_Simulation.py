'''
simulation

执行用时：96 ms, 在所有 Python3 提交中击败了96.67% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了38.33% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = x = y = direction = 0
        # delta for direction
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacles = set(tuple(o) for o in obstacles)

        for command in commands:
            if -2 == command:
                direction -= 1
                direction %= 4
            elif -1 == command:
                direction += 1
                direction %= 4
            else:
                # move 
                dx, dy = delta[direction]
                while command and (x + dx, y + dy) not in obstacles:
                    x += dx 
                    y += dy
                    command -= 1
                ans = max(ans, x * x + y * y)

        return ans 

'''
执行用时：104 ms, 在所有 Python3 提交中击败了85.00% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了35.00% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = x = y = direction = 0
        # delta for direction
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        obstacles = set(tuple(o) for o in obstacles)

        for command in commands:
            if command < 0:
                direction += 1 if -1 == command else -1
                direction %= 4
            else:
                dx, dy = delta[direction]
                while command and (x + dx, y + dy) not in obstacles:
                    x += dx 
                    y += dy
                    command -= 1
                ans = max(ans, x * x + y * y)

        return ans 


'''
执行用时：108 ms, 在所有 Python3 提交中击败了80.00% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了48.33% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = x = y = direction = 0
        # delta for direction
        # delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        delta = [0, 1, 0, -1, 0]
        obstacles = set(tuple(o) for o in obstacles)

        for command in commands:
            if command < 0:
                direction += 1 if -1 == command else -1
                direction %= 4
            else:
                dx, dy = delta[direction], delta[direction + 1]
                while command and (x + dx, y + dy) not in obstacles:
                    x += dx 
                    y += dy
                    command -= 1
                ans = max(ans, x * x + y * y)

        return ans 

