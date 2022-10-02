'''
two pointers, T: O(N), S: O(2N)

执行用时：1468 ms, 在所有 Python3 提交中击败了9.03% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了66.45% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        c1, c2 = Counter(start), Counter(end)
        if c1 != c2:
            return False
        s, e = start.replace('X', ''), end.replace('X', '')
        if s != e:
            return False

        n = len(end)
        i = 0
        ss, ee = list(start), list(end)
        while i < n:
            if ss[i] == ee[i]:
                i += 1
            elif ss[i] == 'X' and ee[i] == 'L':
                # to find next 'L' in ss 
                j = i + 1
                while j < n and ss[j] != 'L':
                    j += 1
                if j < n and ss[j] == 'L':
                    ss[j] = 'X'
                    i += 1
                else:
                    return False 
            elif ss[i] == 'R' and ee[i] == 'X':
                # to find next 'R' in ee 
                j = i + 1
                while j < n and ee[j] != 'R':
                    j += 1
                if j < n and ee[j] ==  'R':
                    ee[j] = 'X'
                    i += 1
                else:
                    return False
            else:
                return False

        return True


'''
执行用时：2244 ms, 在所有 Python3 提交中击败了9.03% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了25.81% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(end)
        i = 0
        ss, ee = list(start), list(end)
        while i < n:
            if ss[i] == ee[i]:
                i += 1
            elif ss[i] == 'X' and ee[i] == 'L':
                # to find next 'L' in ss 
                j = i + 1
                while j < n:
                    # skip 'X'. 'R' will be wrong
                    if ss[j] == 'R':
                        return False
                    elif ss[j] == 'X':
                        j += 1
                    else:
                        break
                if j < n and ss[j] == 'L':
                    ss[j] = 'X'
                    i += 1
                else:
                    return False 
            elif ss[i] == 'R' and ee[i] == 'X':
                # to find next 'R' in ee 
                j = i + 1
                while j < n:
                    # skip 'X'. 'L' will be wrong
                    if ee[j] == 'L':
                        return False
                    elif ee[j] == 'X':
                        j += 1
                    else:
                        break
                if j < n and ee[j] ==  'R':
                    ee[j] = 'X'
                    i += 1
                else:
                    return False
            else:
                return False

        return True



'''
执行用时：2180 ms, 在所有 Python3 提交中击败了9.03% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了52.90% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(end)
        i = 0
        ss, ee = list(start), list(end)
        while i < n:
            if ss[i] == ee[i]:
                i += 1
            elif ss[i] == 'X' and ee[i] == 'L':
                # to find next 'L' in ss 
                j = i + 1
                Found = False
                while j < n:
                    # skip 'X'. 'R' will be wrong
                    if ss[j] == 'R':
                        return False
                    elif ss[j] == 'X':
                        j += 1
                    else:
                        ss[j] = 'X'
                        i += 1
                        Found = True
                        break
                if not Found:
                    return False
            elif ss[i] == 'R' and ee[i] == 'X':
                # to find next 'R' in ee 
                j = i + 1
                Found = False
                while j < n:
                    # skip 'X'. 'L' will be wrong
                    if ee[j] == 'L':
                        return False
                    elif ee[j] == 'X':
                        j += 1
                    else:
                        ee[j] = 'X'
                        i += 1
                        Found = True
                        break
                if not Found:
                    return False
            else:
                return False

        return True


'''
"RXXLRXRXL"
"XRLXXRRLX"
"X"
"L"
"RLX"
"XLR"
'''
