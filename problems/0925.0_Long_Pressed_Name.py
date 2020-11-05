'''
Approach: Two Pointer
Time Complexity: O(N + T), where N, T are the lengths of name and typed.
Space Complexity: we have O(1) space complexity.

Success
Details 
Runtime: 16 ms, faster than 90.98% of Python online submissions for Long Pressed Name.
Memory Usage: 13.7 MB, less than 38.11% of Python online submissions for Long Pressed Name.
'''


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_len = len(name)
        typed_len = len(typed)
        i = j = 0
                    
        while i < name_len and j < typed_len:
            if name[i] == typed[j]:  # for name = "leelee"
                i += 1
                j += 1
                continue
            elif i > 0 and name[i - 1] == typed[j]:
                j += 1
                continue
            else:
                return False
        
        if i == name_len:
            while j < typed_len:
                if name[-1] == typed[j]:
                    j += 1
                    continue
                else:
                    return False
        
        return True if i == name_len and j == typed_len else False
         