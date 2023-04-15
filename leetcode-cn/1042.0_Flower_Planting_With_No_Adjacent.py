'''
graph

执行用时：144 ms, 在所有 Python3 提交中击败了20.90% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了36.57% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = defaultdict(list)
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            if t:
                continue
            seen = {ans[neigh] for neigh in g[i] if ans[neigh] != 0}
            for x in range(1, 5):
                if x not in seen:
                    ans[i] = x 
                    break

        return ans 


'''
g = [[] for _ in range(n)]

执行用时：100 ms, 在所有 Python3 提交中击败了82.84% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了47.01% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            seen = {ans[neigh] for neigh in g[i] if ans[neigh] != 0}
            for x in range(1, 5):
                if x not in seen:
                    ans[i] = x 
                    break

        return ans 


'''
执行用时：112 ms, 在所有 Python3 提交中击败了65.67% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了33.58% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = defaultdict(list)
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            ans[i] = ({1, 2, 3, 4} - {ans[j] for j in g[i]}).pop()
        return ans 


'''
执行用时：100 ms, 在所有 Python3 提交中击败了82.84% 的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了49.25% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [6] * n
        g = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            mask = 0
            for j in g[i]:
                mask |= 1 << (ans[j] - 1)
            mask = (~mask) & 15
            ans[i] = ((mask & -mask) - 1).bit_count() + 1
        return ans 

'''
执行用时：84 ms, 在所有 Python3 提交中击败了99.25% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了46.27% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            mask = 1
            for j in g[i]:
                mask |= 1 << ans[j]
            mask = ~mask
            ans[i] = ((mask & -mask) - 1).bit_count()
        return ans 
        
'''
执行用时：100 ms, 在所有 Python3 提交中击败了82.84% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了61.94% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
        for i, t in enumerate(ans):
            mask = 1
            for j in g[i]:
                mask |= 1 << ans[j]
            mask = ~mask
            ans[i] = (mask & -mask).bit_length() - 1
        return ans 
        
   