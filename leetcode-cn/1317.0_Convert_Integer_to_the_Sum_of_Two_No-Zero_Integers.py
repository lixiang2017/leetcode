'''
brute force
T: O(NlogN)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了17.83% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了44.59% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        x, y = 1, n - 1
        while x <= y and ('0' in str(x) or '0' in str(y)):
            x += 1
            y -= 1
        return [x, y]

'''
执行用时：32 ms, 在所有 Python3 提交中击败了91.08% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了65.61% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        x, y = 1, n - 1

        def contain0(x):
            if x == 0:
                return True 
            while x:
                if x % 10 == 0:
                    return True 
                x //= 10
            return False

        while x <= y and (contain0(x) or contain0(y)):
            x += 1
            y -= 1
        return [x, y]
        