'''
sort + backtrack + mask

执行用时：44 ms, 在所有 Python3 提交中击败了67.25% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了70.72% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        n = len(S)
        s = sorted(list(S))
        mask = (1 << n) - 1

        def backtrack(cur, visited):
            if visited == mask:
                ans.append(cur)
                return 
            for j in range(n):
                if visited >> j & 1 or (j > 0 and s[j - 1] == s[j] and not (visited >> (j - 1) & 1)):
                    continue
                backtrack(cur + s[j], visited | (1 << j))

        backtrack('', 0)
        return ans 

'''
BFS

执行用时：40 ms, 在所有 Python3 提交中击败了81.14% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了79.40% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        n = len(S)
        s = sorted(list(S))
        mask = (1 << n) - 1
        q = deque([('', 0)])

        while q:
            cur, visited = q.popleft()
            if visited == mask:
                ans.append(cur)
            for j in range(n):
                if visited >> j & 1 or (j > 0 and s[j - 1] == s[j] and not (visited >> (j - 1) & 1)):
                    continue
                q.append((cur + s[j], visited | (1 << j)))

        return ans 



