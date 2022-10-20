'''
执行用时：52 ms, 在所有 Python3 提交中击败了46.79% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了68.30% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans  = 0
        for _type, color, name in items:
            if ruleKey == 'type':
                ans += int(_type == ruleValue)
            elif ruleKey == 'color':
                ans += int(color == ruleValue)
            elif ruleKey == 'name':
                ans += int(name == ruleValue)
        return ans
