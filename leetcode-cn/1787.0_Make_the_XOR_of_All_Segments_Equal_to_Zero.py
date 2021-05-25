'''
approach: DP
Time: O(1024k + N)
Space: O(2048 + N/k)
'''


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x [0, 2^10)
        MAXX = 2 ** 10

        N = len(nums)
        f = [float('inf')] * MAXX
        # edge case, f(-1, 0) = 0
        f[0] = 0

        for i in range(k):
            # i-th group dict
            count = Counter()
            size = 0
            for j in range(i, N, k):
                count[nums[j]] += 1
                size += 1
            
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)
            
            f = [val + size for val in g]
        return f[0]
