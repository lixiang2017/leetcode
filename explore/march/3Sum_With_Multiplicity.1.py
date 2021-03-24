'''
approach: Sort + Two Pointers (Three Pointers)
Time: O(N^2)
Space: O(1)

You are here!
Your runtime beats 25.00 % of python submissions.
'''

class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        MOD = 10 ** 9 + 7
        arr.sort()
        N = len(arr)
        for i in range(N):
            T = target - arr[i]
            j, k = i + 1, N - 1
            while j < k:
                if arr[j] + arr[k] > T:
                    k -= 1
                elif arr[j] + arr[k] < T:
                    j += 1
                else:
                    if arr[j] == arr[k]:
                        M = k - j + 1
                        ans += M * (M - 1) / 2
                        ans %= MOD
                        break
                    else:
                        left = right = 1
                        while j + 1 < k and arr[j] == arr[j + 1]:
                            left += 1
                            j += 1
                        while k - 1 > j and arr[k] == arr[k - 1]:
                            right += 1
                            k -= 1
                        ans += left * right
                        ans %= MOD
                        j += 1
                        k -= 1

        return ans



