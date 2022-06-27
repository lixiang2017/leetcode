'''
运行时间：57ms 超过5.76% 用Python 3提交的代码
占用内存：4680KB 超过61.98%用Python 3提交的代码 
'''
import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

def encode(s):
    en = ''
    for ch in s:
        if ch.isalpha():
            if 'a' <= ch < 'z':
                idx = ord(ch) - ord('a') + ord('A') + 1
            elif 'A' <= ch < 'Z':
                idx = ord(ch) - ord('A') + ord('a') + 1
            elif ch == 'Z':
                idx = ord('a')
            elif ch == 'z':
                idx = ord('A')
            x = chr(idx)
        elif ch.isdigit():
            x = (int(ch) + 1) % 10 
        en += str(x)
    return en 

def decode(s):
    de = ''
    for ch in s:
        if ch.isalpha():
            if 'a' < ch <= 'z':
                idx = ord(ch) - ord('a') + ord('A') - 1
            elif 'A' < ch <= 'Z':
                idx = ord(ch) - ord('A') + ord('a') - 1
            elif ch == 'A':
                idx = ord('z')
            elif ch == 'a':
                idx = ord('Z')
            x = chr(idx)
        elif ch.isdigit():
            x = (int(ch) + 9) % 10
        de += str(x)
    return de 

print(encode(s1))
print(decode(s2))



