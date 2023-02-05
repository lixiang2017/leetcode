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
        

'''
bit mask

Runtime: 157 ms, faster than 62.09% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.2 MB, less than 27.00% of Python3 online submissions for Find All Anagrams in a String.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pn = len(p)
        cp = Counter(p)
        diff_mask = 0
        ans = []
        for i, ch in enumerate(s):
            if i < pn:
                cp[ch] -= 1
                if cp[ch] == 0:
                    diff_mask &= ~(1 << (ord(ch) - ord('a')))
                else:
                    diff_mask |= (1 << (ord(ch) - ord('a')))
                if i == pn - 1 and diff_mask == 0:
                    ans.append(0)
                continue
                
            # remove i - pn
            left = s[i - pn]
            cp[left] += 1
            if cp[left] == 0:
                diff_mask &= ~(1 << (ord(left) - ord('a')))
            else:
                diff_mask |= (1 << (ord(left) - ord('a')))
            # add i 
            cp[ch]-= 1
            if cp[ch] == 0:
                diff_mask &= ~(1 << (ord(ch) - ord('a')))
            else:
                diff_mask |= (1 << (ord(ch) - ord('a')))
            
            if diff_mask == 0:
                ans.append(i - pn + 1)
                
        return ans

