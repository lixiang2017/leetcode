'''
ref:
https://leetcode.cn/problems/minimum-cost-to-make-array-equal/solution/by-endlesscheng-i10r/

Runtime: 419 ms, faster than 89.71% of Python3 online submissions for Minimum Cost to Make Array Equal.
Memory Usage: 34.6 MB, less than 41.18% of Python3 online submissions for Minimum Cost to Make Array Equal.
'''
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        ans = total = sum((x - pairs[0][0]) * c for x, c in pairs)
        sum_cost = sum(cost)
        for (x0, c), (x1, _) in pairwise(pairs):
            sum_cost -= c * 2
            total -= sum_cost * (x1 - x0)
            ans = min(ans, total)
        return ans
        
'''
Runtime: 404 ms, faster than 97.06% of Python3 online submissions for Minimum Cost to Make Array Equal.
Memory Usage: 34.6 MB, less than 41.18% of Python3 online submissions for Minimum Cost to Make Array Equal.
'''
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        ans = total = sum((x - pairs[0][0]) * c for x, c in pairs)
        sum_cost = sum(cost)
        for (x0, c), (x1, _) in pairwise(pairs):
            sum_cost -= c * 2
            total -= sum_cost * (x1 - x0)
            if total <= ans:
                ans = total
            else:
                break
        return ans
        

'''
Runtime: 376 ms, faster than 100.00% of Python3 online submissions for Minimum Cost to Make Array Equal.
Memory Usage: 34.5 MB, less than 42.65% of Python3 online submissions for Minimum Cost to Make Array Equal.
'''
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        _sum, mid = 0, (sum(cost) + 1) // 2
        for x, c in pairs:
            _sum += c
            if _sum >= mid:
                return sum(abs(y - x) * c for y, c in pairs)
                