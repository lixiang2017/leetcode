'''
sort + priority queque
T: O(NlogN + NlogN)
S: O(N)

Runtime: 1039 ms, faster than 72.14% of Python3 online submissions for Maximum Subsequence Score.
Memory Usage: 38.6 MB, less than 32.44% of Python3 online submissions for Maximum Subsequence Score.
'''
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda p: -p[1])
        h = [pairs[i][0] for i in range(k)]
        heapify(h)
        s = sum(h)
        ans = s * pairs[k - 1][1]
        for i in range(k, n):
            ans = max(ans, pairs[i][1] * (s - h[0] + pairs[i][0]))
            s += pairs[i][0]
            heappush(h, pairs[i][0])
            s -= heappop(h)
        return ans 
