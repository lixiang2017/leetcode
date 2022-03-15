'''
heapq + pre_min + suf_max
枚举分割点
T: O(2N + 2NlogN) = O(NlogN)
S: O(N)

执行用时：464 ms, 在所有 Python3 提交中击败了72.51% 的用户
内存消耗：34.7 MB, 在所有 Python3 提交中击败了67.77% 的用户
通过测试用例：110 / 110
'''
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        0 ... n-1   n ... 2*n-1    2*n ... 3*n-1
        '''
        m = len(nums)
        n = m // 3
        suf_max = [0] * (2 * n + 1)
        min_pq = nums[2 * n: ]
        heapify(min_pq)
        suf_max[-1] = s = sum(min_pq)
        for i in range(2 * n - 1, n - 1, -1):
            s += nums[i] - heappushpop(min_pq, nums[i])
            suf_max[i] = s 
        
        max_pq = [-x for x in nums[: n]]
        heapify(max_pq)
        pre_min = -sum(max_pq)
        ans = pre_min - suf_max[n]
        for i in range(n, 2 * n):
            pre_min += nums[i] + heappushpop(max_pq, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])

        return ans 

