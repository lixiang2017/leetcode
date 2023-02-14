'''
Monotonic stack + prefix sum
T: O(2N)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了40.14% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0] * (n + 1)
        stack = [0]
        for i, h in enumerate(hours, 1):
            presum[i] = presum[i - 1] + (1 if h > 8 else -1)
            if presum[i] < presum[stack[-1]]:
                stack.append(i)
        ans = 0
        # i -> j
        for j in range(n, 0, -1):
            while stack and presum[stack[-1]] < presum[j]:
                ans = max(ans, j - stack.pop())
        return ans 


'''
hash table + prefix sum
T: O(N)
S: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了97.49% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了99.28% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 记录前缀和首次出现的位置
        pos = [0] * (len(hours) + 2)
        ans = s = 0
        for i, h in enumerate(hours, 1):
            # 取反，改为减法
            s -= 1 if h > 8 else -1
            if s < 0:
                ans = i 
            else:
                # 原本是 s-1, 取反改为 s+1
                if pos[s + 1]:
                    ans = max(ans, i - pos[s + 1])
                if pos[s] == 0:
                    pos[s] = i 
        return ans 
