'''
执行用时：44 ms, 在所有 Python3 提交中击败了11.14% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了53.93% 的用户
通过测试用例：204 / 204
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n:
            if pre == n % 2:
                return False
            pre = n % 2
            n //= 2
        return True

'''
执行用时：36 ms, 在所有 Python3 提交中击败了60.92% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.49% 的用户
通过测试用例：204 / 204
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        return not '00' in b and not '11' in b


'''
执行用时：36 ms, 在所有 Python3 提交中击败了60.92% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了73.80% 的用户
通过测试用例：204 / 204
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not '00' in bin(n) and not '11' in bin(n)
