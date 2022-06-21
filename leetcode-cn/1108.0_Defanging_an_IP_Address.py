'''
执行用时：28 ms, 在所有 Python3 提交中击败了96.86% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.11% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


'''
执行用时：32 ms, 在所有 Python3 提交中击败了88.60% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.47% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))



'''
执行用时：36 ms, 在所有 Python3 提交中击败了67.98% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.74% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for ch in address:
            if ch == '.':
                ans += '[.]'
            else:
                ans += ch 
        return ans 
