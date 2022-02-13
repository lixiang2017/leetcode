'''
prefix sum + hash table + binary search
T: O(N + NlogN)
S: O(N)

Runtime: 629 ms, faster than 5.05% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 22.4 MB, less than 8.13% of Python3 online submissions for Subarray Sum Equals K.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = defaultdict(list)
        n = len(nums)
        pre = [0] + [0] * n
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i]
            pre[i + 1] += x
            presum[pre[i + 1]].append(i)

        for i in range(n):
            # target
            t = pre[i] + k
            idx = bisect_left(presum[t], i)
            ans += len(presum[t]) - idx
        return ans
    
        
