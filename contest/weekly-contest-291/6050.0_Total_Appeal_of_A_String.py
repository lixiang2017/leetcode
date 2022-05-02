'''
比赛中没想清楚这个贡献是怎么回事。
pos记录位置倒是知道。
没有想到需要枚举子串左右边界范围。

执行用时：200 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：76 / 76
'''
'''
仅考虑每个位置的字符在最后结果中的贡献
如果一个子串中有多个相同字符，这些相同字符中 [只考虑最左侧的那个]
                  .....a.....a......a.....a......
第一个a贡献范围     [.....a.....a......a.....a......]
第二个a贡献范围     .....a[.....a......a.....a......]
第三个a贡献范围     .....a.....a[......a.....a......]
第四个a贡献范围     .....a.....a......a[.....a......]
对于某个有贡献的字符，(考虑包含这个有贡献字符的子串，这些子串的左右边界)
左边界范围是  (pos_left, i] 
右边界范围是  [i, n - 1]    
'''

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        ans = 0
        pos = [-1] * 26
        for i, ch in enumerate(s):
            d = ord(ch) - ord('a')
            left = i - pos[d]
            right = n - i 
            ans += left * right
            pos[d] = i 
        return ans 


'''
执行用时192 m, 在所有 Python3 提交中击败100.00的用户
内存消耗15.3 M, 在所有 Python3 提交中击败100.00的用户
通过测试用例76 / 76
'''

'''
仅考虑每个位置的字符在最后结果中的贡献
如果一个子串中有多个相同字符，这些相同字符中 [只考虑最右侧的那个]
                  .....a.....a......a.....a......
第一个a贡献范围     [.....a.....a......a.....a......]
第二个a贡献范围     [.....a.....a......a.....]a......
第三个a贡献范围     [.....a.....a......]a.....a......
第四个a贡献范围     [.....a.....]a......a.....a......
对于某个有贡献的字符，(考虑包含这个有贡献字符的子串，这些子串的左右边界)
左边界范围是  [0, i] 
右边界范围是  [i, pos_right)   
所以应该用乘法
'''

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        ans = 0
        pos = [n] * 26
        for i in range(n - 1, -1, -1):
            d = ord(s[i]) - ord('a')
            left = i + 1
            right = pos[d] - i 
            ans += left * right
            pos[d] = i 
        return ans 


'''
ref:
https://leetcode-cn.com/problems/total-appeal-of-a-string/solution/by-endlesscheng-g405/


执行用时192 m, 在所有 Python3 提交中击败100.00的用户
内存消耗15.4 M, 在所有 Python3 提交中击败100.00的用户
通过测试用例76 / 76
'''
class Solution:
    def appealSum(self, s: str) -> int:
        ans, sum_g, pos = 0, 0, [-1] * 26
        for i, ch in enumerate(s):
            d = ord(ch) - ord('a')
            sum_g += i - pos[d]
            ans += sum_g 
            pos[d] = i 
        return ans 



