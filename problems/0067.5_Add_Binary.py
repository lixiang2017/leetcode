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
    
'''
Runtime: 35 ms, faster than 69.29% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 63.05% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2: ]


'''
Runtime: 32 ms, faster than 82.84% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 63.16% of Python3 online submissions for Add Binary.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        seq, carry = [], 0
        for ch1, ch2 in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry, d = divmod(ord(ch1) - ord('0') + ord(ch2) - ord('0') + carry, 2)
            seq.append(str(d))
        if carry:
            seq.append(str(carry))
        return ''.join(reversed(seq))
        