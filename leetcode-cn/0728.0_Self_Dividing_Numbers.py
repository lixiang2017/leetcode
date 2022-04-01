'''
T: O((right-left) * logx) = O(4 * (right - left))
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了79.13% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了42.36% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isDividingNumber(num):
            x = num
            while x:
                x, r = divmod(x, 10)
                if 0 == r or num % r != 0:
                    return False
            return True 
        
        return [x for x in range(left, right + 1) if isDividingNumber(x)]
