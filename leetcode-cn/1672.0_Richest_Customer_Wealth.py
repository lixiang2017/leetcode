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
        