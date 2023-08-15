'''
时间 56ms, 击败 9.76%使用 Python3 的用户
内存 15.63mb, 击败 93.90%使用 Python3 的用户
'''
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        prev = 0
        parts = []
        for indice, source, target in sorted(zip(indices, sources, targets)):
            step = len(source)
            if s[indice: indice + step] == source:
                parts.append(s[prev: indice])
                parts.append(target)
                prev = indice + step 
            else:
                parts.append(s[prev: indice + 1])
                prev = indice + 1
        parts.append(s[prev: ])

        return ''.join(parts)
