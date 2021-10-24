'''
backtracking

64 / 64 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 15.2 MB
提交时间：15 分钟前
'''
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        optimal = reduce(operator.add, [p * n for p, n in zip(price, needs)])
        special = [s for s in special if all(ss <= n for ss, n in zip(s, needs))]

        def backtracking(cost, to_buy):
            nonlocal optimal
            if cost >= optimal:
                return 
            if set(to_buy) == {0}:
                optimal = min(optimal, cost)
                return
            # special buy
            for s in special:
                if all(ss <= t for ss, t in zip(s, to_buy)):
                    backtracking(cost + s[-1], [t - ss for ss, t in zip(s, to_buy)])
            # normal buy
            backtracking(cost + reduce(operator.add, [p * t for p, t in zip(price, to_buy)]), [0 for _ in range(len(to_buy))])

        backtracking(0, needs)
        return optimal


'''
backtracking

执行用时：52 ms, 在所有 Python3 提交中击败了90.20% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了49.51% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        optimal = reduce(operator.add, [p * n for p, n in zip(price, needs)])
        special = [s for s in special if all(ss <= n for ss, n in zip(s, needs))]

        def backtracking(cost, to_buy):
            nonlocal optimal
            if cost >= optimal:
                return 
            if set(to_buy) == {0}:
                optimal = min(optimal, cost)
                return
            # special buy
            for s in special:
                if all(ss <= t for ss, t in zip(s, to_buy)):
                    backtracking(cost + s[-1], [t - ss for ss, t in zip(s, to_buy)])
            # normal buy
            backtracking(cost + reduce(operator.add, [p * t for p, t in zip(price, to_buy)]), [0])

        backtracking(0, needs)
        return optimal


'''
sum
backtracking

执行用时：56 ms, 在所有 Python3 提交中击败了76.47% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了82.35% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        optimal = sum(p * n for p, n in zip(price, needs))
        special = [s for s in special if all(ss <= n for ss, n in zip(s, needs))]

        def backtracking(cost, to_buy):
            nonlocal optimal
            if cost >= optimal:
                return 
            if set(to_buy) == {0}:
                optimal = min(optimal, cost)
                return
            # special buy
            for s in special:
                if all(ss <= t for ss, t in zip(s, to_buy)):
                    backtracking(cost + s[-1], [t - ss for ss, t in zip(s, to_buy)])
            # normal buy
            backtracking(cost + sum(p * t for p, t in zip(price, to_buy)), [0])

        backtracking(0, needs)
        return optimal

