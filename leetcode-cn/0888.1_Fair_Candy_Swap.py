'''
approach: Sort + Two Pointers
Time: O(M + N + NlogN + MlogM + N + M) = O(NlogN + MlogM), N is the length of A and M is the length of B.
Space: O(1)

执行结果：通过
显示详情
执行用时：368 ms, 在所有 Python 提交中击败了62.35%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了70.59%的用户
'''


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(A), sum(B)
        sizeA, sizeB = len(A), len(B)
        target_diff = (sumA - sumB) / 2
        A.sort()
        B.sort()

        i = j = 0
        while i < sizeA and j < sizeB:
            diff = A[i] - B[j]
            if diff == target_diff:
                return [A[i], B[j]]
            elif diff > target_diff:
                j += 1
            else:
                i += 1

        print 'not found'
        return -1
