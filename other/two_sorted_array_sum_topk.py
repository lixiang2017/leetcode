
'''
今天每日一题：两个有序数组间相加和的Topk问题。给定两个有序数组arr1和arr2，再给定一个整数k，
返回来自arr1和arr2的两个数相加和最大的前k个，两个数必须分别来自两个数组。按照降序输出。[要求]时间复杂度为O(klogk)。
'''


# wrong solution
from typing import List

class Solution:
    def topKSumTwoSortedArray(self, A: List[int], B: List[int], k) -> List[int]:
        ans = []
        M, N = len(A), len(B)
        i = j = 0
        cnt = 0

        while cnt < k and i < M:
            j = 0
            # while cnt < k and A[i] + B[p] >= A[i + 1] + B[j]:  # wrong
            while cnt < k and i + 1 < M and j < N and A[i] + B[j] >= A[i + 1] + B[0]:  # still wrong
                cnt += 1
                ans.append(A[i] + B[j])
                j += 1

            i += 1

        return ans



def verify(A, B, k):
    mix_sum = [a + b for a in A for b in B]
    mix_sum.sort(reverse=True)
    return mix_sum[: k]


def main():
    A = list(range(100, -1, -1))
    B = list(range(200, 70, -1))
    k = 30
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans1 = Solution().topKSumTwoSortedArray(A, B, k)
    print('ans1: ', ans1)
    ans2 = verify(A, B, k)
    print('ans2: ', ans2)
    assert ans1 == ans2

if __name__ == '__main__':
    main()
