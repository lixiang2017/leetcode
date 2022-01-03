'''
T: O(T + 3 * N)
S: O(2 * N)

Runtime: 1250 ms, faster than 5.72% of Python3 online submissions for Find the Town Judge.
Memory Usage: 18.9 MB, less than 65.18% of Python3 online submissions for Find the Town Judge.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = set(range(1, n + 1))
        cnt = [0] * (n + 1)
        for a, b in trust:
            candidates.discard(a)
            cnt[b] += 1
        candidates = list(filter(lambda cand: cnt[cand] == n - 1, candidates))
        
        if len(candidates) == 1:
            return candidates[0]
        else:
            return -1


'''
directed graph
T: O(T + 3 * N)
S: O(2 * N)

Runtime: 948 ms, faster than 14.22% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19 MB, less than 65.18% of Python3 online submissions for Find the Town Judge.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree, in_degree = [0] * (n + 1), [0] * (n + 1)
        # a -> b
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        return -1

'''
directed graph
T: O(T + 2 * N)
S: O(N)

Runtime: 1449 ms, faster than 5.04% of Python3 online submissions for Find the Town Judge.
Memory Usage: 19 MB, less than 65.18% of Python3 online submissions for Find the Town Judge.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # out_degree, in_degree = [0] * (n + 1), [0] * (n + 1)
        # in_degree - out_degree == n - 1
        degree = [0] * (n + 1)
        # a -> b
        for a, b in trust:
            degree[a] -= 1
            degree[b] += 1
        for i in range(1, n + 1):
            if degree[i] == n - 1:
                return i
        return -1

