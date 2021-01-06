'''
approach: Two Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 54.03 % of python submissions
You are here!
Your memory usage beats 86.25 % of python submissions
'''


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr.insert(0, 0)
        size = len(arr)
        i = 0
        while i < size:
            j = i + 1
            if j < size:
                if arr[j] - arr[i] > k:
                    # print 'diff: ', arr[j] - arr[i]
                    return arr[i] + k
                else:
                    k -= (arr[j] - arr[i] - 1)
                    # print 'k: ', k
            i += 1
        return arr[-1] + k
        