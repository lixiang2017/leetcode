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
