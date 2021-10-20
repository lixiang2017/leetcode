'''
Runtime: 34 ms, faster than 60.67% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.4 MB, less than 37.09% of Python3 online submissions for Reverse Words in a String.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[:: -1])


'''
Runtime: 48 ms, faster than 32.39% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.2 MB, less than 86.72% of Python3 online submissions for Reverse Words in a String.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


'''
Two Pointers

Runtime: 44 ms, faster than 40.39% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.3 MB, less than 86.72% of Python3 online submissions for Reverse Words in a String.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1
                
            if i > j:
                ans.append(s[j + 1: i + 1])
            i = j - 1
            
        return ' '.join(ans)
