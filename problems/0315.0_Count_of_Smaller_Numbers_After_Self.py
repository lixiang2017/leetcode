'''
binary search
T: O(NlogN)
S: O(N)

Runtime: 5369 ms, faster than 26.89% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 32.3 MB, less than 85.35% of Python3 online submissions for Count of Smaller Numbers After Self.
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n 
        arr = []
        for i in range(n - 1, -1, -1):
            idx = bisect_left(arr, nums[i])
            ans[i] = idx
            bisect.insort(arr, nums[i])
        return ans 
