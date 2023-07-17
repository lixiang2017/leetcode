'''
执行用时：40 ms, 在所有 Python3 提交中击败了83.96% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了69.30% 的用户
通过测试用例：317 / 317
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


'''
执行用时：44 ms, 在所有 Python3 提交中击败了68.62% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了12.24% 的用户
通过测试用例：317 / 317
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        ans, carry = deque(), 0
        i, j = n1 - 1, n2 - 1
        while i >= 0 or j >= 0 or carry:
            s = carry 
            if i >= 0:
                s += int(num1[i])
                i -= 1
            if j >= 0:
                s += int(num2[j])
                j -= 1
            carry, x = divmod(s, 10)
            ans.appendleft(str(x))
        
        return ''.join(ans)


'''
执行用时：40 ms, 在所有 Python3 提交中击败了83.96% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了84.69% 的用户
通过测试用例：317 / 317
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(num1) + eval(num2))

'''
执行用时：56 ms, 在所有 Python3 提交中击败了19.42% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了65.15% 的用户
通过测试用例：317 / 317
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        ans, carry = deque(), 0
        i, j = n1 - 1, n2 - 1
        while i >= 0 or j >= 0 or carry:
            s = carry 
            if i >= 0:
                s += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(num2[j]) - ord('0')
                j -= 1
            carry, x = divmod(s, 10)
            ans.appendleft(chr(x + ord('0')))
        
        return ''.join(ans)
        


'''
执行用时：68 ms, 在所有 Python3 提交中击败了7.58% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了13.44% 的用户
通过测试用例：317 / 317
'''       
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        chars = []
        carry = 0
        it1, it2 = iter(reversed(num1)), iter(reversed(num2))
        while True:
            x1 = next(it1, None)
            x2 = next(it2, None)
            if x1 is None and x2 is None and 0 == carry:
                break
            s = (int(x1) if x1 is not None else 0) + (int(x2) if x2 is not None else 0) + carry
            carry, x = divmod(s, 10)
            chars.append(str(x))

        return ''.join(reversed(chars)) or "0"


'''
执行用时：48 ms, 在所有 Python3 提交中击败了75.11% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了5.26% 的用户
通过测试用例：317 / 317
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        chars = []
        carry = 0
        it1, it2 = iter(reversed(num1)), iter(reversed(num2))
        while True:
            x1 = next(it1, None)
            x2 = next(it2, None)
            if x1 is None and x2 is None and 0 == carry:
                break
            s = (int(x1) if x1 is not None else 0) + (int(x2) if x2 is not None else 0) + carry
            carry, x = divmod(s, 10)
            chars.append(str(x))

        return ''.join(reversed(chars))
