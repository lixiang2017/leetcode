'''
approach: Mono Stack
Time: O(N)
Space: O(N)

执行用时：472 ms, 在所有 Python 提交中击败了38.46%的用户
内存消耗：17.4 MB, 在所有 Python 提交中击败了30.16%的用户
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        N = len(T)
        days = [0] * N
        stack = []
        for i in range(N):
            while stack and T[i] > T[stack[-1]]:   
                idx = stack.pop()
                days[idx] = i - idx
            stack.append(i)

        return days


'''
monotonic stack
Time: O(N)
Space: O(N)

执行用时：196 ms, 在所有 Python3 提交中击败了57.50% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了26.12% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        wait = [0] * N
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                pre = stack.pop()
                wait[pre] = i - pre
            stack.append(i)
        return wait 
