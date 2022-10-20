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
        