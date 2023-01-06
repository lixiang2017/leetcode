'''
greedy + sort
T: O(NlogN)
S: O(1)

Runtime: 1060 ms, faster than 54.19% of Python3 online submissions for Maximum Ice Cream Bars.
Memory Usage: 27.9 MB, less than 61.26% of Python3 online submissions for Maximum Ice Cream Bars.
'''
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if c > coins:
                break
            else:
                coins -= c
                ans += 1
        return ans 

'''
counting sort
T: O(2*n + m), n is the size of costs and m is the maximum of costs array.
S：O(m)

Runtime: 1455 ms, faster than 45.55% of Python3 online submissions for Maximum Ice Cream Bars.
Memory Usage: 28 MB, less than 17.54% of Python3 online submissions for Maximum Ice Cream Bars.
'''
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        count = [0] * (m + 1)
        for c in costs:
            count[c] += 1
            
        ans = 0
        for c in range(1, m + 1):
            if coins < c:
                break
            if not count[c]:
                continue
            take = min(count[c], coins // c)
            ans += take
            coins -= c * take 
        return ans 


