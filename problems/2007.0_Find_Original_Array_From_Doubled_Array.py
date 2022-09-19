'''
sort + hash table

Runtime: 2937 ms, faster than 22.26% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 34 MB, less than 15.81% of Python3 online submissions for Find Original Array From Doubled Array.
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        distinct = sorted(set(changed))
        original = []
        if c[0] % 2:
            return []
        else:
            original += [0] * (c[0] // 2)
            
        for x in distinct:
            if x != 0 and c[x] != 0:
                if 2 * x not in c or c[x] > c[x * 2]:
                    return []
                original += [x] * c[x]
                c[x * 2] -= c[x]
        
        return original
