'''
BFS

Runtime: 3758 ms, faster than 28.80% of Python3 online submissions for Jump Game II.
Memory Usage: 15.8 MB, less than 11.50% of Python3 online submissions for Jump Game II.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        seen_indices = {0}
        q = deque([(0, 0)])
        while q:
            i, step = q.popleft()
            for j in range(1, nums[i] + 1):
                if i + j == n - 1:
                    return step + 1
                if i + j not in seen_indices:
                    seen_indices.add(i + j)
                    q.append((i + j, step + 1))


'''
DP

Runtime: 9148 ms, faster than 14.34% of Python3 online submissions for Jump Game II.
Memory Usage: 15.1 MB, less than 22.88% of Python3 online submissions for Jump Game II.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i, x in enumerate(nums):
            for j in range(1, x + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
                else:
                    break
        return dp[-1]
        
