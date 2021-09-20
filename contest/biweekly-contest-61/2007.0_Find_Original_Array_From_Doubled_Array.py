'''
AC
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        
        original = []
        c = Counter(changed)
        sorted_c = sorted([num for num, _ in c.items()])
        for num in sorted_c:
            if num not in c:
                continue
            if num == 0:
                if c[num] % 2:
                    return []
                else:
                    original += [0] * (c[0] // 2)
                    c.pop(0)
                    continue
            if num * 2 not in c or c[num * 2] < c[num]:
                return []
            else:
                original += [num] * c[num]
                c[num * 2] -= c[num] 
                c.pop(num)
                if 0 == c[num * 2]:
                    c.pop(num * 2)
        
        return original
