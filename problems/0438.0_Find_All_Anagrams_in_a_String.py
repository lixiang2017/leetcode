'''
hash table + sliding window
T: O(N)
S: O(26 * 2)

Runtime: 209 ms, faster than 34.64% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.2 MB, less than 41.94% of Python3 online submissions for Find All Anagrams in a String.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pn = len(p)
        p_cnt = [0] * 26
        part_cnt = [0]* 26
        for p_ch in p:
            p_cnt[ord(p_ch) - ord('a')] += 1
            
        ans = []
        for i, ch in enumerate(s):
            part_cnt[ord(ch) - ord('a')] += 1
            # 0 .. pn-1
            if i < pn - 1:
                continue
            if part_cnt == p_cnt:
                ans.append(i - pn + 1)
            
            part_cnt[ord(s[i - pn + 1]) - ord('a')] -= 1

        return ans 
        
