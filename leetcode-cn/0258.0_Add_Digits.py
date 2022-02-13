'''
执行用时：36 ms, 在所有 Python3 提交中击败了51.08% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了64.00% 的用户
通过测试用例：1101 / 1101

'''
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            x = 0
            while num:
                x += num % 10
                num //= 10
            num = x
        return num 


'''
执行用时：48 ms, 在所有 Python3 提交中击败了9.70% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了34.21% 的用户
通过测试用例：1101 / 1101
'''
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(int(ch) for ch in str(num))
        return num 


'''
ref:
https://leetcode.com/problems/add-digits/solution/

执行用时：40 ms, 在所有 Python3 提交中击败了23.40% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了93.11% 的用户
通过测试用例：1101 / 1101
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

'''
执行用时：32 ms, 在所有 Python3 提交中击败了79.74% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了42.04% 的用户
通过测试用例：1101 / 1101
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0



'''
执行用时：48 ms, 在所有 Python3 提交中击败了9.70% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了91.40% 的用户
通过测试用例：1101 / 1101
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return num - int((num - 1) / 9) * 9

'''
中国弃九验算法或余九法
DFS, 每次减去九倍的一个东西

能够被9整除的整数，各位上的数字加起来也必然能被9整除

执行用时：40 ms, 在所有 Python3 提交中击败了23.40% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.89% 的用户
通过测试用例：1101 / 1101
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num 
        num = num // 10 + num % 10
        return self.addDigits(num)
        

