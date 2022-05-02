'''
brute force

执行用时28 m, 在所有 Python3 提交中击败100.00的用户
内存消耗14.8 M, 在所有 Python3 提交中击败100.00的用户
通过测试用例112 / 112
'''
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        cands = []
        for i, ch in enumerate(number):
            if ch == digit:
                cands.append(number[: i] + number[i + 1: ])
        
        return max(cands)


'''
greedy
思路：第一个遇到满足后一位大于digit的位置，如果没遇到就是最后一次遇到digit

执行用时40 m, 在所有 Python3 提交中击败100.00的用户
内存消耗15 M, 在所有 Python3 提交中击败100.00的用户
通过测试用例112 / 112
'''
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = None
        n = len(number)
        for i, ch in enumerate(number):
            if ch == digit:
                if i + 1 < n and ord(number[i + 1]) > ord(digit):
                    idx = i
                    break
                idx = i 

        return number[: idx] + number[idx + 1: ]

'''
执行用时36 m, 在所有 Python3 提交中击败100.00的用户
内存消耗15 M, 在所有 Python3 提交中击败100.00的用户
'''
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = None
        n = len(number)
        for i, ch in enumerate(number):
            if ch == digit:
                idx = i 
                if i + 1 < n and ord(number[i + 1]) > ord(digit):
                    break
        return number[: idx] + number[idx + 1: ]


