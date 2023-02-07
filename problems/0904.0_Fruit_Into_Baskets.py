'''
Runtime: 1052 ms, faster than 48.30% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 19.6 MB, less than 97.64% of Python3 online submissions for Fruit Into Baskets.
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        n = len(fruits)
        i = j = 0
        cur = defaultdict(int)
        while i < n:
            while j < n and (len(cur) < 2 or (len(cur) == 2 and fruits[j] in cur)):
                cur[fruits[j]] += 1
                j += 1
            ans = max(ans, j - i)
            cur[fruits[i]] -= 1
            if  cur[fruits[i]] == 0:
                cur.pop(fruits[i])
            i += 1
        return ans 
        