'''
59 / 70 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 4 hours, 1 minute ago
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))[k - 1]


'''
70 / 70 test cases passed, but took too long.
    Status: Time Limit Exceeded
Submitted: 0 minutes ago
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        ans = 1
        while low <= high: 
            target = (low + high) // 2
            # count values <= mid
            cnt = 0
            l, h = 1, m
            while l <= h:
                midm = (l + h) // 2
                if midm * n <= target:
                    cnt += (midm - l + 1) * n
                    l = midm + 1
                elif midm * 1 > target:
                    h = midm - 1
                else:
                    for row in range(h, l - 1, -1):
                        # column left, right
                        coll, colr = 1, n
                        choose = 0
                        while coll <= colr:
                            # mid column
                            midc = (coll + colr) // 2
                            if row * midc <= target:
                                choose = midc
                                coll = midc + 1
                            else:
                                colr = midc - 1
                        cnt += choose
                        if cnt >= k:
                            break
                    # count over
                    break

            if cnt >= k:
                ans = target
                high = target - 1
            else:
                low = target + 1
                
        return ans



'''
heap


59 / 70 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
Last executed input: 
9895
28405
100787757

T: O(k * 2 * log(MN)) = O(2MNlog(MN))
'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        h = [(r, r) for r in range(1, m + 1)]
        heapq.heapify(h)
        
        for _ in range(k):
            val, row = heapq.heappop(h)
            nxt = val + row
            if nxt <= row * n:
                heapq.heappush(h, (nxt, row))
                
        return val

