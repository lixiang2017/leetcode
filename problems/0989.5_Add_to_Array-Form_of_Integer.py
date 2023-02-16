'''
Runtime: 299 ms, faster than 83.44% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15 MB, less than 65.15% of Python3 online submissions for Add to Array-Form of Integer.
'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        array, carry = [], 0
        for x in reversed(num):
            k, y = divmod(k, 10)
            carry, d = divmod(x + y + carry, 10)
            array.append(d)
            
        while carry or k:
            k, y = divmod(k, 10)
            carry, d = divmod(y + carry, 10)
            array.append(d)
        
        return reversed(array)
        
        