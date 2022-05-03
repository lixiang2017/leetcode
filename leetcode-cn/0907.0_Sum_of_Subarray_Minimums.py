'''
如果有相等的情况，影响力可以扩散。所以有一侧的相等可以放行


执行用时：456 ms, 在所有 Python3 提交中击败了5.07% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了5.06% 的用户
通过测试用例：87 / 87
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        left = [0] * n 
        right = [n - 1] * n 

        # increasing stack, (x, idx)
        left_stack = []
        for i, x in enumerate(arr):
            while left_stack and x <= left_stack[-1][0]:  # 放行
                left_stack.pop()
            if left_stack:
                left[i] = left_stack[-1][1] + 1
            left_stack.append((x, i))
        
        # increasing stack, (x, idx)
        right_stack = []
        for i in range(n - 1, -1, -1):
            x = arr[i]
            while right_stack and x < right_stack[-1][0]:  # 不放行
                right_stack.pop()
            if right_stack:
                right[i] = right_stack[-1][1] - 1
            right_stack.append((x, i))

        ans = 0
        for i, x in enumerate(arr):
            ans += (right[i] - i + 1) * (i - left[i] + 1) * x
            ans %= MOD 
        return ans 


'''
[71,55,82,55]
'''