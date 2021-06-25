'''
BFS + Hash Set

执行用时：644 ms, 在所有 Python3 提交中击败了80.02% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了21.75% 的用户
'''


from typing import Generator

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' == target:
            return 0
        dead = set(deadends)
        if '0000' in dead or target in dead:
            return -1
        
        def num_prev(x: str) -> str:
            return '9' if '0' == x else str(int(x) - 1)
        
        def num_succ(x: str) -> str:
            return '0' if '9' == x else str(int(x) + 1)

        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            for i in range(4):
                x = s[i]
                s[i] = num_prev(x)
                yield ''.join(s)
                s[i] = num_succ(x)
                yield ''.join(s)
                s[i] = x
        
        q = deque([('0000', 0)])
        seen = {'0000'} # seen = set(['0000'])
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append([next_status, step + 1])
                    seen.add(next_status)
        return -1
