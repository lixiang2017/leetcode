'''
DP
T: O(5N)
S: O(1)

Runtime: 26 ms, faster than 96.82% of Python3 online submissions for Count Sorted Vowel Strings.
Memory Usage: 13.8 MB, less than 96.44% of Python3 online submissions for Count Sorted Vowel Strings.
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # ends with a e i o u 
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = a, a + e, a + e + i, a + e + i + o, a + e + i + o + u
        return a + e + i + o + u

'''
DP
T: O(5N)
S: O(5N)

Runtime: 76 ms, faster than 17.53% of Python3 online submissions for Count Sorted Vowel Strings.
Memory Usage: 13.9 MB, less than 65.31% of Python3 online submissions for Count Sorted Vowel Strings.
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # ends with a e i o u 
        dp = [[1] * 5] + [[0] * 5 for _ in range(n - 1)]
        for i in range(n - 1):
            for j in range(5):
                dp[i + 1][j] = sum(dp[i][: j + 1])
        return sum(dp[-1])

