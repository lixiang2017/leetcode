'''
执行用时：1336 ms, 在所有 Python3 提交中击败了31.58% 的用户
内存消耗：34.4 MB, 在所有 Python3 提交中击败了55.26% 的用户
通过测试用例：108 / 108
'''
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # process cnt 
        cnt = [0] * k 
        # available server set
        available_set = SortedList(range(k))
        # heap  (end_time, server_idx)
        h = []

        for i, ar in enumerate(arrival):
            # release reachable server
            while h and h[0][0] <= ar:
                done_time, server_idx = heappop(h)
                available_set.add(server_idx)
            if len(available_set) == 0:
                continue
            idx = available_set.bisect_left(i % k)
            if idx == len(available_set):
                idx = 0
            # handled, server_id
            sid = available_set[idx]
            end = ar + load[i]
            available_set.remove(sid)
            heappush(h, (end, sid))
            cnt[sid] += 1

        maxc = max(cnt)
        return [sid for sid, c in enumerate(cnt) if c == maxc]

