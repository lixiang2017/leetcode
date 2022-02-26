'''

执行用时：40 ms, 在所有 Python3 提交中击败了22.15% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.95% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = self.parseComplex(num1)
        r2, i2 = self.parseComplex(num2)
        r = r1 * r2 - i1 * i2 
        i = i1 * r2 + i2 * r1 
        return str(r) + '+' + str(i) + 'i'
    
    def parseComplex(self, num: str) -> List[int]:
        real, img = num.split('+')
        real = int(real)
        img = int(img.rstrip('i'))
        return real, img

