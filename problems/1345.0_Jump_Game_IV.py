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
        
        
