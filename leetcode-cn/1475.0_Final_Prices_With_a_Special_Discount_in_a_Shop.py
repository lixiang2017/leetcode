'''
monotonic stack, T: O(N), S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了73.70% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.70% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = copy.copy(prices)
        # store index, from tail to head, non-decreasing
        stack = [n - 1]
        for i in range(n - 2, -1, -1):
            while stack and prices[i] < prices[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] -= prices[stack[-1]]
            stack.append(i)
        return ans 
