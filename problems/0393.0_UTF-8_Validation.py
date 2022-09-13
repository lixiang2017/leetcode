'''
Runtime: 235 ms, faster than 27.34% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.3 MB, less than 19.59% of Python3 online submissions for UTF-8 Validation.
'''
'''
     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

0 - 127
192 - 223  128 - 191
224 - 239  128 - 191  128 - 191
240 - 247  128 - 191  128 - 191  128 - 191
'''

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            # UTF8 begins
            if 0 <= data[i] <= 127:
                i += 1
            elif 192 <= data[i] <= 223:
                if i + 1 < n and 128 <= data[i + 1] <= 191:
                    i += 2
                else:
                    return False 
            elif 224 <= data[i] <= 239:
                if i + 2 < n and 128 <= data[i + 1] <= 191 and 128 <= data[i + 2] <= 191:
                    i += 3
                else:
                    return False 
            elif 240 <= data[i] <= 247:
                if i + 3 < n and 128 <= data[i + 1] <= 191 and \
                        128 <= data[i + 2] <= 191 and 128 <= data[i + 3] <= 191:
                    i += 4
                else:
                    return False 
            else:
                return False 

        return True
        
'''

Input: [240,162,138,147,145]
Output: true
Expected: false

Input
[240,162,138,147,17]
Output
false
Expected
true
'''

