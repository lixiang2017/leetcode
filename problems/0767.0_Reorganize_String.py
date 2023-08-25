'''
Runtime: 39 ms, faster than 85.26% of Python3 online submissions for Reorganize String.
Memory Usage: 16.4 MB, less than 9.58% of Python3 online submissions for Reorganize String.
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        h = [(-cnt, ch) for ch, cnt in c.items()]
        heapify(h)
        # max count
        m = -h[0][0]
        if 2 * m - 1 > n:
            return ''
        
        ans = []
        while h:
            neg_cnt1, ch1 = heappop(h)
            ans.append(ch1)
            if h:
                neg_cnt2, ch2 = heappop(h)
                ans.append(ch2)
                neg_cnt2 += 1
                if neg_cnt2:
                    heappush(h, (neg_cnt2, ch2))
            # push to h later
            neg_cnt1 += 1
            if neg_cnt1:
                heappush(h, (neg_cnt1, ch1))
                
        return ''.join(ans)
        
        