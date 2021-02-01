'''
approach: Sort + Two Pointers
# Actually, it's no need to assemble pairsA and pairsB.
Time: O(M + N + NlogN + MlogM + N + M) = O(NlogN + MlogM), N is the length of A and M is the length of B.
Space: O(N + M)

执行结果：通过
显示详情
执行用时：504 ms, 在所有 Python 提交中击败了45.88%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了8.23%的用户
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
        # print 'target: ', target_diff
        pairsA = [(value, idx) for idx, value in enumerate(A)]
        pairsB = [(value, idx) for idx, value in enumerate(B)]
        pairsA.sort()
        pairsB.sort()


        i = j = 0
        while i < sizeA and j < sizeB:
            diff = pairsA[i][0] - pairsB[j][0]
            # print 'diff: ', diff
            if diff == target_diff:
                # return [pairsA[i][1], pairsB[j][1]]
                return [pairsA[i][0], pairsB[j][0]]
            elif diff > target_diff:
                j += 1
            else:
                i += 1

        print 'not found'
        return [-1, -1]
        
