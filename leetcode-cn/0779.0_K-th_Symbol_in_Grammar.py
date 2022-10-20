'''
recursion

执行用时：40 ms, 在所有 Python3 提交中击败了42.21% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了38.96% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0    
        prev = self.kthGrammar(n - 1, (k + 1) // 2)
        if prev == 0:
            if k & 1:
                return 0
            else:
                return 1
        else:
            if k & 1:
                return 1
            else:
                return 0


'''
recursion

执行用时：36 ms, 在所有 Python3 提交中击败了72.08% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了44.80% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        prev = self.kthGrammar(n - 1, (k + 1) // 2)
        if prev == 0:
            return 1 - (k & 1)
        else:
            return k & 1


'''
想起了数电里的卡诺图，不过已经忘了怎么化简为逻辑表达式了

recursion

执行用时：32 ms, 在所有 Python3 提交中击败了90.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了33.77% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0        
        prev = self.kthGrammar(n - 1, (k + 1) // 2)
        return int((k & 1) == prev)


'''
卡诺图

执行用时：24 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.06% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0        
        prev = self.kthGrammar(n - 1, (k + 1) // 2)
        return (k & 1 & prev) + ((1 - (k & 1)) & (1 - prev))



'''
执行用时：40 ms, 在所有 Python3 提交中击败了42.21% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了25.32% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0        
        prev = self.kthGrammar(n - 1, (k + 1) // 2)
        return 1 - ((k & 1) ^ prev)
