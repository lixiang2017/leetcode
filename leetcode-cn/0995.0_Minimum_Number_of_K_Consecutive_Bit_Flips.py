'''
Brute Force
Time: O(N * K)
Space: O(K)

90 / 110 个通过测试用例
状态：超出时间限制
提交时间：几秒前
'''


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        flips = 0
        size = len(A)
        for i in range(size - K + 1):
            if 1 == A[i]:
                continue
            flips += 1

            # A[i: i + K]
            for j in range(i, i + K):
                A[j] = 1 - A[j]

        all_1s = True
        for idx in range(size - K, size):
            if 0 == A[idx]:
                all_1s = False

        print all_1s
        return flips if all_1s else -1


'''
approach: 差分数组
Time: O(N)
Space: O(N)

ref:
https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/k-lian-xu-wei-de-zui-xiao-fan-zhuan-ci-s-dseq/
'''

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        flips = sumReA = 0
        size = len(A)

        diff = [0] * (size + 1)
        for i in range(size):
            sumReA += diff[i]
            if (0 == (sumReA & 1) ^ A[i]):
                if i + K > size:
                    return -1
                diff[i] += 1
                diff[i + K] -= 1
                sumReA += 1
                flips += 1
                
        return flips 
