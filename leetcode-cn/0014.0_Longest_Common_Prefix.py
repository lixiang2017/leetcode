'''
执行用时：36 ms, 在所有 Python3 提交中击败了63.76% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了82.52% 的用户
通过测试用例：123 / 123
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        for column in zip(*strs):
            if len(one := set(column)) == 1:
                pre += list(one)[0]
            else:
                break
                
        return pre