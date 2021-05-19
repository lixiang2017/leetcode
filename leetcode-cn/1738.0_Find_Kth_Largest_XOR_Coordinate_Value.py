'''
Prefix XOR using origin space + Sort,T:O(MN + MNlog(MN)),S:O(1)

执行用时：1256 ms, 在所有 Python3 提交中击败了69.56% 的用户
内存消耗：37.6 MB, 在所有 Python3 提交中击败了73.91% 的用户
'''


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M, N = len(matrix), len(matrix[0])
        one_line = [matrix[0][0]]
        # first row
        for j in range(1, N):
            # matrix[0][j] = matrix[0][j-1] ^ matrix[0][j]
            matrix[0][j] ^= matrix[0][j-1]
            one_line.append(matrix[0][j])
        #
        for i in range(1, M):
            for j in range(N):
                if 0 == j:
                    matrix[i][j] ^= matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1] ^ matrix[i][j]
                one_line.append(matrix[i][j])
        one_line.sort(reverse=True)
        return one_line[k - 1]



'''
approach: 滚动数组 + 最小堆
pre: 前一行的前缀异或数组（包含之前所有行）
p: 当前行的前缀异或值

Time: O(MNlogk)
Space: O(N + k)

执行用时：840 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了91.30% 的用户
'''

import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M, N = len(matrix), len(matrix[0])
        queue = []
        pre = [0] * N
        for i in range(M):
            p = 0
            for j in range(N):
                p ^= matrix[i][j]
                num = p ^ pre[j]
                if len(queue) < k:
                    heapq.heappush(queue, num)
                elif num > queue[0]:
                    heapq.heapreplace(queue, num)
                pre[j] = num

        return queue[0]