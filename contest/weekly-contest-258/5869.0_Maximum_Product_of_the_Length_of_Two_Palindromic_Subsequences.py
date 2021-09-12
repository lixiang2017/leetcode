'''
AC
'''
class Solution:
    def maxProduct(self, s: str) -> int:
        palinlen_mask = []
        N = len(s)
        
        # curr_substr, index, mask, palinlen
        def findAllPalin(curr, i, m, l):
            if curr != '' and curr == curr[:: -1]:
                palinlen_mask.append([l, m])

            if i == N:
                return
            
            # choose
            choose_m = m | (1 << i)
            findAllPalin(curr + s[i], i + 1, choose_m, l + 1)
            # not choose
            findAllPalin(curr, i + 1, m, l)
        
        findAllPalin('', 0, 0, 0)
        
        ans = 0
        palinlen_mask.sort(reverse=True)
        L = len(palinlen_mask)
        for i in range(1, L):
            for j in range(i):
                p1, m1 = palinlen_mask[i]
                p2, m2 = palinlen_mask[j]
                if p1 * p2 < ans:
                    break
                if m1 & m2 == 0:
                    ans = max(ans, p1 * p2)

        return ans