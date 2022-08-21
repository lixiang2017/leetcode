'''
Runtime: 629 ms, faster than 17.91% of Python3 online submissions for Stamping The Sequence.
Memory Usage: 19.3 MB, less than 13.43% of Python3 online submissions for Stamping The Sequence.
'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target_list = list(target)
        processed_indice = []
        m, n = len(stamp), len(target)
        all_indice = set(range(n - m + 1))

        choice = set()
        for i in range(m):
            for j in range(i, m):
                middle = tuple(['_'] * i + list(stamp[i: j + 1]) + ['_'] * (m - 1 - j))
                choice.add(middle)
        
        while True:
            replaced = False
            for idx in all_indice:
                t = tuple(target_list[idx: idx + m])
                if t in choice:
                    target_list[idx: idx + m] = ['_'] * m
                    processed_indice.append(idx)
                    replaced = True
                    break
            
            if not replaced:
                break 
            else:
                all_indice.remove(processed_indice[-1])

        if target_list == ['_'] * n:
            return reversed(processed_indice)
        else:
            return []
        
'''
Input
"zbs"
"zbzbsbszbssbzbszbsss"
Output
[]
Expected
[11,9,17,10,6,5,3,1,16,14,13,8,4,0,15,12,7,2]
'''


'''
记住未stamp部分的起止下标，减少赋值次数

Runtime: 582 ms, faster than 19.40% of Python3 online submissions for Stamping The Sequence.
Memory Usage: 18.9 MB, less than 13.43% of Python3 online submissions for Stamping The Sequence.
'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target_list = list(target)
        processed_indice = []
        m, n = len(stamp), len(target)
        all_indice = set(range(n - m + 1))

        choice = dict()
        for i in range(m):
            for j in range(i, m):
                middle = tuple(['_'] * i + list(stamp[i: j + 1]) + ['_'] * (m - 1 - j))
                choice[middle] = (i, j)
        
        while True:
            replaced = False
            for idx in all_indice:
                t = tuple(target_list[idx: idx + m])
                if t in choice:
                    i, j = choice[t]
                    target_list[idx + i: idx + j + 1] = ['_'] * (j + 1 - i)
                    processed_indice.append(idx)
                    replaced = True
                    break
            
            if not replaced:
                break 
            else:
                all_indice.remove(processed_indice[-1])

        if target_list == ['_'] * n:
            return reversed(processed_indice)
        else:
            return []


