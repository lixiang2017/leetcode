'''
heapq
T: O(NlogK)
S: O(K)

注意sliding window左右边界的下标

执行用时：572 ms, 在所有 Python3 提交中击败了45.37% 的用户
内存消耗：39.2 MB, 在所有 Python3 提交中击败了4.99% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # window
        h = [(-x, i) for i, x in enumerate(nums[: k])]
        heapify(h)
        ans = []
        for i in range(n - k):
            # i:     0 ... n-k-1
            # last window   n-k-1 ... n-1
            while h and not (i <= h[0][1] <= i + k - 1):
                heappop(h)
            ans.append(-h[0][0])
            heappush(h, (-nums[i + k], i + k))
        # last one  # n-k ... n-1
        while h and not (n - k <= h[0][1] <= n - 1):
            heappop(h)        
        ans.append(-h[0][0])

        return ans 

