'''
BFS,T:O(N),S:O(N)

执行用时：384 ms, 在所有 Python3 提交中击败了53.68% 的用户
内存消耗：29.1 MB, 在所有 Python3 提交中击败了34.74% 的用户
'''

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        q = deque([(0, 0)])   # (start_index, steps)
        seen = set([0])   # seen indices

        same = defaultdict(list)
        for i, num in enumerate(arr):
            same[num].append(i)
        
        while q:
            cur, steps = q.popleft()
            if N - 1 == cur:
                return steps
            seen.add(cur)
            # append
            if cur - 1 >= 0 and cur - 1 not in seen:
                q.append((cur - 1, steps + 1))
            if cur + 1 < N and cur + 1 not in seen:
                q.append((cur + 1, steps + 1))
            for i in same[arr[cur]]:
                if i != cur and i not in seen:
                    q.append((i, steps + 1))

            same[arr[cur]] = []  # to avoid TLE

        return -1


'''
BFS,T:O(N),S:O(N)

执行用时：544 ms, 在所有 Python3 提交中击败了42.11% 的用户
内存消耗：29.1 MB, 在所有 Python3 提交中击败了34.74% 的用户
'''

from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        q = deque([(0, 0)])   # (start_index, steps)
        seen = set([0])   # seen indices

        same = defaultdict(list)
        for i, num in enumerate(arr):
            same[num].append(i)
        
        while q:
            cur, steps = q.popleft()
            if N - 1 == cur:
                return steps
            seen.add(cur)
            # append
            for j in [cur - 1, cur + 1] + same[arr[cur]]:
                if 0 <= j < N and j not in seen:
                    q.append((j, steps + 1))

            same[arr[cur]] = []  # to avoid TLE

        return -1

'''
BFS,T:O(N),S:O(N)

执行用时：272 ms, 在所有 Python3 提交中击败了62.50% 的用户
内存消耗：29.5 MB, 在所有 Python3 提交中击败了46.53% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        num2indices = defaultdict(list)
        for i, x in enumerate(arr):
            num2indices[x].append(i)
        seen = set([0])
        q = deque([0])
        step = 0
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == n - 1:
                    return step 
                v = arr[idx]
                for nxt_idx in [idx - 1, idx + 1]:
                    if 0 <= nxt_idx < n and nxt_idx not in seen:
                        seen.add(nxt_idx)
                        q.append(nxt_idx)
                for nxt_idx in num2indices[v]:
                    if nxt_idx not in seen:
                        seen.add(nxt_idx)
                        q.append(nxt_idx)
                num2indices[v].clear()
            step += 1

        return -1


'''
Bidirectional BFS,T:O(N),S:O(N)

执行用时：172 ms, 在所有 Python3 提交中击败了95.14% 的用户
内存消耗：29.4 MB, 在所有 Python3 提交中击败了49.31% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        num2indices = defaultdict(list)
        for i, x in enumerate(arr):
            num2indices[x].append(i)

        head = set([0])
        tail = set([n - 1])
        seen = set([0, n - 1])
        step = 0
        while head or tail:
            if len(head) > len(tail):
                head, tail = tail, head 
            now = set()
            for node in head:
                if node in tail:
                    return step 
                for nxt_idx in chain([node - 1, node + 1], num2indices[arr[node]]):
                    if nxt_idx in tail:
                        return step + 1
                    if 0 <= nxt_idx < n and nxt_idx not in seen:
                        seen.add(nxt_idx)
                        now.add(nxt_idx)
                num2indices[arr[node]].clear()
            head = now 
            step += 1

        return -1



