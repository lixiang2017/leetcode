'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了63.83%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了11.17%的用户
'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max([sum(account) for account in accounts])


'''
执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了96.35%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了74.82%的用户
'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return sum(max(accounts, key=lambda account: sum(account)))


'''
执行用时：36 ms, 在所有 Python3 提交中击败了70.09% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.36% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)




