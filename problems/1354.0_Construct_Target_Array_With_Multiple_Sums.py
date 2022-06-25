'''
heap 

逆向思维，think in a reversed way
1、需要取模，否则会超时
2、除数可能为 0 
3、长度为 1 的特殊情况

Runtime: 280 ms, faster than 83.53% of Python3 online submissions for Construct Target Array With Multiple Sums.
Memory Usage: 19.9 MB, less than 55.29% of Python3 online submissions for Construct Target Array With Multiple Sums.
'''
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return 1 == target[0]
        
        s = sum(target)
        h = [-t for t in target]
        heapify(h)
        while True:
            t = -heappop(h)
            if t == 1:
                break
            left = s - t
            if t < left:
                return False
            t %= left
            if t == 0 and left != 1:
                return False

            s = t + left
            heappush(h, -t)
            
        return True 
    
'''
TLE
[1,1000000000]


Submitted: 0 minutes ago
Input: [1,1,2]
Output: true
Expected: false


Runtime Error Message: ZeroDivisionError: integer division or modulo by zero
    t %= left
[2]
'''


