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

