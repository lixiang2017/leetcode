'''
Stack / Monotonic Stack
T: O(1)
S: O(N)

Runtime: 698 ms, faster than 13.25% of Python3 online submissions for Online Stock Span.
Memory Usage: 18.9 MB, less than 84.11% of Python3 online submissions for Online Stock Span.
'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0
        self.pre_idx = 0
        
    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            self.pre_idx = self.stack[-1][1] + 1    
        else:
            self.pre_idx = 0
        self.stack.append([price, self.idx])
        self.idx += 1
        return self.idx - self.pre_idx
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


'''

Input: ["StockSpanner","next","next","next","next","next"]
[[],[31],[41],[48],[59],[79]]
Output: [null,1,2,2,2,2]
Expected: [null,1,2,3,4,5]
'''



'''
                                    --cnt5--
    --cnt1--
            --cnt2--
                    --cnt3--

                            --cnt4--


Runtime: 520 ms, faster than 34.70% of Python3 online submissions for Online Stock Span.
Memory Usage: 19.2 MB, less than 16.18% of Python3 online submissions for Online Stock Span.
'''
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1]
        self.stack.append([price, cnt])
        return cnt
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


