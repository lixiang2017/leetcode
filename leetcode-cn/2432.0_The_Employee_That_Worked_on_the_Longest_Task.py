'''
执行用时：40 ms, 在所有 Python3 提交中击败了99.09% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了51.59% 的用户
通过测试用例：514 / 514
'''
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = longest = pre_t = 0
        for id, leavTime in logs:
            cost = leavTime - pre_t
            if cost > longest or (cost == longest and id < ans):
                ans = id
                longest = cost
            pre_t = leavTime
        return ans 


'''
执行用时：296 ms, 在所有 Python3 提交中击败了25.71% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：514 / 514
'''
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        pairs = [(-logs[0][1], logs[0][0])] + [(leave1 - leave2, id2) for (id1, leave1), (id2, leave2) in pairwise(logs)]
        pairs.sort()
        return pairs[0][1]


'''
执行用时：324 ms, 在所有 Python3 提交中击败了8.57% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：514 / 514
'''
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        pairs = [(-logs[0][1], logs[0][0])] + [(leave1 - leave2, id2) for (id1, leave1), (id2, leave2) in pairwise(logs)]
        return heapq.nsmallest(1, pairs)[0][1]


'''
执行用时：292 ms, 在所有 Python3 提交中击败了27.86% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：514 / 514
'''
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        t = 0
        return min((t - (t := x), i) for i, x in logs)[1]
        