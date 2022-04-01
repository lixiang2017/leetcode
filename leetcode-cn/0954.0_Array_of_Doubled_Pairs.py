'''
执行用时：140 ms, 在所有 Python3 提交中击败了71.01% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了7.25% 的用户
通过测试用例：102 / 102
'''
from sortedcontainers import SortedDict

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 2 * arr[0] = arr[1]
        # 2 * arr[2] = arr[3]
        # 2 * arr[4] = arr[5]
        c = Counter(arr)
        s = SortedDict(c)
        for k, v in s.items():
            if v == 0:
                continue
            if k == 0 and v % 2:
                return False
            elif k > 0:
                if 2 * k not in s or s[2 * k] < v:
                    return False 
                else:
                    s[k * 2] -= v 
                    if 0 == s[k * 2]:
                        s.pop(k * 2)                    
            elif k < 0:
                if k % 2 or k // 2 not in s or s[k // 2] < v:
                    return False 
                else:
                    s[k // 2] -= v 
                    if 0 == s[k // 2]:
                        s.pop(k // 2)
            # s.pop(k)  # may be wrong
            s[k] = 0
            
        return True 


'''
执行用时：100 ms, 在所有 Python3 提交中击败了80.43% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了35.51% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = sorted(set(arr))
        for x in s:
            if c[x] == 0:
                continue

            if x < 0:
                if x % 2 or x // 2 not in c or c[x // 2] < c[x]:
                    return False 
                else:
                    c[x // 2] -= c[x]
            elif x == 0:
                if c[x] % 2:
                    return False
            else:
                if x * 2 not in c or c[x * 2] < c[x]:
                    return False 
                else:
                    c[x * 2] -= c[x]
            c[x] = 0
            
        return True 


