'''
执行用时：36 ms, 在所有 Python3 提交中击败了73.20% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了66.01% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        # same rank
        max_cnt = max(Counter(ranks).values())
        if max_cnt >= 3:
            return 'Three of a Kind'
        if max_cnt == 2:
            return 'Pair'
        return 'High Card'
        