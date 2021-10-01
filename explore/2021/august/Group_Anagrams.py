'''
Hash Table + Sort

You are here!
Your runtime beats 57.68 % of python3 submissions.
You are here!
Your memory usage beats 77.16 % of python3 submissions.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            memo[sorted_s].append(s)
        return list(memo.values())

'''
Hash Table 

You are here!
Your runtime beats 30.49 % of python3 submissions.
You are here!
Your memory usage beats 19.08 % of python3 submissions.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for s in strs:
            t = [0] * 26
            for ch in s:
                t[ord(ch) - ord('a')] += 1
            memo[tuple(t)].append(s)                
        return list(memo.values())
        