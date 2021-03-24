'''
approach: Greedy
=>> 田忌赛马
Time: O(NlogN + NlogN) = O(NlogN)
Space: O(N)

You are here!
Your runtime beats 28.20 % of python submissions
You are here!
Your memory usage beats 97.44 % of python submissions.
'''


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        advantage = []
        N = len(A)
        for b in B:
            idx = self.getAdvant(A, 0, N - 1, b)
            advantage.append(A[idx])
            A.pop(idx)
            N -= 1
        
        return advantage

    # bisect_right
    def getAdvant(self, arr, left, right, target):
        lo = left
        while left < right:
            mid = left + ((right - left) >> 1)  # bracket!!
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        # if we cannot find the least larger number, return the original left-most
        return right if arr[right] > target else lo