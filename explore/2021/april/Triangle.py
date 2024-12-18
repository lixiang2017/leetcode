'''
approach: Iteration / DP
Time: O(N*N) = O(N^2), where N is the length of triangle.
Space: O(N + N) = O(N)

You are here!
Your runtime beats 59.65 % of python3 submissions.
You are here!
Your memory usage beats 95.11 % of python3 submissions
'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        presums = [0] * N
        sums = [0] * N
        for i in range(N):
            presums = sums[:]
            for j in range(i + 1):
                if 0 == j:
                    sums[j] = presums[j] + triangle[i][j]
                elif i == j:
                    sums[j] = presums[j - 1] + triangle[i][j]
                else:
                    sums[j] = min(presums[j] + triangle[i][j], presums[j - 1] + triangle[i][j]) 
            
        return min(sums)




'''
approach: Thinking Reversely, add from bottom to top
Time: O(N^2)
Space: O(1)

You are here!
Your runtime beats 59.65 % of python3 submissions.
You are here!
Your memory usage beats 66.62 % of python3 submissions.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        for i in range(N - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]