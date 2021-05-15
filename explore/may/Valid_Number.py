'''
approach: Split and regex

You are here!
Your memory usage beats 60.64 % of python3 submissions.
'''


import re
class Solution:
    def isNumber(self, s: str) -> bool:
        def isDecimal(part):
            pattern = re.compile('^[+-]*(\d+\.|\d+\.\d+|\.\d+)$')
            return bool(pattern.match(part))  
        
        def isInteger(part):
            pattern = re.compile('^[+-]*\d+$')
            return bool(pattern.match(part))                     
            
        splits = re.split('e|E', s)
        if len(splits) > 2:
            return False
        elif 2 == len(splits):
            return (isDecimal(splits[0]) or isInteger(splits[0])) and isInteger(splits[1])
        elif 1 == len(splits):
            return isDecimal(splits[0]) or isInteger(splits[0])
        else:
            return False

        
'''
approach: Split and regex
should be [+-]?, not [+-]*

You are here!
Your runtime beats 92.40 % of python3 submissions.
You are here!
Your memory usage beats 60.64 % of python3 submissions.
'''
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        def isDecimal(part):
            pattern = re.compile('^[+-]?(\d+\.|\d+\.\d+|\.\d+)$')
            return bool(pattern.match(part))  
        
        def isInteger(part):
            pattern = re.compile('^[+-]?\d+$')
            return bool(pattern.match(part))                     
            
        splits = re.split('e|E', s)
        if len(splits) > 2:
            return False
        elif 2 == len(splits):
            return (isDecimal(splits[0]) or isInteger(splits[0])) and isInteger(splits[1])
        elif 1 == len(splits):
            return isDecimal(splits[0]) or isInteger(splits[0])
        else:
            return False
        
        

