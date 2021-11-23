'''
hash table

执行用时：52 ms, 在所有 Python3 提交中击败了8.86% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了83.80% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diff_a, diff_b = [], []
        c = Counter()
        max_cnt = 1

        for ss, gg in zip(s, goal):
            c[ss] += 1
            if c[ss] > max_cnt:
                max_cnt = c[ss]
            if ss != gg:
                diff_a.append(ss)
                diff_b.append(gg)
                if len(diff_a) > 2:
                    return False

        return (diff_a == [] and max_cnt > 1) or (set(diff_a) == set(diff_b) and len(diff_a) == 2)
