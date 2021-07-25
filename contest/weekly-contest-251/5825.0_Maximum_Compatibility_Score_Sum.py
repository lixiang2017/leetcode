'''
86 / 86 个通过测试用例
状态：通过
执行用时: 2156 ms
内存消耗: 14.8 MB
提交时间：2 分钟前
'''
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        compat = 0
        for perm in permutations(mentors):
            total = 0
            for s1, m1 in zip(students, perm):
                for s, m in zip(s1, m1):
                    if s == m:
                        total += 1
            
            compat = max(compat, total)
        
        return compat
        