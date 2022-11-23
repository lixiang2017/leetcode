'''
approach: Hash Table
Time: O(highLimit - lowLimit)
Space: O(...)
'''


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        seen = defaultdict(int)
        most = 0
        for num in range(lowLimit, highLimit + 1):
            digits_sum =  sum([int(d) for d in list(str(num))])
            seen[digits_sum] += 1
            if seen[digits_sum] > most:
                most = seen[digits_sum]
        return most

'''
执行用时：348 ms, 在所有 Python3 提交中击败了66.87% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了99.40% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for x in range(lowLimit, highLimit + 1):
            t = 0 
            while x:
                t += x % 10
                x //= 10
            cnt[t] += 1
            ans = max(ans, cnt[t])
        return ans 
        