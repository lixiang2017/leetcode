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
        min_len = min([len(string) for string in strs])
        
        for i in xrange(min_len):
            first_string_char = strs[0][i]
            if all(first_string_char == string[i] for string in strs):
                common += first_string_char
            else:
                return common
            
        return common
               