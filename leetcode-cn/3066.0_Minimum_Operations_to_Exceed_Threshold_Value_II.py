class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            x, y = heappop(nums), heappop(nums)
            if x >= k:
                break
            ans += 1
            z = min(x, y) * 2 + max(x, y)
            heappush(nums, z)

        return ans