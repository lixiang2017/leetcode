'''
two pointers, T: O(4N), S: O(1)

执行用时：84 ms, 在所有 Python3 提交中击败了49.15% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了88.14% 的用户
通过测试用例：109 / 109
'''
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def checka(l, r):
            while l < r:
                if a[l] != a[r]:
                    return False 
                l += 1
                r -= 1
            return True

        def checkb(l, r):
            while l < r:
                if b[l] != b[r]:
                    return False
                l += 1
                r -= 1
            return True         

        def check_apre_bsuf():
            i, j = 0, n - 1
            while i < j:
                if a[i] != b[j]:
                    return checka(i, j) or checkb(i, j)
                i += 1
                j -= 1
            return True
        
        def check_bpre_asuf():
            i, j = 0, n - 1
            while i < j:
                if b[i] != a[j]:
                    return checka(i, j) or checkb(i, j)
                i += 1
                j -= 1
            return True 
        
        return check_apre_bsuf() or check_bpre_asuf()

'''
输入：
"pvhmupgqeltozftlmfjjde"
"yjgpzbezspnnpszebzmhvp"
输出：
false
预期结果：
true
'''
