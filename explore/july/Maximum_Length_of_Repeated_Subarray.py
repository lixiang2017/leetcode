'''
approach: DP
Time: O(MN)
Space: O(MN)

You are here!
Your runtime beats 37.09 % of python3 submissions.
You are here!
Your memory usage beats 59.38 % of python3 submissions.
'''

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        max_len = 0
        for i in range(N):
            for j in range(M):
                if nums2[i] == nums1[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len

'''
[1,2,3,2,1]
[3,2,1,4]
[1,2,3,2,1]
[3,2,1,4,7]
[0,0,0,0,0]
[0,0,0,0,0]
'''


'''
approach: DP
Time: O(MN)
Space: O(2M) = O(M)

You are here!
Your runtime beats 60.36 % of python3 submissions.
You are here!
Your memory usage beats 95.44 % of python3 submissions.
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        # dp = [[0] * (M + 1) for _ in range(N + 1)]
        prev, post = [0] * (M + 1), [0] * (M + 1)
        max_len = 0
        for i in range(N):
            for j in range(M):
                if nums2[i] == nums1[j]:
                    # dp[i][j] = dp[i - 1][j - 1] + 1
                    post[j] = prev[j - 1] + 1 
                    max_len = max(max_len, post[j])
                else:
                    post[j] = 0
                    
            prev[:] = post[:]
        
        return max_len
