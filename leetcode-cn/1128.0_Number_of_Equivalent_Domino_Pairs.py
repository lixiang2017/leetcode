'''
dp count

执行用时：56 ms, 在所有 Python3 提交中击败了52.88% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了13.46% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            c[a * 10 + b] += 1
            if c[a * 10 + b] > 1:
                ans += c[a * 10 + b] - 1
        return ans 

'''
no need to use if 

执行用时：60 ms, 在所有 Python3 提交中击败了43.27% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了60.10% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            c[a * 10 + b] += 1
            ans += c[a * 10 + b] - 1
        return ans 

'''
ans += c[a * 10 + b]

执行用时：76 ms, 在所有 Python3 提交中击败了14.42% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了44.23% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            ans += c[a * 10 + b]
            c[a * 10 + b] += 1
        return ans 

'''
执行用时：64 ms, 在所有 Python3 提交中击败了35.10% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了41.35% 的用户
通过测试用例：19 / 19
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(c * (c - 1) // 2 for c in Counter(tuple(sorted(d)) for d in dominoes).values())
        

