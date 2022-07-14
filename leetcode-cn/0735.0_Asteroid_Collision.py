'''
stack, T: O(N), S: O(N)

执行用时：56 ms, 在所有 Python3 提交中击败了29.37% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了67.92% 的用户
通过测试用例：275 / 275
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or a > 0:
                stack.append(a)
            elif a < 0:
                need = True
                while stack and stack[-1] > 0:
                    if stack[-1] < -a:
                        stack.pop()
                    elif stack[-1] == -a:
                        stack.pop()
                        need = False 
                        break 
                    else:
                        need = False
                        break 
                if need:
                    stack.append(a)
        return stack


