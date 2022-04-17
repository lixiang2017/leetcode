'''
63 / 63 个通过测试用例
状态：通过
执行用时: 760 ms
内存消耗: 37.9 MB
提交时间：18 小时前

a - x - y - b
'''

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for a, b in edges:
            g[a].append((scores[b], b))
            g[b].append((scores[a], a))
        for i, vs in enumerate(g):
            g[i] = nlargest(3, vs)
        
        ans = -1
        for x, y in edges:
            for (score_a, a), (score_b, b) in product(g[x], g[y]):
                # if a != x != y != b:  # wrong
                if y != a and x != b and a != b:   # if len({a, x, y, b}) == 4:
                    ans = max(ans, score_a + scores[x] + scores[y] + score_b)

        return ans 


'''
63 / 63 个通过测试用例
状态：通过
执行用时: 912 ms
内存消耗: 37.7 MB
提交时间：18 小时前

a - x - y - b
'''

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for a, b in edges:
            g[a].append((scores[b], b))
            g[b].append((scores[a], a))
        for i, vs in enumerate(g):
            g[i] = nlargest(3, vs)
        
        ans = -1
        for x, y in edges:
            for score_a, a in g[x]:
                for score_b, b in g[y]:
                    if len({a, x, y, b}) == 4:
                        ans = max(ans, score_a + scores[x] + scores[y] + score_b)

        return ans 

