'''
Success
Details 
Runtime: 20 ms, faster than 91.08% of Python online submissions for Reorder Data in Log Files.
Memory Usage: 13.8 MB, less than 26.96% of Python online submissions for Reorder Data in Log Files.
'''


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            identifier, after = log.split(' ', 1)  # sep, maxsplit
            if ord('0') <= ord(after[0]) <= ord('9'):
                digit_logs.append(log)
            else:
                letter_logs.append((identifier, after))
                
        letter_logs.sort(key = lambda log: (log[1], log[0]))  # sort by keys, a tuple of keys
        return [identifier + ' ' + after for identifier, after in letter_logs] + digit_logs
    
    
'''
62 / 63 test cases passed.
Status: Wrong Answer
Submitted: 2 minutes ago
Input:
["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
Output:
["g1 act car","a2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
Expected:
["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''