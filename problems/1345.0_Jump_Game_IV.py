'''
### !!! clear the list
BFS

Runtime: 776 ms, faster than 35.13% of Python3 online submissions for Jump Game IV.
Memory Usage: 29.2 MB, less than 50.69% of Python3 online submissions for Jump Game IV.
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        val2indice = defaultdict(list)
        for i, x in enumerate(arr):
            val2indice[x].append(i)
        n = len(arr)
        if n == 1:
            return 0
        # (idx, step)
        q = deque([(0, 0)])
        # seen indice
        seen = set([0])
        while q:
            idx, step = q.popleft()
            for nxt_idx in chain([idx - 1, idx + 1], val2indice[arr[idx]]):
                if 0 <= nxt_idx < n and nxt_idx not in seen:
                    if nxt_idx == n - 1:
                        return step + 1
                    q.append((nxt_idx, step + 1))
                    seen.add(nxt_idx)
            # clear list
            val2indice[arr[idx]] = []
        return -1
        
        
'''
BFS

Runtime: 739 ms, faster than 89.92% of Python3 online submissions for Jump Game IV.
Memory Usage: 29.3 MB, less than 40.00% of Python3 online submissions for Jump Game IV.
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # x -> indice
        indice = defaultdict(list)
        for i, x in enumerate(arr):
            indice[x].append(i)
        n = len(arr)
        # seen indice
        seen = {0}
        # (idx, jump)
        q = deque([(0, 0)])
        while q:
            idx, jump = q.popleft()
            if idx == n - 1:
                return jump
            if idx - 1 >= 0 and idx - 1 not in seen:
                seen.add(idx - 1)
                q.append((idx - 1, jump + 1))
            if idx + 1 < n and idx + 1 not in seen:
                seen.add(idx + 1)
                q.append((idx + 1, jump + 1))
            for neigh in indice[arr[idx]]:
                if neigh not in seen:
                    seen.add(neigh)
                    q.append((neigh, jump + 1))
            # clear list !!!!!!  no need to check next time
            indice[arr[idx]] = []
        return -1

