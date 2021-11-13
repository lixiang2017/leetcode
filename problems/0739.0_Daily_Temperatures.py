'''
Stack / Monotonic Stack
T: O(N)
S: O(N)

Runtime: 1629 ms, faster than 23.12% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.2 MB, less than 71.45% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        higher = [0] * N
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                top, i = stack.pop()
                higher[i] = idx - i
            stack.append((t, idx))
        return higher


'''
stack

Runtime: 1260 ms, faster than 56.41% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.4 MB, less than 46.13% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # non-increasing stack
        stack = []
        N = len(temperatures)
        ans = [0] * N
        
        for i, t in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= t:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    idx = stack.pop()
                    ans[idx] = i - idx
                stack.append(i)
        return ans
