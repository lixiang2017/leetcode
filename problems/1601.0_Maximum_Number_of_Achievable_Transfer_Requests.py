'''
Runtime: 2076 ms, faster than 29.12% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
Memory Usage: 16.4 MB, less than 81.55% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
'''
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans
    

'''
Runtime: 1296 ms, faster than 60.19% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
Memory Usage: 16.5 MB, less than 53.40% of Python3 online submissions for Maximum Number of Achievable Transfer Requests.
'''
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        delta = [0] * n
        ans, cnt, zero = 0, 0, n
        
        def backtrack(pos: int) -> None:
            nonlocal ans, cnt, zero
            if pos == len(requests):
                if zero == n:
                    ans = max(ans, cnt)
                return 
            
            # not choose
            backtrack(pos + 1)
            # choose
            z = zero 
            cnt += 1
            x, y = requests[pos]
            ## for x
            zero -= delta[x] == 0
            delta[x] -= 1
            zero += delta[x] == 0
            ## for y
            zero -= delta[y] == 0
            delta[y] += 1
            zero += delta[y] == 0
            backtrack(pos + 1)
            ## undo
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1
            zero = z 
        
        backtrack(0)
        return ans
