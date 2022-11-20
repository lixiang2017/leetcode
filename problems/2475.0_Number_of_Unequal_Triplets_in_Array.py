'''
Runtime: 66 ms, faster than 66.67% of Python3 online submissions for Number of Unequal Triplets in Array.
Memory Usage: 14 MB, less than 33.33% of Python3 online submissions for Number of Unequal Triplets in Array.
'''
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = start = 0
        for i, (x, y) in enumerate(pairwise(nums)):
            if x != y:
                ans += start * (i - start + 1) * (n - i - 1)
                start = i + 1
        return ans


'''
Runtime: 31 ms, faster than 100.00% of Python3 online submissions for Number of Unequal Triplets in Array.
Memory Usage: 13.8 MB, less than 66.67% of Python3 online submissions for Number of Unequal Triplets in Array.
'''
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        ans = 0
        for mid in Counter(nums).values():
            right -= mid
            ans += left * mid * right
            left += mid
        return ans 

'''
Runtime: 5341 ms, faster than 33.33% of Python3 online submissions for Number of Unequal Triplets in Array.
Memory Usage: 13.9 MB, less than 66.67% of Python3 online submissions for Number of Unequal Triplets in Array.

Time Limit Exceeded
'''
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(len(set(t)) == 3 for t in product(nums, repeat=3)) // 6
