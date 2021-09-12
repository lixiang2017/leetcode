'''
Two Pass
从头到尾以及从尾到头遍历两遍括号串。
从左往右可以保证正确判断右括号是否可以全匹配；
从右往左可以保证正确判断左括号是否可以全匹配。

执行用时：28 ms, 在所有 Python3 提交中击败了88.47% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了51.12% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        # left star right
        # from beginning
        l = st = r = 0
        for ch in s:
            if '(' == ch:
                l += 1
            elif ')' == ch:
                r += 1
            else:
                st += 1
            if l + st < r:
                return False
        # from the end
        l = st = r = 0
        for ch in s[:: -1]:
            if '(' == ch:
                l += 1
            elif ')' == ch:
                r += 1
            else:
                st += 1
            if l > st + r:
                return False

        return True


'''
记录当前未匹配左括号数量的范围即可。只需遍历一遍，不需要使用栈。
这道题是普通括号匹配的变体。回忆一下一般的括号匹配（即没有'*'这个特殊符号），一般用栈来做，栈用来存储左括号，每当遇到右括号时出栈。实际上，这个栈不是必须的，只需要用一个变量记录当前未匹配左括号的数量即可。
从这个角度来看，这道题就会简单很多，加入'*'号后，未匹配左括号的数量从一个值变成了一个范围，所以只需要转变思路，用两个变量来记录这个范围的上下界即可。

执行用时：32 ms, 在所有 Python3 提交中击败了69.71% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.64% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        # low high
        lo = hi = 0
        for ch in s:
            if '(' == ch:
                lo += 1
                hi += 1
            elif ')' == ch:
                lo = max(0, lo - 1)
                hi -= 1
                if hi < 0:
                    return False
            else:
                lo = max(0, lo - 1)
                hi += 1

        return lo == 0

