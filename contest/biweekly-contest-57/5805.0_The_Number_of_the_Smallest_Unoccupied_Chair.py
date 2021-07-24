'''
60 / 60 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 19.4 MB
提交时间：1 小时前
'''
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrival = deque(sorted([(time[0], i) for i, time in enumerate(times)]))
        leaving = deque(sorted([(time[1], i) for i, time in enumerate(times)]))
        unused = deque([])
        occupied = {}
        curr = 0
        
        for ar, i in arrival:
            
            while ar >= leaving[0][0]:
                le, j = leaving.popleft()
                # unused.append()  # wrong
                bisect.insort(unused, occupied[j])
            if unused:
                occupied[i] = unused.popleft()
            else:
                occupied[i] = curr
                curr += 1
                
            if i == targetFriend:
                return occupied[i]
            

