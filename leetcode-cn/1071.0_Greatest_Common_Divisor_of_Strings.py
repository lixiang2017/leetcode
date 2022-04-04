'''
执行用时：32 ms, 在所有 Python3 提交中击败了92.44% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了45.06% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        def gcd(x, y):
            if x == 0:
                return y
            return gcd(y % x, x)
        
        common = gcd(m, n)
        for d in range(common, 0, -1):
            if common % d == 0:
                c1, c2, part = m // d, n // d, str1[: d]
                if str1 == part * c1 and str2 == part * c2:
                    return part 
        return ''


'''
执行用时：36 ms, 在所有 Python3 提交中击败了72.97% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了55.81% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1 + str2 == str2 + str1 and str1[: gcd(len(str1), len(str2))] or ''
