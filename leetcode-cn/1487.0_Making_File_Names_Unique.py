'''
hash table

执行用时：180 ms, 在所有 Python3 提交中击败了23.53% 的用户
内存消耗：34.6 MB, 在所有 Python3 提交中击败了5.88% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # name -> idx
        d = {}
        ans = []
        for name in names:
            if name not in d:
                ans.append(name)
                d[name] = 0
            else:
                idx = d[name] + 1
                while name + '(' + str(idx) + ')' in d:
                    idx += 1
                ans.append(name + '(' + str(idx) + ')')
                d[name] = idx 
                d[name + '(' + str(idx) + ')'] = 0
        return ans 

'''
hash table

执行用时：84 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：31.1 MB, 在所有 Python3 提交中击败了22.06% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d, ans = {}, []
        for name in names:
            s = name
            while s in d:
                s = f'{name}({d[name]})'
                d[name] += 1
            d[s] = 1
            ans.append(s)
        return ans 
