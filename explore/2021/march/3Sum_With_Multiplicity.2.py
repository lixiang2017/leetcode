'''
approach: Math / Counting with Cases
Time: O(N + W^2), where N is the length of arr, and W is the maximum possible value of arr[i].
Space: O(W)

You are here!
Your runtime beats 61.11 % of python submissions.

x y z       # all different
x == y != z
x != y == z
x == y == z
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
        count = [0] * 101
        for element in arr:
            count[element] += 1

        # all different
        for x in range(101):
            for y in range(x + 1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # x == y != z
        for x in range(101):
            z = target - 2 * x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) / 2 * count[z]
                ans %= MOD

        # x != y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                y = z = (target - x) / 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) / 2
                    ans %= MOD

        # x == y == z
        # for x in range(101):  # no need
        if target % 3 == 0:
            x = target / 3
            ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
            ans %= MOD

        return ans
