'''
approach: Two Pointers / Sliding Window + Hash Table
Time: O(N + N) = O(N)
Space: O(N + N) = O(N)

执行结果：
通过
显示详情
执行用时：424 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了45.00%的用户
'''


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K - 1)
    
    def atMostKDistinct(self, A, K):
        size = len(A)
        left = right = 0
        distinct = most = 0
        freq = defaultdict(int)
        while right < size:
            if freq[A[right]] == 0:
                distinct += 1
            freq[A[right]] += 1
            right += 1

            while distinct > K:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    distinct -= 1
                left += 1
            most += right - left
        return most
