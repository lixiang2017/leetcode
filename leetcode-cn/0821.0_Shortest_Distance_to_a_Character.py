'''
two passes
T: O(2N)
S: O(N)

执行用时：32 ms, 在所有 Python3 提交中击败了97.71% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了40.59% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        left_idx, right = -2 * n, [2 * n] * n 
        right_idx = 2 * n 
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                right_idx = i 
            right[i] = right_idx 
        
        ans = []
        for i in range(n):
            if s[i] == c:
                left_idx = i 
            ans.append(min(abs(left_idx - i), abs(right[i] - i)))
        return ans 


'''
two passes
T: O(2N)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了61.05% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.07% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        left_idx = -n
        for i in range(n):
            if s[i] == c:
                left_idx = i 
            ans[i] = abs(left_idx - i)
        right_idx = 2 * n 
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                right_idx = i 
            ans[i] = min(ans[i], abs(right_idx - i))
        return ans 
