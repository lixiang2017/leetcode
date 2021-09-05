'''
AC
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        N = len(properties)
        properties.sort()
        attack = [att for att, defense in properties]
        post_max = [0] * N
        for i in range(N - 1, -1, -1):
            if i == N - 1:
                post_max[i] = properties[i][1]
            else:
                post_max[i] = max(post_max[i + 1], properties[i][1])
        
        ans = 0
        for i in range(N):
            x = bisect_right(attack, properties[i][0])
            if x != N and post_max[x] > properties[i][1]:
                ans += 1
        return ans

    
'''
[[5,5],[6,3],[3,6]]
[[2,2],[3,3]]
[[1,5],[10,4],[4,3]]


输入：[[1,1],[2,1],[2,2],[1,2]]
输出：2
预期：1
'''


'''
44 / 44 个通过测试用例
状态：通过
执行用时: 532 ms
内存消耗: 49.2 MB
提交时间：几秒前
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        max_def = ans = 0
        for p in properties:
            if p[1] < max_def:
                ans += 1
            else:
                max_def = p[1]
        return ans
