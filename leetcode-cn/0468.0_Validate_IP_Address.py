'''
simulation

执行用时：28 ms, 在所有 Python3 提交中击败了97.25% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.66% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isValidIPv4(queryIP):
            return 'IPv4'
        if self.isValidIPv6(queryIP):
            return 'IPv6'
        return 'Neither'
    
    def isValidIPv4(self, queryIP: str) -> bool:
        parts = queryIP.split('.')
        if 4 != len(parts):
            return False 
        for part in parts:
            if not self.isValid0to255(part):
                return False
        return True 
    
    def isValid0to255(self, part) -> bool:
        # leading zero
        if (len(part) > 1 and part[0] == '0') or len(part) < 1 or len(part) > 3:
            return False 
        x = 0
        for p in part:
            if not '0' <= p <= '9':
                return False 
            x *= 10
            x += ord(p) - ord('0')
        return 0 <= x <= 255 

    def isValidIPv6(self, queryIP: str) -> bool:
        parts = queryIP.split(':')
        if len(parts) != 8:
            return False 
        for part in parts:
            if len(part) < 1 or len(part) > 4:
                return False
            for p in part:
                if not ('a' <= p <= 'f' or 'A' <= p <= 'F' or '0' <= p <= '9'):
                    return False 
        return True 


'''
all

执行用时：40 ms, 在所有 Python3 提交中击败了40.72% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了74.28% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isValidIPv4(queryIP):
            return 'IPv4'
        if self.isValidIPv6(queryIP):
            return 'IPv6'
        return 'Neither'
    
    def isValidIPv4(self, queryIP: str) -> bool:
        parts = queryIP.split('.')
        return 4 == len(parts) and all(self.isValid0to255(part) for part in parts)
    
    def isValid0to255(self, part) -> bool:
        # leading zero
        if (len(part) > 1 and part[0] == '0') or len(part) < 1 or len(part) > 3:
            return False 
        return all(p.isdigit() for p in part) and 0 <= int(part) <= 255 

    def isValidIPv6(self, queryIP: str) -> bool:
        parts = queryIP.split(':')
        validChar = lambda p: 'a' <= p <= 'f' or 'A' <= p <= 'F' or '0' <= p <= '9'
        return 8 == len(parts) and all(1 <= len(part) <= 4 for part in parts) and \
            all(validChar(p) for part in parts for p in part)


'''
尝试优雅一点

执行用时：36 ms, 在所有 Python3 提交中击败了70.15% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了54.88% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isValidIPv4(queryIP):
            return 'IPv4'
        if self.isValidIPv6(queryIP):
            return 'IPv6'
        return 'Neither'
    
    def isValidIPv4(self, queryIP: str) -> bool:
        parts = queryIP.split('.')
        return 4 == len(parts) and all(self.isValidIPv4Part(part) for part in parts)
    
    def isValidIPv4Part(self, part: str) -> bool:
        if (len(part) > 1 and part[0] == '0') or not 0 < len(part) < 4:
            return False 
        return all(p.isdigit() for p in part) and 0 <= int(part) <= 255 

    def isValidIPv6(self, queryIP: str) -> bool:
        parts = queryIP.split(':')
        return 8 == len(parts) and all(self.isValidIPv6Part(part) for part in parts) 

    def isValidIPv6Part(self, part: str) -> bool:
        validChar = lambda p: 'a' <= p <= 'f' or 'A' <= p <= 'F' or p.isdigit()
        return 1 <= len(part) <= 4 and all(validChar(p) for p in part)



