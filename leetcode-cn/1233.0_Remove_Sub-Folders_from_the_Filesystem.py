'''
sort

执行用时：64 ms, 在所有 Python3 提交中击败了88.30% 的用户
内存消耗：25.5 MB, 在所有 Python3 提交中击败了53.19% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        last = ''
        ans = []

        def isSubfolderOfLast(last, f):
            if last == '':
                return False
            m, n = len(last), len(f)
            if m < n and f[: m] == last and f[m] == '/':
                return True 
            return False 

        for f in folder:
            if not isSubfolderOfLast(last, f):
                ans.append(f)
                last = f 

        return ans
