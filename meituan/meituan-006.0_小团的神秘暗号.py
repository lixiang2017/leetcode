'''
https://leetcode-cn.com/problems/z3XKBp/

Two Pointers
执行用时：12 ms, 在所有 Python3 提交中击败了85.71% 的用户
内存消耗：9.1 MB, 在所有 Python3 提交中击败了42.86% 的用户
'''
n = int(input())
s = input()
i, j = 0, n - 1
# left
while i < j and s[i] != 'M':
    i += 1
i += 1
while i < j and s[i] != 'T':
    i += 1
i += 1
# right
while i < j and s[j] != 'T':
    j -= 1
while i <= j and s[j] != 'M':
    j -= 1

print(s[i: j])

'''
输入：
10
MMATSATMMT
输出：SATM
'''


'''
执行用时：16 ms, 在所有 Python3 提交中击败了14.29% 的用户
内存消耗：9.9 MB, 在所有 Python3 提交中击败了14.29% 的用户
'''
import re

n = int(input())
s = input()
pat = '^[^M]*M[^T]*T(\S*)M[^M]*T[^T]*$'
print(re.search(pat, s).group(1))



