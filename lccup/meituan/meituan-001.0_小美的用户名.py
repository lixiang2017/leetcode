'''
https://leetcode-cn.com/problems/BaR9fy/

执行用时：12 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：8.9 MB, 在所有 Python3 提交中击败了14.29% 的用户
'''
n = int(input())

def check(name):
    if len(name) < 2:
        return False
    # first letter
    if not name[0].isalpha():
        return False
    # isalnum()
    if not name.isalnum():
        return False
    # at least one letter and one digit
    containLetter = containDigit = False
    for ch in name:
        if ch.isalpha():
            containLetter = True
        elif ch.isdigit():
            containDigit = True
        if containLetter and containDigit:
            return True
    if not (containLetter and containDigit):
        return False
    return True

while n > 0:
    name = input()
    if check(name):
        print('Accept')
    else:
        print('Wrong')
    n -= 1

'''
输入：
5
Ooook
Hhhh666
ABCD
Meituan
6666
输出：
     Wrong
     Accept
     Wrong
     Wrong
     Wrong
'''


