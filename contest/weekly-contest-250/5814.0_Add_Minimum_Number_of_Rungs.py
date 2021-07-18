'''
Accepted
'''
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ladder = 0
        N = len(rungs)
        for i in range(N):
            pre = 0 if 0 == i else rungs[i - 1]
            gap = rungs[i] - pre
            if gap > dist:
                ladder += (gap - 1) // dist
                
        return ladder
        