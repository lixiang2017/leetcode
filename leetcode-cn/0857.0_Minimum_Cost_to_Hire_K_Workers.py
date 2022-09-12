'''
Greedy + Priority Queue + Sort
T: O(NlogN + NlogK)
S: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了92.45% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了67.92% 的用户
通过测试用例：46 / 46
'''
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key = lambda p: p[1] / p[0])
        ans, h, totalq = inf, [], 0
        for q, w in pairs[: k - 1]:
            totalq += q 
            heappush(h, -q)
        for q, w in pairs[k - 1: ]:
            totalq += q 
            heappush(h, -q)
            ans = min(ans, totalq * w / q)
            totalq += heappop(h)
        return ans 
