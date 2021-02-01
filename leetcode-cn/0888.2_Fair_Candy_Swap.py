'''
approach: Set
Time: O(M + N + M * 1) = O(M + N)
Space: O(N)

执行结果：通过
显示详情
执行用时：328 ms, 在所有 Python 提交中击败了91.76%的用户
内存消耗：15.5 MB, 在所有 Python 提交中击败了21.18%的用户
'''

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(A), sum(B)
        setB = set(B)
        target_diff = (sumB - sumA) / 2
        for x in A:
            if x + target_diff in setB:
                return [x, x + target_diff]

        print 'not found'
        return -1
        