'''
执行用时：36 ms, 在所有 Python3 提交中击败了39.31% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.86% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        h = []
        for ch, cnt in [('a', a), ('b', b), ('c', c)]:
            if cnt != 0:
                # change to negative
                heappush(h, (-cnt, ch))
        
        while h:
            cnt, ch = heappop(h)
            if not (len(ans) > 1 and ans[-1] == ch and ans[-2] == ch):
                ans += ch 
                cnt += 1
                if cnt != 0:
                    heappush(h, (cnt, ch))
            else:
                if h:
                    cnt1, ch1 = heappop(h)
                    ans += ch1
                    cnt1 += 1
                    if cnt1 != 0:
                        heappush(h, (cnt1, ch1))
                    heappush(h, (cnt, ch))
                else:
                    break

        return ans 
