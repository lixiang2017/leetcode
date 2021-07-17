'''
Hash Table + Sort
执行用时：56 ms, 在所有 Python3 提交中击败了78.23% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了54.84% 的用户
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(list(s)))].append(s)
        
        return list(groups.values())

'''
Hash Table + Hash Table
执行用时：60 ms, 在所有 Python3 提交中击败了61.29% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了5.24% 的用户
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
