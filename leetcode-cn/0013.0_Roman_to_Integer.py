'''
approach: Hash Table
T: O(N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了93.31% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了60.53% 的用户
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol2value = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        value = 0
        N = len(s)
        i = 0
        while i < N:
            if i + 1 < N and s[i: i + 2] in symbol2value:
                value += symbol2value[s[i: i + 2]]
                i += 2
            else:
                value += symbol2value[s[i]]
                i += 1

        return value
