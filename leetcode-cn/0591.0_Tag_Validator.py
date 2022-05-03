'''
执行用时：40 ms, 在所有 Python3 提交中击败了40.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.00% 的用户
通过测试用例：260 / 260
'''
class Solution:
    def isValid(self, code: str) -> bool:
        code = re.sub(r'<\!\[CDATA\[.*?\]\]>', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'



'''
cdata必须要被包裹起来
输入：
"<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"
输出：
true
预期结果：
false

输入：
"<![CDATA[ABC]]><TAG>sometext</TAG>"
输出：
true
预期结果：
false

必须是嵌套的
输入：
"<A></A><B></B>"
输出：
true
预期结果：
false
'''