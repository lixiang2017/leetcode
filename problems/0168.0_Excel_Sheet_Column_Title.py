'''

Runtime: 60 ms, faster than 9.10% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.6 MB, less than 99.84% of Python3 online submissions for Excel Sheet Column Title.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber, seq = divmod(columnNumber, 26)
            if seq == 0:
                seq += 26
                columnNumber -= 1
            ans = chr(ord('A') + seq - 1) + ans
        
        return ans


'''
Runtime: 35 ms, faster than 64.63% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.9 MB, less than 80.85% of Python3 online submissions for Excel Sheet Column Title.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber:
            columnNumber, seq = divmod(columnNumber, 26)
            if seq == 0:
                seq += 26
                columnNumber -= 1
            arr.append(chr(ord('A') + seq - 1))
            
        arr.reverse()
        return ''.join(arr)

'''
Runtime: 46 ms, faster than 39.42% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 13.9 MB, less than 80.85% of Python3 online submissions for Excel Sheet Column Title.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber:
            columnNumber, seq = divmod(columnNumber - 1, 26)
            arr.append(chr(ord('A') + seq))
            
        arr.reverse()
        return ''.join(arr)


'''
Runtime: 43 ms, faster than 49.33% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 16.4 MB, less than 23.11% of Python3 online submissions for Excel Sheet Column Title.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber:
            columnNumber, x = divmod(columnNumber, 26)
            if 0 == x:
                x = 26
                columnNumber -= 1
            arr.append(chr(x + ord('A') - 1))
        return ''.join(reversed(arr))
            
            