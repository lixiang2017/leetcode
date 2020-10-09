'''
You are here!
Your runtime beats 60.26 % of python submissions.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        common = ''
        min_len = float('inf')
        for string in strs:
            if len(string) < min_len:
                min_len = len(string)
        
        
        for i in xrange(min_len):
            reach_end = True
            first_string_char = strs[0][i]
            for string in strs[1:]:
                if string[i] != first_string_char:
                    reach_end = False
                    break
                    
            if not reach_end:
                break
            else:
                common += first_string_char
        return common