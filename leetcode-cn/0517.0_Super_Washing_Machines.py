'''
执行用时：40 ms, 在所有 Python3 提交中击败了79.78% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：120 / 120
'''
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        N = len(machines)
        avg, remainder = divmod(total, N)
        if remainder:
            return -1   

        ans = presum = 0
        for m in machines:
            diff = m - avg
            presum += diff
            ans = max(ans, abs(presum), diff)
        return ans

'''
输入：
[4,0,0,4]
输出：
4
预期结果：
2
'''
