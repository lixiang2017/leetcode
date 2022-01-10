'''
Runtime: 28 ms, faster than 93.01% of Python3 online submissions for Add Binary.
Memory Usage: 14.3 MB, less than 55.41% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reverse_sum, carry = [], 0
        for aa, bb in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry, tail = divmod(int(aa) + int(bb) + carry, 2)
            reverse_sum.append(str(tail))
        if carry:
            reverse_sum.append(str(carry))
            
        return ''.join(reversed(reverse_sum))
    
    