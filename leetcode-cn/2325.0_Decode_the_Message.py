'''
hash table

执行用时：40 ms, 在所有 Python3 提交中击败了63.86% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了30.69% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {}
        start = ord('a')
        for ch in key:
            if ch == ' ' or ch in cipher:
                continue
            cipher[ch] = chr(start)
            start += 1

        return ''.join(cipher.get(ch, ' ') for ch in message)

