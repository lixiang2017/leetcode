'''
PrefixSum + Hash Table, T:O(M^2*N),S:O(N)

执行用时：988 ms, 在所有 Python3 提交中击败了25.41% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        def subarraySum(nums: List[int], k: int) -> int:
            count = pre = 0
            seen = Counter([0])
            for x in nums:
                pre += x
                if pre - k in seen:
                    count += seen[pre - k]
                seen[pre] += 1
            return count

        ans = 0
        for i in range(M):
            total = [0] * N
            for j in range(i, M):
                for c in range(N):
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)
        return ans
