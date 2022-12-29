'''
sort + heap

Runtime: 2303 ms, faster than 71.81% of Python3 online submissions for Single-Threaded CPU.
Memory Usage: 63.5 MB, less than 9.34% of Python3 online submissions for Single-Threaded CPU.
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [t + [i] for i, t in enumerate(tasks)]
        n = len(tasks)
        tasks.sort()
        order = []
        now = -1
        h = []
        idx = 0

        while idx < n or h:
            while idx < n and tasks[idx][0] <= now:
                enTime, proTime, i = tasks[idx]
                heappush(h, [proTime, i, enTime])
                idx += 1
            if h:
                proTime, i, enTime = heappop(h)
                order.append(i)
                now += proTime
            else: 
                enTime, proTime, i = tasks[idx]
                order.append(i)
                if now >= enTime:
                    now += proTime
                else:
                    now = enTime + proTime
                idx += 1
        return order

        