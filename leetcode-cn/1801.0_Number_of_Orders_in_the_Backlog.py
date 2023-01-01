'''
max heap + min heap
股票市场的撮合交易

执行用时：176 ms, 在所有 Python3 提交中击败了55.95% 的用户
内存消耗：38.9 MB, 在所有 Python3 提交中击败了23.81% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # max heap, min heap
        buy, sell = [], []
        MOD = 10 ** 9 + 7
        for p, a, t in orders:
            if t == 0: # buy
                while sell and sell[0][0] <= p and a > 0:
                    sell_p, sell_a = heappop(sell)
                    if sell_a > a:
                        sell_a -= a 
                        a = 0
                        heappush(sell, [sell_p, sell_a])
                        break 
                    elif sell_a <= a:
                        a -= sell_a 
                if a > 0:
                    heappush(buy, [-p, a])
            else: # sell
                while buy and -buy[0][0] >= p and a > 0:
                    neg_buy_p, buy_a = heappop(buy)
                    buy_p = -neg_buy_p
                    if buy_a > a:
                        buy_a -= a 
                        a = 0
                        heappush(buy, [-buy_p, buy_a])
                        break 
                    elif buy_a <= a:
                        a -= buy_a
                if a > 0:
                    heappush(sell, [p, a])
        
        return sum([sell_a for sell_p, sell_a in sell] + [buy_a for neg_buy_p, buy_a in buy]) % MOD 

