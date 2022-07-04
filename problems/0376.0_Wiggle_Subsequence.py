'''
DP
T: O(N^2)
S: O(2N)

Runtime: 263 ms, faster than 13.06% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 13.9 MB, less than 77.55% of Python3 online submissions for Wiggle Subsequence.
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 0 positive, 1 negative
        dp = [[1] * n for _ in range(2)]
        # i...j
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[1][j] = max(dp[1][j], 1 + dp[0][i])
                elif nums[i] > nums[j]:
                    dp[0][j] = max(dp[0][j], 1 + dp[1][i])
        return max(chain(*dp))


'''
DP
T: O(N)
S: O(2N)

Runtime: 53 ms, faster than 56.22% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 13.9 MB, less than 36.01% of Python3 online submissions for Wiggle Subsequence.
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 0 positive, 1 negative
        dp = [[1] * n for _ in range(2)]
        for j in range(1, n): 
            if nums[j - 1] < nums[j]:
                dp[0][j] = dp[0][j - 1]
                dp[1][j] = 1 + dp[0][j - 1]
            elif nums[j - 1] > nums[j]:
                dp[1][j] = dp[1][j - 1]
                dp[0][j] = 1 + dp[1][j - 1]
            else:
                dp[0][j] = dp[0][j - 1]
                dp[1][j] = dp[1][j - 1]
                
        return max(dp[0][-1], dp[1][-1])


'''
DP
T: O(N)
S: O(1)

Runtime: 56 ms, faster than 51.12% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 13.8 MB, less than 77.55% of Python3 online submissions for Wiggle Subsequence.
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1     
        for j in range(1, n): 
            if nums[j - 1] < nums[j]:
                up = down + 1
            elif nums[j - 1] > nums[j]:
                down = up + 1
        return max(up, down)


'''
swap [up = down + 1] with [down = up + 1]
DP
T: O(N)
S: O(1)

Runtime: 85 ms, faster than 24.81% of Python3 online submissions for Wiggle Subsequence.
Memory Usage: 13.9 MB, less than 77.55% of Python3 online submissions for Wiggle Subsequence.
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1     
        for j in range(1, n): 
            if nums[j - 1] < nums[j]:
                down = up + 1
            elif nums[j - 1] > nums[j]:
                up = down + 1
        return max(up, down)



