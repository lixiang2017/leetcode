'''
backtrack

Runtime: 44 ms, faster than 60.26% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.9 MB, less than 31.50% of Python3 online submissions for Restore IP Addresses.
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        
        ans = []
        def backtrack(parts: List[str], i: int) -> None:
            if i == n:
                if len(parts) == 4:
                    ans.append('.'.join(parts))
                return 
    
            # s[i] as a part
            backtrack(parts + [s[i]], i + 1)
            # concate last part with s[i]
            if parts:
                new_part = parts[-1] + s[i]
                if '0' != new_part[0] and int(new_part) <= 255:
                    parts[-1] = new_part
                    backtrack(parts, i + 1)
    
        backtrack([], 0)
        return ans 
    
