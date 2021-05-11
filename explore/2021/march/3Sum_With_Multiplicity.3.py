'''
approach: Adapt from 3 Sum
Time: O(N^2), where N is the length of arr.
Space: O(N)

x y z       # all different
x == y != z
x != y == z
x == y == z

You are here!
Your runtime beats 88.89 % of python submissions.
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
        count = collections.Counter(arr)
        keys = sorted(count)

        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:  # x + y + z == target
                    if x < y < z:
                        ans += count[x] * count[y] * count[z]
                    elif x == y < z:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif x < y == z:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    elif x == y == z:
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                    ans %= MOD
                    j += 1
                    k -= 1

        return ans
