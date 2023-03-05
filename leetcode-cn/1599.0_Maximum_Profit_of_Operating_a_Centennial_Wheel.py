'''
simulation (while), operate once each time

执行用时：928 ms, 在所有 Python3 提交中击败了41.51% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了5.66% 的用户
通过测试用例：141 / 141
'''
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = max_profit = operation = max_operation = 0
        n = len(customers)
        # current customers
        current = customers[0]
        i = 1
        while True:
            if current >= 4:
                current -= 4
                profit -= runningCost 
                profit += boardingCost * 4
            else:
                profit -= runningCost 
                profit += boardingCost * current
                current = 0
            operation += 1
            if i < n and i <= operation:
                current += customers[i]
                i += 1
            if profit > max_profit:
                max_profit = profit
                max_operation = operation
            if current == 0 and i == n:
                break 

        return -1 if max_profit <= 0 else max_operation


'''
simulation (while), operate as many times as possible

执行用时：144 ms, 在所有 Python3 提交中击败了94.34% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了7.55% 的用户
通过测试用例：141 / 141
'''
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = max_profit = operation = max_operation = 0
        n = len(customers)
        # current customers
        current = customers[0]
        i = 1
        while True:
            if current >= 4:
                fold, remain = divmod(current, 4)
                profit -= runningCost * fold 
                profit += boardingCost * fold * 4
                operation += fold 
                current = remain
            else:
                profit -= runningCost 
                profit += boardingCost * current
                current = 0
                operation += 1
            while i < n and i <= operation:
                current += customers[i]
                i += 1
            if profit > max_profit:
                max_profit = profit
                max_operation = operation
            if current == 0 and i == n:
                break 

        return -1 if max_profit <= 0 else max_operation


