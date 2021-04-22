'''
approach: PrefixSum + SortedList + Binary Search
Time: O(M * M * N * logN)
Space: O(N)

执行用时：2784 ms, 在所有 Python3 提交中击败了16.15%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了66.46%的用户
'''

from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M, N = len(matrix), len(matrix[0])
        ans = -sys.maxsize

        for i in range(M):
            total = [0] * N
            for j in range(i, M):
                for c in range(N):
                    total[c] += matrix[j][c]
                
                prefixSum = 0
                # totalSet = SortedList([])  # wrong
                totalSet = SortedList([0])

                for v in total:
                    prefixSum += v
                    idx = totalSet.bisect_left(prefixSum - k)
                    if idx != len(totalSet):
                        ans = max(ans, prefixSum - totalSet[idx])

                    totalSet.add(prefixSum)

        return ans

'''
输入：
[[2,2,-1]]
3
输出：
2
预期结果：
3
'''

