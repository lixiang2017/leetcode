'''
执行用时：200 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # first -> tails
        group = defaultdict(set)
        for s in ideas:
            group[s[0]].add(s[1: ])
        
        ans = 0
        for a, b in combinations(group.values(), 2):
            c = len(a & b)
            ans += 2 * (len(a) - c) * (len(b) - c)
        return ans 

'''
执行用时：204 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # first -> tails
        group = [set() for _ in range(26)]
        for s in ideas:
            group[ord(s[0]) - ord('a')].add(s[1: ])
        
        ans = 0
        for a, b in combinations(group, 2):
            c = len(a & b)
            ans += 2 * (len(a) - c) * (len(b) - c)
        return ans 