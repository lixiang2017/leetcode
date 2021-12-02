'''
heap

执行用时：44 ms, 在所有 Python3 提交中击败了22.91% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了56.06% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pos_h = [x for x in nums if x >= 0] 
        neg_h = [x for x in nums if x < 0]
        heapify(pos_h)
        heapify(neg_h)
        
        while k and neg_h:
            neg = heappop(neg_h)
            heappush(pos_h, -neg)
            k -= 1

        if k == 0:
            return sum(neg_h) + sum(pos_h)
        else:
            if k & 1:
                minx = heappop(pos_h)
                return sum(pos_h) - minx
            else:
                return sum(pos_h)


'''
heap

执行用时：36 ms, 在所有 Python3 提交中击败了61.78% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.85% 的用户
通过测试用例：80 / 80
'''

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pos_h, neg_h = [], []
        for x in nums:
            if x < 0:
                heappush(neg_h, x)
            else:
                heappush(pos_h, x)
        
        ans = 0
        neg = None
        while k and neg_h:
            neg = heappop(neg_h)
            ans -= neg
            k -= 1
        if k == 0:
            ans += sum(neg_h) + sum(pos_h)
        else:
            if k & 1:
                if pos_h:
                    minx = heappop(pos_h)
                    if neg:
                        if minx < -neg:
                            ans -= minx
                        else:
                            ans += minx + 2 * neg
                    else:
                        ans -= minx
                    ans += sum(pos_h)
                else:
                    ans += 2 * neg
            else:
                ans += sum(pos_h)
        return ans
            
'''
heapify

执行用时：28 ms, 在所有 Python3 提交中击败了94.60% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.29% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pos_h = [x for x in nums if x >= 0] 
        neg_h = [x for x in nums if x < 0]
        heapify(pos_h)
        heapify(neg_h)
        
        ans = 0
        neg = None
        while k and neg_h:
            neg = heappop(neg_h)
            ans -= neg
            k -= 1
        if k == 0:
            ans += sum(neg_h) + sum(pos_h)
        else:
            if k & 1:
                if pos_h:
                    minx = heappop(pos_h)
                    if neg:
                        if minx < -neg:
                            ans -= minx
                        else:
                            ans += minx + 2 * neg
                    else:
                        ans -= minx
                    ans += sum(pos_h)
                else:
                    ans += 2 * neg
            else:
                ans += sum(pos_h)
        return ans
            

