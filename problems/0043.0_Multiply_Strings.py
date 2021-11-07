'''
Runtime: 28 ms, faster than 96.17% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.2 MB, less than 82.06% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


'''
simulation

Runtime: 216 ms, faster than 19.20% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.3 MB, less than 59.17% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        L1, L2 = len(num1), len(num2)
        ans = [0] * (L1 + L2)
        
        def add2ans(product, shift):
            nonlocal ans
            i = L1 + L2 - 1 - shift
            while product:
                product, ans[i] = divmod(product + ans[i], 10)
                i -= 1
        
        for i, ch1 in enumerate(num1):
            if ch1 == '0':
                continue
            for j, ch2 in enumerate(num2):
                if ch2 == '0':
                    continue
                product = (ord(ch1) - ord('0')) * (ord(ch2) - ord('0'))
                shift = L1 - (i + 1) + L2 - (j + 1)
                add2ans(product, shift)
                
        ans = ''.join(map(str, ans)).lstrip('0')
        return [ans, '0'][ans == '']


'''
simulation

Runtime: 192 ms, faster than 24.33% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.3 MB, less than 29.49% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        L1, L2 = len(num1), len(num2)
        ans = [0] * (L1 + L2)
        
        for i, ch1 in enumerate(num1):
            if ch1 == '0':
                continue
            for j, ch2 in enumerate(num2):
                if ch2 == '0':
                    continue
                product = (ord(ch1) - ord('0')) * (ord(ch2) - ord('0'))
                shift = L1 - (i + 1) + L2 - (j + 1)
                # add to ans
                k = L1 + L2 - 1 - shift
                while product:
                    product, ans[k] = divmod(product + ans[k], 10)
                    k -= 1
                
        ans = ''.join(map(str, ans)).lstrip('0')
        return [ans, '0'][ans == '']

