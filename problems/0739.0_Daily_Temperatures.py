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
