'''
approach: BFS
Hash Set + Deque, T:O(N),S:O(N)

执行用时：68 ms, 在所有 Python3 提交中击败了83.48% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了79.83% 的用户
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        N = len(arr)
        q = deque([start])

        while q:
            i = q.popleft()
            if 0 == arr[i]:
                return True
            seen.add(i)
            for new_i in (i + arr[i], i - arr[i]):
                if 0 <= new_i < N and new_i not in seen:
                    q.append(new_i)
        
        return False


'''
DFS + memo, T:O(N),S:O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了93.56% 的用户
内存消耗：75.5 MB, 在所有 Python3 提交中击败了27.25% 的用户
'''


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        N = len(arr)

        def dfs(cur):
            if cur < 0 or cur >= N or cur in seen:
                return False
            if 0 == arr[cur]:
                return True
            seen.add(cur)

            return dfs(cur + arr[cur]) or dfs(cur - arr[cur])
        
        return dfs(start)
