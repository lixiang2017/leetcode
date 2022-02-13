'''
hash table + two pointers/sliding window
T: O(M + N)
S: O(26 * 2)

Runtime: 72 ms, faster than 84.53% of Python3 online submissions for Permutation in String.
Memory Usage: 14 MB, less than 93.32% of Python3 online submissions for Permutation in String.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = [0] * 26
        for ch in s1:
            s1_cnt[ord(ch) - ord('a')] += 1
        ns1 = len(s1)
        
        s2_cnt = [0] * 26
        for i, ch in enumerate(s2):
            if i < ns1 - 1:
                s2_cnt[ord(ch) - ord('a')] += 1
                continue
                
            s2_cnt[ord(ch) - ord('a')] += 1
            if s1_cnt == s2_cnt:
                return True
            s2_cnt[ord(s2[i - ns1 + 1]) - ord('a')] -= 1
            
        return False
