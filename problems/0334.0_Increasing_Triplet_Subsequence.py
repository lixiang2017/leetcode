'''
T: O(3N)
S: O(2N)

Runtime: 2011 ms, faster than 6.28% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 27.1 MB, less than 6.78% of Python3 online submissions for Increasing Triplet Subsequence.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        small, large = [nums[0]] * n, [nums[-1]] * n 
        for i in range(1, n):
            small[i] = min(small[i - 1], nums[i - 1])
        for i in range(n - 2, -1, -1):
            large[i] = max(large[i + 1], nums[i + 1])
        for i in range(n):
            if small[i] < nums[i] < large[i]:
                return True
        return False

'''
T: O(N)
S: O(1)

Runtime: 1432 ms, faster than 28.25% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.6 MB, less than 48.78% of Python3 online submissions for Increasing Triplet Subsequence.
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = sys.maxsize
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
