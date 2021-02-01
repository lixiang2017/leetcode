# coding=utf-8

'''
approach: Hash / Dict
Time: O(M + N + M * 1) = O(M + N)
Space: O(N)

执行结果：通过
显示详情
执行用时：340 ms, 在所有 Python 提交中击败了69.41%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了9.41%的用户
'''

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        sumA, sumB = sum(A), sum(B)
        # setB = set(B)
        dictB = defaultdict(bool)
        # dictB = {num: True for num in B}   # KeyError: 0
        for num in B: dictB[num] = True
        target_diff = (sumB - sumA) / 2
        for x in A:
            # if x + target_diff in setB:
            # print 'idx: ', x + target_diff
            if dictB[x + target_diff]:  
            # if x + target_diff in dictB:
                return [x, x + target_diff]

        print 'not found'
        return -1


if __name__ == '__main__':
    A = [1,1]
    B = [2,2]
    print Solution().fairCandySwap(A, B)  # [1,2]

    A = [1,2,5]
    B = [2,4]
    print Solution().fairCandySwap(A, B) # [5, 4]

    A = [35,17,4,24,10]
    B = [63,21]
    print Solution().fairCandySwap(A, B) # [24, 21]




